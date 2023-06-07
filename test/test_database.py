from src.database import *
import datetime

testDbName = "testDb"
sensorDataTableName = "sensorDatas"
sensorDataTablIdName = "timestamp"

def test_createDatabase():
    createDb(testDbName)
    assert checkIfDatabaseExist(testDbName) == True
    dropDb(testDbName)

def test_dropDatabase():
    createDb(testDbName)
    assert checkIfDatabaseExist(testDbName) == True
    dropDb(testDbName)
    assert checkIfDatabaseExist(testDbName) == False


def test_checkIfCreateTableSensorDatas():
    createDb(testDbName)
    assert checkIfDatabaseExist(testDbName) == True
    assert checkIfTableExist(testDbName, sensorDataTableName) == True
    dropDb(testDbName)
    assert checkIfDatabaseExist(testDbName) == False

def test_checkIfCreateRecordSensorDatas():
    datetimeNow = datetime.datetime.now();
    datetimeNowString = datetimeNow.strftime('%Y-%m-%d %H:%M:%S')
    createDb(testDbName)

    mydb = connectToDatabase(testDbName)
    mycursor = mydb.cursor()

    assert checkIfDatabaseExist(testDbName) == True
    assert checkIfTableExist(testDbName, sensorDataTableName) == True
    createSensorDataEntry(mydb, mycursor, datetimeNow, float(12.221))
    assert checkIfRecordExist(testDbName, sensorDataTableName, sensorDataTablIdName, datetimeNowString) == True
    dropDb(testDbName)
    assert checkIfDatabaseExist(testDbName) == False