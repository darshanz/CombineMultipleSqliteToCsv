Combine multiple sqlite files to single csv file.

python script:

***python multiple_sqlite_files_tocsv.py -d <inputFolder> -e <extension> -t <tableName>***


Notebook:

convert_sqlite_to_csv(inputFolder, ext, tableName)

**inputFolder**  - Folder where sqlite files are located. 

**ext** - Extension of your sqlite file (eg. db, sqlite, sqlite3 etc.)

**tableName** - table name from which you want to select the data.