import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

database_host = (
    os.getenv("database_host")
    if (os.getenv("database_host") is not None and os.getenv("database_host"))
    else "localhost"
)
database_user = (
    os.getenv("database_user")
    if (os.getenv("database_user") is not None and os.getenv("database_user"))
    else "root"
)
database_password = (
    os.getenv("database_password")
    if (os.getenv("database_password") is not None)
    else "root"
)


def connect_to_database(db_name):
    """Connect to the database"""
    mydb = mysql.connector.connect(
        host=database_host,
        user=database_user,
        password=database_password,
        database=db_name,
        port=3306,
    )
    return mydb


def check_if_database_exist(db_name):
    """Check if the database exist"""
    mydb = connect_to_database("")
    mycursor = mydb.cursor()
    mycursor.execute(f"SHOW DATABASES LIKE '{db_name}'")
    return mycursor.fetchone() is not None


def create_db(db_name):
    """Create a database with the db_name"""
    mydb = connect_to_database("")
    mycursor = mydb.cursor()
    if check_if_database_exist(db_name) is False:
        mycursor.execute(f"CREATE DATABASE {db_name}")
        mydb.close()
        mydb = connect_to_database(db_name)
        mycursor = mydb.cursor()
        create_sensor_datas_table(mycursor)
        mydb.close()


def create_sensor_datas_table(mycursor):
    """Create a sensorDatas table in the cursor databas"""
    mycursor.execute(
        "CREATE TABLE sensorDatas (timestamp DATETIME PRIMARY KEY, temperature FLOAT)"
    )


def create_sensor_data_entry(mydb, mycursor, datetime, temperature):
    """Create an entry in the sensorDatas table"""
    datetime_string = datetime.strftime("%Y-%m-%d %H:%M:%S")
    mycursor.execute(
        f"INSERT INTO sensorDatas (timestamp, temperature) VALUES ('{datetime_string}',{temperature})"
    )
    mydb.commit()


# POUR TESTER


def drop_db(db_name):
    """Delete the dabase with the name in db_name"""
    mydb = connect_to_database("")
    mycursor = mydb.cursor()
    if check_if_database_exist(db_name) is True:
        mycursor.execute(f"DROP DATABASE {db_name}")
        mydb.close()


def check_if_table_exist(db_name, table_name):
    """Check if the table exist in the database"""
    mydb = connect_to_database(db_name)
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT '{table_name}' FROM information_schema.tables")
    return mycursor.fetchone() is not None


def check_if_record_exist(db_name, table_name, table_id_name_string, record_id):
    """Check if the record exist in the table"""
    mydb = connect_to_database(db_name)
    mycursor = mydb.cursor()
    sql = f"SELECT * FROM {table_name} WHERE {table_id_name_string} ='{record_id}'"
    mycursor.execute(sql)
    return mycursor.fetchone() is not None
