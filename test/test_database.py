from src.database import *
from src.utils import *
import datetime

testDbName = "testDb"
sensorDataTableName = "sensorDatas"
sensorDataTablIdName = "timestamp"
database_host = get_env_var("database_host", "localhost", False)
database_user = get_env_var("database_user", "root", False)
database_password = get_env_var("database_password", "", True)
my_sql_db = MysqlDatabase(database_host, database_user, database_password)


def test_createDatabase():
    my_sql_db.create_db(testDbName)
    assert my_sql_db.check_if_database_exist(testDbName) == True
    my_sql_db.drop_db(testDbName)


def test_dropDatabase():
    my_sql_db.create_db(testDbName)
    assert my_sql_db.check_if_database_exist(testDbName) == True
    my_sql_db.drop_db(testDbName)
    assert my_sql_db.check_if_database_exist(testDbName) == False


def test_checkIfCreateTableSensorDatas():
    my_sql_db.create_db(testDbName)
    assert my_sql_db.check_if_database_exist(testDbName) == True
    assert my_sql_db.check_if_table_exist(testDbName, sensorDataTableName) == True
    my_sql_db.drop_db(testDbName)
    assert my_sql_db.check_if_database_exist(testDbName) == False


def test_checkIfCreateRecordSensorDatas():
    datetimeNow = datetime.datetime.now()
    datetimeNowString = datetimeNow.strftime("%Y-%m-%d %H:%M:%S")
    my_sql_db.create_db(testDbName)

    mydb = my_sql_db.connect_to_database(testDbName)
    mycursor = mydb.cursor()

    assert my_sql_db.check_if_database_exist(testDbName) == True
    assert my_sql_db.check_if_table_exist(testDbName, sensorDataTableName) == True
    my_sql_db.create_sensor_data_entry(mydb, mycursor, datetimeNow, float(12.221))
    assert (
        my_sql_db.check_if_record_exist(
            testDbName, sensorDataTableName, sensorDataTablIdName, datetimeNowString
        )
        == True
    )
    my_sql_db.drop_db(testDbName)
    assert my_sql_db.check_if_database_exist(testDbName) == False
