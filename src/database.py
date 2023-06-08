import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

database_host = os.getenv('database_host') if (os.getenv('database_host') != None and os.getenv('database_host')) else "mydb"
database_user = os.getenv('database_user') if (os.getenv('database_user') != None and os.getenv('database_user')) else "root"
database_password = os.getenv('database_password') if (os.getenv('database_password') != None) else "root"



def connectToDatabase(dbName):
    mydb = mysql.connector.connect(
        host=database_host,
        user=database_user,
        password=database_password,
        database=dbName,
        port=3306
    )
    return mydb;

def checkIfDatabaseExist(dbName):
    mydb = connectToDatabase("")
    mycursor = mydb.cursor()
    mycursor.execute(f"SHOW DATABASES LIKE '{dbName}'")
    return mycursor.fetchone() != None;

def createDb(dbName):
    mydb = connectToDatabase("")
    mycursor = mydb.cursor()
    if(checkIfDatabaseExist(dbName) == False):
        mycursor.execute(f"CREATE DATABASE {dbName}")
        mydb.close()
        mydb = connectToDatabase(dbName)
        mycursor = mydb.cursor()
        createSensorDatasTable(mycursor)

def createSensorDatasTable(mycursor):
    mycursor.execute("CREATE TABLE sensorDatas (timestamp DATETIME PRIMARY KEY, temperature FLOAT)")

def createSensorDataEntry(mydb, mycursor, datetime, temperature):
    datetimeString = datetime.strftime('%Y-%m-%d %H:%M:%S')
    mycursor.execute(f"INSERT INTO sensorDatas (timestamp, temperature) VALUES ('{datetimeString}',{temperature})")
    mydb.commit()


#POUR TESTER

def dropDb(dbName):
    mydb = connectToDatabase("")
    mycursor = mydb.cursor()
    if(checkIfDatabaseExist(dbName) == True):
        mycursor.execute(f"DROP DATABASE {dbName}")
        mydb.close()

def checkIfTableExist(tableName):
    mydb = connectToDatabase("")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT '{tableName}' FROM information_schema.tables")
    return mycursor.fetchone() != None;

def checkIfTableExist(dbName, tableName):
    mydb = connectToDatabase(dbName)
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT '{tableName}' FROM information_schema.tables")
    return mycursor.fetchone() != None;

def checkIfRecordExist(dbName, tableName, tableIdNameString, recordId):
    mydb = connectToDatabase(dbName)
    mycursor = mydb.cursor()
    sql = f"SELECT * FROM {tableName} WHERE {tableIdNameString} ='{recordId}'"
    mycursor.execute(sql)
    return mycursor.fetchone() != None