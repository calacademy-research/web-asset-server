import traceback
import pandas as pd
from picturae_import_utils import remove_two_index
import time_utils
from datetime import datetime
from datetime import timedelta
import hmac
import settings
import sys
from specify_db import SpecifyDb

class SqlCsvTools():
    def __init__(self, config):
        self.config = config
        self.connection = SpecifyDb(db_config_class=self.config)
    def sql_db_connection(self):
        """standard connector"""
        return self.connection.connect()

    def get_record(self, sql):
        """dbtools get_one_record"""
        return self.connection.get_one_record(sql=sql)

    def get_cursor(self):
        """standard db cursor"""
        return self.connection.get_cursor()


    def commit(self):
        """standard db commit"""
        return self.connection.commit()


    # static methods
    def check_agent_name_sql(self, first_name: str, last_name: str, middle_initial: str, title: str):
        """create_name_sql: create a custom sql string, based on number of non-na arguments, the
                            database does not recognize empty strings '' and NA as equivalent.
                            Has conditional to ensure the first statement always starts with WHERE
            args:
                first_name: first name of agent
                last_name: last name of agent
                middle_initial: middle initial of agent
                title: agent's title. (mr, ms, dr. etc..)
        """
        sql = f'''SELECT AgentID FROM agent'''
        statement_count = 0
        if not pd.isna(first_name):
            statement_count += 1
            sql += f''' WHERE FirstName = "{first_name}"'''
        else:
            statement_count += 1
            sql += f''' WHERE FirstName IS NULL'''

        if not pd.isna(last_name):
            sql += f''' AND LastName = "{last_name}"'''

        else:
            sql += f''' AND FirstName IS NULL'''

        if not pd.isna(middle_initial):
            sql += f''' AND MiddleInitial = "{middle_initial}"'''
        else:
            sql += f''' AND MiddleInitial IS NULL'''

        if not pd.isna(title):
            sql += f''' AND Title = "{title}"'''
        else:
            sql += f''' AND Title IS NULL'''

        sql += ''';'''

        result = self.get_record(sql=sql)

        if isinstance(result, (list, dict, set)):
            return result[0]
        else:
            return result

    def get_one_match(self, tab_name, id_col, key_col, match, match_type="string"):
        """populate_sql:
                creates a custom select statement for get one record,
                from which a result can be gotten more seamlessly
                without having to rewrite the sql variable every time
           args:
                tab_name: the name of the table to select
                id_col: the name of the column in which the unique id is stored
                key_col: column on which to match values
                match: value with which to match key_col
                match_type: "string" or "integer", optional with default as "string"
                            puts quotes around sql terms or not depending on data type
        """
        sql = ""
        if match_type == "string":
            sql = f'''SELECT {id_col} FROM {tab_name} WHERE `{key_col}` = "{match}";'''
        elif match_type == "integer":
            sql = f'''SELECT {id_col} FROM {tab_name} WHERE `{key_col}` = {match};'''

        result = self.get_record(sql=sql)

        if isinstance(result, (list, dict, set)):
            return result[0]
        else:
            return result



    def create_insert_statement(self, col_list: list, val_list: list, tab_name: str):
        """create_sql_string:
               creates a new sql insert statement given a list of db columns,
               and values to input.
            args:
                col_list: list of database table columns to fill
                val_list: list of values to input into each table
                tab_name: name of the table you wish to insert data into
        """
        # removing brackets, making sure comma is not inside of quotations
        column_list = ', '.join(col_list)
        value_list = ', '.join(f"'{value}'" if isinstance(value, str) else repr(value) for value in val_list)

        sql = f'''INSERT INTO {tab_name} ({column_list}) VALUES({value_list});'''

        return sql

    def insert_table_record(self, logger_int, sql):
        """create_table_record:
               general code for the inserting of a new record into any table on database,
               creates connection, and runs sql query. cursor.execute with arg multi, to
               handle multi-query commands.
           args:
               sql: the verbatim sql string, or multi sql query string to send to database
               connection: the connection parameter in the case of specify self.specify_db_connection
               logger: the logger instance of your class self.logger
               sqlite: option for sqlite configuration, as get_cursor()
                          requires database ip, which sqlite does not have
        """
        cursor = self.get_cursor()
        logger_int.info(f'running query: {sql}')
        logger_int.debug(sql)
        try:
            cursor.execute(sql)
        except Exception as e:
            print(f"Exception thrown while processing sql: {sql}\n{e}\n", flush=True)
            logger_int.error(traceback.format_exc())
        try:
            self.commit()

        except Exception as e:
            logger_int.error(f"sql debug: {e}")
            sys.exit("terminating script")

        cursor.close()

    def create_batch_record(self, start_time: datetime, end_time: datetime,
                            batch_size: int, batch_md5: str):
        """create_timestamps:
                uses starting and ending timestamps to create window for sql database purge,
                adds 10 second buffer on either end to allow sql queries to populate.
                appends each timestamp record in picturae_batch table.
            args:
                start_time: starting time stamp
                end_time: ending time stamp
        """

        end_time = end_time

        delt_time = timedelta(seconds=15)

        time_stamp_list = [start_time - delt_time, end_time + delt_time]

        column_list = ["batch_MD5",
                       "TimestampCreated",
                       "TimestampModified",
                       "StartTimeStamp",
                       "EndTimeStamp",
                       "batch_size"
                       ]
        value_list = [f"{batch_md5}",
                      f"{time_utils.get_pst_time_now_string()}",
                      f"{time_utils.get_pst_time_now_string()}",
                      f"{time_stamp_list[0]}",
                      f"{time_stamp_list[1]}",
                      f"{batch_size}"
                      ]

        value_list, column_list = remove_two_index(value_list, column_list)

        sql = self.create_insert_statement(val_list=value_list, col_list=column_list, tab_name="picturae_batch")

        return sql

    def create_update_statement(self, tab_name: str, col_list: list, val_list: list, condition: str):
        """create_update_string: function used to create sql string used to upload a list of values in the database

            args:
                tab_name: name of table to update
                col_list: list of columns to update
                val_list: list of values with which to update above list of columns(order matters)
                condition: condition sql string used to select sub-sect of records to update.
        """
        update_string = " SET"
        for index, column in enumerate(col_list):
            update_string += " " + f'''{column} = "{val_list[index]}",'''

        update_string = update_string[:-1]

        sql = f'''UPDATE {tab_name}''' + update_string + ' ' + condition

        return sql

    def taxon_unmatch_insert(self, logger,  unmatched_taxa: pd.DataFrame):
        """taxon_unmatch_create: creates sql query for creating new records in taxa unmatch,
                                from rows that did not pass TNRS successfully,
                                either through spelling, or taxonomic errors.
            args:
                unmatched_taxa: a pandas dataframe with unmatched taxa terms filtered by score
        """
        print("uploading unmatched taxa")
        for index, row in unmatched_taxa.iterrows():
            catalognumber = unmatched_taxa.columns.get_loc("CatalogNumber")

            sql = self.create_tnrs_unmatch_tab(row=row, df=unmatched_taxa, tab_name='taxa_unmatch')

            sql_result = self.get_one_match(tab_name='taxa_unmatch',
                                            id_col='CatalogNumber', key_col='CatalogNumber',
                                            match=row[catalognumber], match_type='integer')
            if sql_result is None:
                self.insert_table_record(logger_int=logger, sql=sql)
            else:
                pass

    def create_tnrs_unmatch_tab(self, row, df, tab_name: str):
        """create_unmatch_tab: function used to insert
            unmatched TNRS taxas into the
            taxa_unmatch table on the Database,
            so that a more trained eye can diagnose,
            and resolve some of the edge cases.

        args:
            row: row of unmatched taxon table, through which this function will itterate.
            df: dataframe input in order to get column numbers
            tab_name: name of mysql database table in which to input records.
        """
        columns = df.columns
        fullname = columns.get_loc('fullname')
        name_matched = columns.get_loc('name_matched')
        accepted_author = columns.get_loc('accepted_author')
        overall_score = columns.get_loc('overall_score')
        unmatched_terms = columns.get_loc('unmatched_terms')
        catalog_number = columns.get_loc('CatalogNumber')

        col_list = ["fullname",
                    "TimestampCreated",
                    "TimestampModified",
                    "name_matched",
                    "unmatched_terms",
                    "author",
                    "overall_score",
                    "CatalogNumber"]

        val_list = [f"{row[fullname]}",
                    f"{time_utils.get_pst_time_now_string()}",
                    f"{time_utils.get_pst_time_now_string()}",
                    f"{row[name_matched]}",
                    f"{row[unmatched_terms]}",
                    f"{row[accepted_author]}",
                    f"{row[overall_score]}",
                    f"{row[catalog_number]}"]

        val_list, col_list = remove_two_index(val_list, col_list)

        sql = self.create_insert_statement(tab_name=tab_name, col_list=col_list,
                                           val_list=val_list)

        return sql

    def insert_taxa_added_record(self, taxon_list, logger_int, df: pd.DataFrame):
        """new_taxa_record: creates record level data for any new taxa added to the database,
                            populates useful table for qc and troubleshooting
        args:
            taxon_list: list of new taxa added to taxon tree during upload
            connection: connection instance for this sql, using self.specify_db_connection
            logger_int: the logger instance for this class
            df: pandas dataframe, the record table uploaded to the database in question
            """
        taxa_frame = df[df['fullname'].isin(taxon_list)]
        for index, row in taxa_frame.iterrows():
            catalog_number = taxa_frame.columns.get_loc('CatalogNumber')
            barcode_result = self.get_one_match(tab_name='picturaetaxa_added',
                                                id_col='CatalogNumber',
                                                key_col='CatalogNumber',
                                                match=row[catalog_number],
                                                match_type="integer")
            if barcode_result is None:
                sql = self.create_new_tax_tab(row=row, df=taxa_frame, tab_name='picturaetaxa_added')

                self.insert_table_record(logger_int=logger_int, sql=sql)

    def create_new_tax_tab(self, row, df: pd.DataFrame, tab_name: str):
        """create_new_tax: does a similar function as create_unmatch_tab,
                            but instead uploads a table of taxa newly added
                            to the database for QC monitoring(make sure no wonky taxa are added)
            args:
                row: row of new_taxa dataframe through which function will iterate
                df: new_taxa dataframe in order to get column index numbers
                tab_name: name of new_taxa table on mysql database.
        """
        columns = df.columns
        fullname = columns.get_loc('fullname')
        catalog_number = columns.get_loc('CatalogNumber')
        family = columns.get_loc('Family')
        taxname = columns.get_loc('taxname')
        hybrid = columns.get_loc('Hybrid')

        col_list = ["fullname",
                    "TimestampCreated",
                    "TimestampModified",
                    "CatalogNumber",
                    "family",
                    "name",
                    "Hybrid"]


        val_list = [f"{row[fullname]}",
                    f"{time_utils.get_pst_time_now_string()}",
                    f"{time_utils.get_pst_time_now_string()}",
                    f"{row[catalog_number]}",
                    f"{row[family]}",
                    f"{row[taxname]}",
                       row[hybrid]]

        val_list, col_list = remove_two_index(val_list, col_list)

        sql = self.create_insert_statement(tab_name=tab_name, col_list=col_list,
                                           val_list=val_list)

        return sql

    def generate_token(self, timestamp, filename):
        """Generate the auth token for the given filename and timestamp.
        This is for comparing to the client submited token.
        args:
            timestamp: starting timestamp of upload batch
            file_name: the name of the datafile that was uploaded
        """
        timestamp = str(timestamp)
        if timestamp is None:
            print(f"Missing timestamp; token generation failure.")
        if filename is None:
            print(f"Missing filename, token generation failure.")
        mac = hmac.new(settings.KEY.encode(), timestamp.encode() + filename.encode(), digestmod='md5')
        print(f"Generated new token for {filename} at {timestamp}.")
        return ':'.join((mac.hexdigest(), timestamp))
