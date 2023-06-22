from src.database import *
import datetime

testDbName = "testDb"
sensorDataTableName = "sensorDatas"
sensorDataTablIdName = "timestamp"


def test_createDatabase():
    create_db(testDbName)
    assert check_if_database_exist(testDbName) == True
    drop_db(testDbName)


def test_dropDatabase():
    create_db(testDbName)
    assert check_if_database_exist(testDbName) == True
    drop_db(testDbName)
    assert check_if_database_exist(testDbName) == False


def test_checkIfCreateTableSensorDatas():
    create_db(testDbName)
    assert check_if_database_exist(testDbName) == True
    assert check_if_table_exist(testDbName, sensorDataTableName) == True
    drop_db(testDbName)
    assert check_if_database_exist(testDbName) == False


def test_checkIfCreateRecordSensorDatas():
    datetimeNow = datetime.datetime.now()
    datetimeNowString = datetimeNow.strftime("%Y-%m-%d %H:%M:%S")
    create_db(testDbName)

    mydb = connect_to_database(testDbName)
    mycursor = mydb.cursor()

    assert check_if_database_exist(testDbName) == True
    assert check_if_table_exist(testDbName, sensorDataTableName) == True
    create_sensor_data_entry(mydb, mycursor, datetimeNow, float(12.221))
    assert (
        check_if_record_exist(
            testDbName, sensorDataTableName, sensorDataTablIdName, datetimeNowString
        )
        == True
    )
    drop_db(testDbName)
    assert check_if_database_exist(testDbName) == False
