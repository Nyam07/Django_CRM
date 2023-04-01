import mysql.connector;

dataBase = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = '37322929',

    use_pure=True
)

#Prepare a cursor object
cursorObject = dataBase.cursor()

#Create a databse 
cursorObject.execute('CREATE DATABASE crmApp')

print("Done")