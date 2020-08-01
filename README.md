# db_importer

Database importer class for a school project.

## REQUIREMENT
pymysql

## FILES
db_helper: Db connection using pymysql
Populate_routine: The file to execute, configure the db connection, call the importer script
pop_NAME: The file to edit, here you write your import script, see importer/pop_NAME files for examples
data/: JSON, text ... data to import

## USAGE
populate_rountine.py -host HOST -user USER -db DBNAME -passwd PASSWORD -port PORT -importer IMPORTER_SCRIPT
