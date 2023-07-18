import mysql.connector


class MysqlDatabase:
    """Class qui permet de se connecter et intéragir avec une BD Mysql"""

    def __init__(self, database_host, database_user, database_password):
        """class MysqlDatabase constructor"""
        self.database_host = database_host
        self.database_user = database_user
        self.database_password = database_password

    def connect_to_database(self, db_name):
        """Connect to the database"""
        mydb = mysql.connector.connect(
            host=self.database_host,
            user=self.database_user,
            password=self.database_password,
            database=db_name,
            port=3306,
        )
        return mydb

    def check_if_database_exist(self, db_name):
        """Check if the database exist"""
        mydb = self.connect_to_database("")
        mycursor = mydb.cursor()
        mycursor.execute(f"SHOW DATABASES LIKE '{db_name}'")
        return mycursor.fetchone() is not None

    def create_db(self, db_name):
        """Create a database with the db_name"""
        mydb = self.connect_to_database("")
        mycursor = mydb.cursor()
        if self.check_if_database_exist(db_name) is False:
            mycursor.execute(f"CREATE DATABASE {db_name}")
            mydb.close()
            mydb = self.connect_to_database(db_name)
            mycursor = mydb.cursor()
            self.create_sensor_datas_table(mycursor)
            self.create_sensor_actions_table(mycursor)
            mydb.close()

    def create_sensor_datas_table(self, mycursor):
        """Create a sensorDatas table in the cursor databas"""
        mycursor.execute(
            "CREATE TABLE sensorDatas (timestamp DATETIME PRIMARY KEY, temperature FLOAT)"
        )

    def create_sensor_data_entry(self, mydb, mycursor, datetime, temperature):
        """Create an entry in the sensorDatas table"""
        datetime_string = datetime.strftime("%Y-%m-%d %H:%M:%S")
        mycursor.execute(
            f"INSERT INTO sensorDatas (timestamp, temperature) VALUES ('{datetime_string}',{temperature})"
        )
        mydb.commit()

    def create_sensor_actions_table(self, mycursor):
        """Create a sensorActions table in the cursor databas"""
        mycursor.execute(
            "CREATE TABLE sensorActions (timestamp DATETIME PRIMARY KEY, action TEXT)"
        )

    def create_sensor_actions_entry(self, mydb, mycursor, datetime, action):
        """Create an entry in the sensorActions table"""
        datetime_string = datetime.strftime("%Y-%m-%d %H:%M:%S")
        mycursor.execute(
            f"INSERT INTO sensorActions (timestamp, action) VALUES ('{datetime_string}','{action}')"
        )
        mydb.commit()

    # POUR TESTER

    def drop_db(self, db_name):
        """Delete the dabase with the name in db_name"""
        mydb = self.connect_to_database("")
        mycursor = mydb.cursor()
        if self.check_if_database_exist(db_name) is True:
            mycursor.execute(f"DROP DATABASE {db_name}")
            mydb.close()

    def check_if_table_exist(self, db_name, table_name):
        """Check if the table exist in the database"""
        mydb = self.connect_to_database(db_name)
        mycursor = mydb.cursor()
        mycursor.execute(
            f"SELECT * FROM information_schema.tables WHERE table_name = '{table_name}'"
        )
        return mycursor.fetchone() is not None

    def check_if_record_exist(
        self, db_name, table_name, table_id_name_string, record_id
    ):
        """Check if the record exist in the table"""
        mydb = self.connect_to_database(db_name)
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM {table_name} WHERE {table_id_name_string} ='{record_id}'"
        mycursor.execute(sql)
        return mycursor.fetchone() is not None
