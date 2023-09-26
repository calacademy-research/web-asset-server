"""contains sql functions for inserting into, pulling from, and creating sqlite tables"""
import sqlite3

def table_sql_list():
    """table_sql_list: creates list of sql DDL commands to run in sqlite DB"""

    sql_bot_list = ['''CREATE TABLE IF NOT EXISTS collectionobject (
                        CollectionObjectID INTEGER PRIMARY KEY,
                        TimestampCreated TEXT NOT NULL,
                        TimestampModified TEXT DEFAULT NULL,
                        Version INTEGER DEFAULT NULL,
                        CollectionMemberID INTEGER NOT NULL,
                        AltCatalogNumber TEXT DEFAULT NULL,
                        Availability TEXT DEFAULT NULL,
                        CatalogNumber TEXT DEFAULT NULL,
                        CatalogedDate TEXT DEFAULT NULL,
                        CatalogedDatePrecision INTEGER DEFAULT NULL,
                        CatalogedDateVerbatim TEXT DEFAULT NULL,
                        CountAmt INTEGER DEFAULT NULL,
                        Deaccessioned INTEGER DEFAULT NULL,
                        Description TEXT,
                        FieldNumber TEXT DEFAULT NULL,
                        GUID TEXT DEFAULT NULL,
                        InventoryDate TEXT DEFAULT NULL,
                        Modifier TEXT DEFAULT NULL,
                        Name TEXT DEFAULT NULL,
                        Notifications TEXT DEFAULT NULL,
                        Number1 REAL DEFAULT NULL,
                        Number2 REAL DEFAULT NULL,
                        ObjectCondition TEXT DEFAULT NULL,
                        ProjectNumber TEXT DEFAULT NULL,
                        Remarks TEXT,
                        Restrictions TEXT DEFAULT NULL,
                        Text1 TEXT,
                        Text2 TEXT,
                        TotalValue REAL DEFAULT NULL,
                        OCR TEXT,
                        Visibility INTEGER DEFAULT NULL,
                        YesNo1 INTEGER DEFAULT NULL,
                        YesNo2 INTEGER DEFAULT NULL,
                        YesNo3 INTEGER DEFAULT NULL,
                        YesNo4 INTEGER DEFAULT NULL,
                        YesNo5 INTEGER DEFAULT NULL,
                        YesNo6 INTEGER DEFAULT NULL,
                        CollectionID INTEGER NOT NULL,
                        CollectingEventID INTEGER DEFAULT NULL,
                        ContainerID INTEGER DEFAULT NULL,
                        FieldNotebookPageID INTEGER DEFAULT NULL,
                        PaleoContextID INTEGER DEFAULT NULL,
                        CreatedByAgentID INTEGER DEFAULT NULL,
                        AccessionID INTEGER DEFAULT NULL,
                        ContainerOwnerID INTEGER DEFAULT NULL,
                        CollectionObjectAttributeID INTEGER DEFAULT NULL,
                        AppraisalID INTEGER DEFAULT NULL,
                        ModifiedByAgentID INTEGER DEFAULT NULL,
                        VisibilitySetByID INTEGER DEFAULT NULL,
                        CatalogerID INTEGER DEFAULT NULL,
                        SGRStatus INTEGER DEFAULT NULL,
                        ReservedText TEXT DEFAULT NULL,
                        Text3 TEXT,
                        Integer1 INTEGER DEFAULT NULL,
                        Integer2 INTEGER DEFAULT NULL,
                        ReservedInteger3 INTEGER DEFAULT NULL,
                        ReservedInteger4 INTEGER DEFAULT NULL,
                        ReservedText2 TEXT DEFAULT NULL,
                        ReservedText3 TEXT DEFAULT NULL,
                        InventorizedByID INTEGER DEFAULT NULL,
                        Date1 TEXT DEFAULT NULL,
                        Date1Precision INTEGER DEFAULT NULL,
                        InventoryDatePrecision INTEGER DEFAULT NULL,
                        Agent1ID INTEGER DEFAULT NULL,
                        NumberOfDuplicates INTEGER DEFAULT NULL,
                        EmbargoReason TEXT,
                        EmbargoReleaseDate TEXT DEFAULT NULL,
                        EmbargoReleaseDatePrecision INTEGER DEFAULT NULL,
                        EmbargoStartDate TEXT DEFAULT NULL,
                        EmbargoStartDatePrecision INTEGER DEFAULT NULL,
                        Text4 TEXT,
                        Text5 TEXT,
                        Text6 TEXT,
                        Text7 TEXT,
                        Text8 TEXT,
                        UniqueIdentifier TEXT DEFAULT NULL,
                        EmbargoAuthorityID INTEGER DEFAULT NULL,
                        CONSTRAINT FK_AccessionID FOREIGN KEY (AccessionID) REFERENCES accession (AccessionID),
                        CONSTRAINT FK_CatalogerID FOREIGN KEY (CatalogerID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_ModifiedByAgentID FOREIGN KEY (ModifiedByAgentID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_FieldNotebookPageID FOREIGN KEY (FieldNotebookPageID) REFERENCES fieldnotebookpage (FieldNotebookPageID),
                        CONSTRAINT FK_CreatedByAgentID FOREIGN KEY (CreatedByAgentID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_VisibilitySetByID FOREIGN KEY (VisibilitySetByID) REFERENCES specifyuser (SpecifyUserID),
                        CONSTRAINT FK_CollectionID FOREIGN KEY (CollectionID) REFERENCES collection (UserGroupScopeId),
                        CONSTRAINT FK_PaleoContextID FOREIGN KEY (PaleoContextID) REFERENCES paleocontext (PaleoContextID),
                        CONSTRAINT FK_InventorizedByID FOREIGN KEY (InventorizedByID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_CollectionObjectAttributeID FOREIGN KEY (CollectionObjectAttributeID) REFERENCES collectionobjectattribute (CollectionObjectAttributeID),
                        CONSTRAINT FK_ContainerOwnerID FOREIGN KEY (ContainerOwnerID) REFERENCES container (ContainerID),
                        CONSTRAINT FK_AppraisalID FOREIGN KEY (AppraisalID) REFERENCES appraisal (AppraisalID),
                        CONSTRAINT FK_CollectingEventID FOREIGN KEY (CollectingEventID) REFERENCES collectingevent (CollectingEventID),
                        CONSTRAINT FK_Agent1ID FOREIGN KEY (Agent1ID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_EmbargoAuthorityID FOREIGN KEY (EmbargoAuthorityID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_ContainerID FOREIGN KEY (ContainerID) REFERENCES container (ContainerID)
                    );''',
                    '''CREATE TABLE IF NOT EXISTS agent (
                        AgentID INTEGER PRIMARY KEY AUTOINCREMENT,
                        TimestampCreated TEXT NOT NULL,
                        TimestampModified TEXT DEFAULT NULL,
                        Version INTEGER DEFAULT NULL,
                        Abbreviation VARCHAR(50) DEFAULT NULL,
                        AgentType INTEGER NOT NULL,
                        DateOfBirth DATE DEFAULT NULL,
                        DateOfBirthPrecision INTEGER DEFAULT NULL,
                        DateOfDeath DATE DEFAULT NULL,
                        DateOfDeathPrecision INTEGER DEFAULT NULL,
                        DateType INTEGER DEFAULT NULL,
                        Email VARCHAR(50) DEFAULT NULL,
                        FirstName VARCHAR(50) DEFAULT NULL,
                        GUID VARCHAR(128) DEFAULT NULL,
                        Initials VARCHAR(8) DEFAULT NULL,
                        Interests VARCHAR(255) DEFAULT NULL,
                        JobTitle VARCHAR(50) DEFAULT NULL,
                        LastName VARCHAR(256) DEFAULT NULL,
                        MiddleInitial VARCHAR(50) DEFAULT NULL,
                        Remarks TEXT,
                        Title VARCHAR(50) DEFAULT NULL,
                        URL TEXT,
                        ParentOrganizationID INTEGER DEFAULT NULL,
                        InstitutionTCID INTEGER DEFAULT NULL,
                        CreatedByAgentID INTEGER DEFAULT NULL,
                        CollectionTCID INTEGER DEFAULT NULL,
                        CollectionCCID INTEGER DEFAULT NULL,
                        ModifiedByAgentID INTEGER DEFAULT NULL,
                        InstitutionCCID INTEGER DEFAULT NULL,
                        SpecifyUserID INTEGER DEFAULT NULL,
                        DivisionID INTEGER DEFAULT NULL,
                        Suffix VARCHAR(50) DEFAULT NULL,
                        Date1 DATE DEFAULT NULL,
                        Date1Precision INTEGER DEFAULT NULL,
                        Date2 DATE DEFAULT NULL,
                        Date2Precision INTEGER DEFAULT NULL,
                        Integer1 INTEGER DEFAULT NULL,
                        Integer2 INTEGER DEFAULT NULL,
                        Text1 TEXT,
                        Text2 TEXT,
                        VerbatimDate1 VARCHAR(128) DEFAULT NULL,
                        VerbatimDate2 VARCHAR(128) DEFAULT NULL,
                        Text3 TEXT,
                        Text4 TEXT,
                        Text5 TEXT,
                        CONSTRAINT FK_ParentOrganizationID FOREIGN KEY (ParentOrganizationID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_InstitutionTCID FOREIGN KEY (InstitutionTCID) REFERENCES institutionnetwork (InstitutionNetworkID),
                        CONSTRAINT FK_CreatedByAgentID FOREIGN KEY (CreatedByAgentID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_CollectionTCID FOREIGN KEY (CollectionTCID) REFERENCES collection (UserGroupScopeId),
                        CONSTRAINT FK_CollectionCCID FOREIGN KEY (CollectionCCID) REFERENCES collection (UserGroupScopeId),
                        CONSTRAINT FK_ModifiedByAgentID FOREIGN KEY (ModifiedByAgentID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_InstitutionCCID FOREIGN KEY (InstitutionCCID) REFERENCES institution (UserGroupScopeId),
                        CONSTRAINT FK_SpecifyUserID FOREIGN KEY (SpecifyUserID) REFERENCES specifyuser (SpecifyUserID),
                        CONSTRAINT FK_DivisionID FOREIGN KEY (DivisionID) REFERENCES division (UserGroupScopeId)
                    );
                    ''',
                    '''CREATE TABLE IF NOT EXISTS collectingevent (
                        CollectingEventID INTEGER PRIMARY KEY AUTOINCREMENT,
                        TimestampCreated TEXT NOT NULL,
                        TimestampModified TEXT DEFAULT NULL,
                        Version INTEGER DEFAULT NULL,
                        EndDate DATE DEFAULT NULL,
                        EndDatePrecision INTEGER DEFAULT NULL,
                        EndDateVerbatim VARCHAR(50) DEFAULT NULL,
                        EndTime SMALLINT DEFAULT NULL,
                        Method VARCHAR(50) DEFAULT NULL,
                        Remarks TEXT,
                        StartDate DATE DEFAULT NULL,
                        StartDatePrecision INTEGER DEFAULT NULL,
                        StartDateVerbatim VARCHAR(50) DEFAULT NULL,
                        StartTime SMALLINT DEFAULT NULL,
                        StationFieldNumber VARCHAR(50) DEFAULT NULL,
                        VerbatimDate VARCHAR(50) DEFAULT NULL,
                        VerbatimLocality TEXT,
                        Visibility INTEGER DEFAULT NULL,
                        ModifiedByAgentID INTEGER DEFAULT NULL,
                        LocalityID INTEGER DEFAULT NULL,
                        CreatedByAgentID INTEGER DEFAULT NULL,
                        DisciplineID INTEGER NOT NULL,
                        VisibilitySetByID INTEGER DEFAULT NULL,
                        CollectingTripID INTEGER DEFAULT NULL,
                        CollectingEventAttributeID INTEGER DEFAULT NULL,
                        SGRStatus INTEGER DEFAULT NULL,
                        GUID VARCHAR(128) DEFAULT NULL,
                        Integer1 INTEGER DEFAULT NULL,
                        Integer2 INTEGER DEFAULT NULL,
                        ReservedInteger3 INTEGER DEFAULT NULL,
                        ReservedInteger4 INTEGER DEFAULT NULL,
                        ReservedText1 VARCHAR(128) DEFAULT NULL,
                        ReservedText2 VARCHAR(128) DEFAULT NULL,
                        Text1 TEXT,
                        Text2 TEXT,
                        PaleoContextID INTEGER DEFAULT NULL,
                        StationFieldNumberModifier1 VARCHAR(50) DEFAULT NULL,
                        StationFieldNumberModifier2 VARCHAR(50) DEFAULT NULL,
                        StationFieldNumberModifier3 VARCHAR(50) DEFAULT NULL,
                        Text3 TEXT,
                        Text4 TEXT,
                        Text5 TEXT,
                        Text6 TEXT,
                        Text7 TEXT,
                        Text8 TEXT,
                        UniqueIdentifier VARCHAR(128) DEFAULT NULL,
                        CONSTRAINT FK_LocalityID FOREIGN KEY (LocalityID) REFERENCES locality (LocalityID),
                        CONSTRAINT FK_CollectingEventAttributeID FOREIGN KEY (CollectingEventAttributeID) REFERENCES collectingeventattribute (CollectingEventAttributeID),
                        CONSTRAINT FK_DisciplineID FOREIGN KEY (DisciplineID) REFERENCES discipline (UserGroupScopeId),
                        CONSTRAINT FK_CreatedByAgentID FOREIGN KEY (CreatedByAgentID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_ModifiedByAgentID FOREIGN KEY (ModifiedByAgentID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_VisibilitySetByID FOREIGN KEY (VisibilitySetByID) REFERENCES specifyuser (SpecifyUserID),
                        CONSTRAINT FK_CollectingTripID FOREIGN KEY (CollectingTripID) REFERENCES collectingtrip (CollectingTripID),
                        CONSTRAINT FK_PaleoContextID FOREIGN KEY (PaleoContextID) REFERENCES paleocontext (PaleoContextID)
                    );
                    ''',
                    '''CREATE TABLE IF NOT EXISTS locality (
                        LocalityID INTEGER PRIMARY KEY AUTOINCREMENT,
                        TimestampCreated TEXT NOT NULL,
                        TimestampModified TEXT DEFAULT NULL,
                        Version INTEGER DEFAULT NULL,
                        Datum VARCHAR(50) DEFAULT NULL,
                        ElevationAccuracy REAL DEFAULT NULL,
                        ElevationMethod VARCHAR(50) DEFAULT NULL,
                        GML TEXT,
                        GUID VARCHAR(128) DEFAULT NULL,
                        Lat1Text VARCHAR(50) DEFAULT NULL,
                        Lat2Text VARCHAR(50) DEFAULT NULL,
                        LatLongAccuracy REAL DEFAULT NULL,
                        LatLongMethod VARCHAR(50) DEFAULT NULL,
                        LatLongType VARCHAR(50) DEFAULT NULL,
                        Latitude1 REAL DEFAULT NULL,
                        Latitude2 REAL DEFAULT NULL,
                        LocalityName VARCHAR(1024) NOT NULL,
                        Long1Text VARCHAR(50) DEFAULT NULL,
                        Long2Text VARCHAR(50) DEFAULT NULL,
                        Longitude1 REAL DEFAULT NULL,
                        Longitude2 REAL DEFAULT NULL,
                        MaxElevation REAL DEFAULT NULL,
                        MinElevation REAL DEFAULT NULL,
                        NamedPlace VARCHAR(255) DEFAULT NULL,
                        OriginalElevationUnit VARCHAR(50) DEFAULT NULL,
                        OriginalLatLongUnit INTEGER DEFAULT NULL,
                        RelationToNamedPlace VARCHAR(120) DEFAULT NULL,
                        Remarks TEXT,
                        ShortName VARCHAR(32) DEFAULT NULL,
                        SrcLatLongUnit INTEGER NOT NULL,
                        Text1 TEXT,
                        Text2 TEXT,
                        VerbatimElevation VARCHAR(50) DEFAULT NULL,
                        Visibility INTEGER DEFAULT NULL,
                        DisciplineID INTEGER NOT NULL,
                        GeographyID INTEGER DEFAULT NULL,
                        ModifiedByAgentID INTEGER DEFAULT NULL,
                        CreatedByAgentID INTEGER DEFAULT NULL,
                        VisibilitySetByID INTEGER DEFAULT NULL,
                        SGRStatus INTEGER DEFAULT NULL,
                        Text3 TEXT,
                        Text4 TEXT,
                        Text5 TEXT,
                        VerbatimLatitude VARCHAR(50) DEFAULT NULL,
                        VerbatimLongitude VARCHAR(50) DEFAULT NULL,
                        PaleoContextID INTEGER DEFAULT NULL,
                        YesNo1 INTEGER DEFAULT NULL,
                        YesNo2 INTEGER DEFAULT NULL,
                        YesNo3 INTEGER DEFAULT NULL,
                        YesNo4 INTEGER DEFAULT NULL,
                        YesNo5 INTEGER DEFAULT NULL,
                        UniqueIdentifier VARCHAR(128) DEFAULT NULL,
                        CONSTRAINT FK_DisciplineID FOREIGN KEY (DisciplineID) REFERENCES discipline (UserGroupScopeId),
                        CONSTRAINT FK_ModifiedByAgentID FOREIGN KEY (ModifiedByAgentID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_CreatedByAgentID FOREIGN KEY (CreatedByAgentID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_VisibilitySetByID FOREIGN KEY (VisibilitySetByID) REFERENCES specifyuser (SpecifyUserID),
                        CONSTRAINT FK_PaleoContextID FOREIGN KEY (PaleoContextID) REFERENCES paleocontext (PaleoContextID),
                        CONSTRAINT FK_GeographyID FOREIGN KEY (GeographyID) REFERENCES geography (GeographyID)
                    );
                    ''',
                    '''CREATE TABLE IF NOT EXISTS taxon (
                        TaxonID INTEGER PRIMARY KEY AUTOINCREMENT,
                        TimestampCreated TEXT NOT NULL,
                        TimestampModified TEXT DEFAULT NULL,
                        Version INTEGER DEFAULT NULL,
                        Author VARCHAR(128) DEFAULT NULL,
                        CitesStatus VARCHAR(32) DEFAULT NULL,
                        COLStatus VARCHAR(32) DEFAULT NULL,
                        CommonName VARCHAR(128) DEFAULT NULL,
                        CultivarName VARCHAR(32) DEFAULT NULL,
                        EnvironmentalProtectionStatus VARCHAR(64) DEFAULT NULL,
                        EsaStatus VARCHAR(64) DEFAULT NULL,
                        FullName VARCHAR(512) DEFAULT NULL,
                        GroupNumber VARCHAR(20) DEFAULT NULL,
                        GUID VARCHAR(128) DEFAULT NULL,
                        HighestChildNodeNumber INTEGER DEFAULT NULL,
                        IsAccepted INTEGER DEFAULT NULL,
                        IsHybrid INTEGER DEFAULT NULL,
                        IsisNumber VARCHAR(16) DEFAULT NULL,
                        LabelFormat VARCHAR(64) DEFAULT NULL,
                        Name VARCHAR(256) NOT NULL,
                        NcbiTaxonNumber VARCHAR(8) DEFAULT NULL,
                        NodeNumber INTEGER DEFAULT NULL,
                        Number1 INTEGER DEFAULT NULL,
                        Number2 INTEGER DEFAULT NULL,
                        RankID INTEGER NOT NULL,
                        Remarks TEXT,
                        Source VARCHAR(64) DEFAULT NULL,
                        TaxonomicSerialNumber VARCHAR(50) DEFAULT NULL,
                        Text1 VARCHAR(32) DEFAULT NULL,
                        Text2 VARCHAR(32) DEFAULT NULL,
                        UnitInd1 VARCHAR(50) DEFAULT NULL,
                        UnitInd2 VARCHAR(50) DEFAULT NULL,
                        UnitInd3 VARCHAR(50) DEFAULT NULL,
                        UnitInd4 VARCHAR(50) DEFAULT NULL,
                        UnitName1 VARCHAR(50) DEFAULT NULL,
                        UnitName2 VARCHAR(50) DEFAULT NULL,
                        UnitName3 VARCHAR(50) DEFAULT NULL,
                        UnitName4 VARCHAR(50) DEFAULT NULL,
                        UsfwsCode VARCHAR(16) DEFAULT NULL,
                        Visibility INTEGER DEFAULT NULL,
                        AcceptedID INTEGER DEFAULT NULL,
                        TaxonTreeDefID INTEGER NOT NULL,
                        ParentID INTEGER DEFAULT NULL,
                        HybridParent1ID INTEGER DEFAULT NULL,
                        ModifiedByAgentID INTEGER DEFAULT NULL,
                        CreatedByAgentID INTEGER DEFAULT NULL,
                        VisibilitySetByID INTEGER DEFAULT NULL,
                        TaxonTreeDefItemID INTEGER NOT NULL,
                        HybridParent2ID INTEGER DEFAULT NULL,
                        Number3 REAL DEFAULT NULL,
                        Number4 REAL DEFAULT NULL,
                        Number5 REAL DEFAULT NULL,
                        Text3 TEXT,
                        Text4 TEXT,
                        Text5 TEXT,
                        YesNo1 INTEGER DEFAULT NULL,
                        YesNo2 INTEGER DEFAULT NULL,
                        YesNo3 INTEGER DEFAULT NULL,
                        Integer1 INTEGER DEFAULT NULL,
                        Integer2 INTEGER DEFAULT NULL,
                        Integer3 INTEGER DEFAULT NULL,
                        Integer4 INTEGER DEFAULT NULL,
                        Integer5 INTEGER DEFAULT NULL,
                        Text10 VARCHAR(128) DEFAULT NULL,
                        Text11 VARCHAR(128) DEFAULT NULL,
                        Text12 VARCHAR(128) DEFAULT NULL,
                        Text13 VARCHAR(128) DEFAULT NULL,
                        Text14 VARCHAR(256) DEFAULT NULL,
                        Text15 VARCHAR(256) DEFAULT NULL,
                        Text16 VARCHAR(256) DEFAULT NULL,
                        Text17 VARCHAR(256) DEFAULT NULL,
                        Text18 VARCHAR(256) DEFAULT NULL,
                        Text19 VARCHAR(256) DEFAULT NULL,
                        Text20 VARCHAR(256) DEFAULT NULL,
                        Text6 TEXT,
                        Text7 TEXT,
                        Text8 TEXT,
                        Text9 TEXT,
                        YesNo10 INTEGER DEFAULT NULL,
                        YesNo11 INTEGER DEFAULT NULL,
                        YesNo12 INTEGER DEFAULT NULL,
                        YesNo13 INTEGER DEFAULT NULL,
                        YesNo14 INTEGER DEFAULT NULL,
                        YesNo15 INTEGER DEFAULT NULL,
                        YesNo16 INTEGER DEFAULT NULL,
                        YesNo17 INTEGER DEFAULT NULL,
                        YesNo18 INTEGER DEFAULT NULL,
                        YesNo19 INTEGER DEFAULT NULL,
                        YesNo4 INTEGER DEFAULT NULL,
                        YesNo5 INTEGER DEFAULT NULL,
                        YesNo6 INTEGER DEFAULT NULL,
                        YesNo7 INTEGER DEFAULT NULL,
                        YesNo8 INTEGER DEFAULT NULL,
                        YesNo9 INTEGER DEFAULT NULL,
                        LSID TEXT,
                        TaxonAttributeID INTEGER DEFAULT NULL,
                        CONSTRAINT FK_AcceptedID FOREIGN KEY (AcceptedID) REFERENCES taxon (TaxonID),
                        CONSTRAINT FK_ModifiedByAgentID FOREIGN KEY (ModifiedByAgentID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_HybridParent1ID FOREIGN KEY (HybridParent1ID) REFERENCES taxon (TaxonID),
                        CONSTRAINT FK_HybridParent2ID FOREIGN KEY (HybridParent2ID) REFERENCES taxon (TaxonID),
                        CONSTRAINT FK_CreatedByAgentID FOREIGN KEY (CreatedByAgentID) REFERENCES agent (AgentID),
                        CONSTRAINT FK_VisibilitySetByID FOREIGN KEY (VisibilitySetByID) REFERENCES specifyuser (SpecifyUserID),
                        CONSTRAINT FK_TaxonAttributeID FOREIGN KEY (TaxonAttributeID) REFERENCES taxonattribute (TaxonAttributeID),
                        CONSTRAINT FK_TaxonTreeDefItemID FOREIGN KEY (TaxonTreeDefItemID) REFERENCES taxontreedefitem (TaxonTreeDefItemID),
                        CONSTRAINT FK_ParentID FOREIGN KEY (ParentID) REFERENCES taxon (TaxonID),
                        CONSTRAINT FK_TaxonTreeDefID FOREIGN KEY (TaxonTreeDefID) REFERENCES taxontreedef (TaxonTreeDefID)
                        );''']

    return sql_bot_list


def casbotany_lite_creator():
    """casbotqny_lite_creator: casbotany_lite_creator: creates the
                  sqllite tables contained in the sqllite DDL list"""
    connect = sqlite3.connect('tests/casbotany_lite.db')
    sql_list = table_sql_list()
    curs = connect.cursor()
    # running a loop through tables for sql_lite
    for table in sql_list:
        curs.execute(table)
        connect.commit()

    # closing connection
    curs.close()
    connect.close()


def sql_lite_connection(db_name):
    """sql_lite_connection: creates the connection for sqllite db,
        used as the "connection" parameter in other functions
        args:
            db_name: db_name is the file path to the sqlite db."""
    connection = sqlite3.connect(db_name)
    return connection


def sql_lite_insert(sql, connection, logger_int):
    """sql_lite_insert: facsimile to insert_table_record in sql_csv_utils.py
        args:
            sql: sql string to send to database
            connection: the sqlite connection used to insert data
            logger_int: the instance of logger to use for error reporting
    """
    curs = connection.cursor()
    try:
        curs.execute(sql)
    except Exception as e:
        logger_int.error(f"Exception thrown while processing sql: {sql}\n{e}\n")
    try:
        connection.commit()

    except Exception as e:
        raise ValueError(f"sql debug: {e}")

    curs.close()
    connection.close()


def casbotany_lite_getrecord(id_col, tab_name, key_col, match, match_type="string"):
    """modified get one record function for sql lite

       args:
            tab_name: the name of the table to select
            id_col: the name of the column in which the unique id is stored
            key_col: column on which to match values
            match: value with which to match key_col
            match_type: "string" or "integer", optional with default as "string"
                        puts quotes around sql terms or not depending on data type """

    sql = ""
    if match_type == "string":
        sql = f'''SELECT {id_col} FROM {tab_name} WHERE `{key_col}` = "{match}";'''
    elif match_type == "integer":
        sql = f'''SELECT {id_col} FROM {tab_name} WHERE `{key_col}` = {match};'''

    connection = sqlite3.connect(database="../tests/casbotany_lite.db")
    curs = connection.cursor()
    # running sql query
    curs.execute(sql)
    record = curs.fetchone()
    # closing connection
    curs.close()
    connection.close()
    if record is not None:
        return record[0]
    else:
        return record



