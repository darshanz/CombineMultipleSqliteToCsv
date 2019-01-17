import sqlite3
import csv
import os
import sys, getopt

def convert_sqlite_to_csv(inputFolder, ext, tableName):
    """ inputFolder - Folder where sqlite files are located. 
        ext - Extension of your sqlite file (eg. db, sqlite, sqlite3 etc.)
        tableName - table name from which you want to select the data.
    """
    csvWriter = csv.writer(open(inputFolder+'/output.csv', 'w', newline=''))
    for file1 in os.listdir(inputFolder):
        if file1.endswith('.'+ext):
            conn = sqlite3.connect(inputFolder+'/'+file1)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM "+tableName)
            rows = cursor.fetchall()
            for row in rows:
                csvWriter.writerow(row)
            continue
        else:
            continue
 
def main(argv):
	inputFolder = ''
	extension = ''
	tableName = ''
	
	try:
		opts, args = getopt.getopt(argv, "hf:e:t:" ,["inputFolder=","extension=", "tableName="])
	except getopt.GetoptError:
		print('multiple_sqlite_files_tocsv.py -d <inputFolder> -e <extension> -t <tableName>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('multiple_sqlite_files_tocsv.py -f <inputFolder> -e <extension> -t <tableName>')
			sys.exit()
		elif opt in ("-f", "--inputFolder"):
			inputFolder = arg
		elif opt in ("-e", "--extension"):
			extension = arg
		elif opt in ("-t", "--tableName"):
			tableName = arg

	if(len(inputFolder) == 0):
		print("Please enter inputFolder")
		print('multiple_sqlite_files_tocsv.py -d <inputFolder> -e <extension> -t <tableName>')
	elif(len(extension) == 0):
		print("Please enter extension")
		print('multiple_sqlite_files_tocsv.py -d <inputFolder> -e <extension> -t <tableName>')
	elif(len(tableName) == 0):
		print("Please enter tableName")
		print('multiple_sqlite_files_tocsv.py -d <inputFolder> -e <extension> -t <tableName>')
	else:
		convert_sqlite_to_csv(inputFolder, extension, tableName)
    
   
if __name__ == "__main__":
   main(sys.argv[1:])