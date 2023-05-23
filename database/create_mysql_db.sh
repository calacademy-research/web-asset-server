port=3306
database_file=botany.sql
database=casbotany
docker container stop mysql-specify; docker container rm mysql-specify
sudo rm -rf ./sql-db-store
mkdir ./sql-db-store
docker  run   -v sql-db-store:/var/lib/mysql -e MYSQL_ROOT_HOST=% -e MYSQL_ROOT_PASSWORD=password1 --publish $port:3306 --name=mysql-specify -d mysql/mysql-server:5.7.34
cat startup.sql | mysql -h 127.0.0.1 -u root --password=password1 -P $port
# note, if the file is gzipped then 'gzcat' is useful here
cat $database_file | mysql -h 127.0.0.1 -u root --password=password1 -P $port $database
#cat $database_file | mysql -h 127.0.0.1 -u root --password=password1 -P $port
