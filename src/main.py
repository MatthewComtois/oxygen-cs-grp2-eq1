import datetime
from signalrcore.hub_connection_builder import HubConnectionBuilder
import logging
import requests
import json
import time
from dotenv import load_dotenv
import os
from database import *


load_dotenv() 

class Main:
    def __init__(self):
        self._hub_connection = None
        self.HOST = os.getenv('HOST') if (os.getenv('HOST') != None and os.getenv('HOST')) else "http://34.95.34.5"
        if (os.getenv('TOKEN')!= None and os.getenv('TOKEN')):
            self.TOKEN = os.getenv('TOKEN') 
        else:
            raise Exception("La variable 'Token' doit être définie comme variable d'environnement.")
        self.TICKETS = os.getenv('TICKETS') if (os.getenv('TICKETS') != None and os.getenv('TICKETS')) else "25"
        self.T_MAX = os.getenv('T_MAX') if (os.getenv('T_MAX') != None and os.getenv('HOST')) else "80"
        self.T_MIN = os.getenv('T_MIN') if (os.getenv('T_MIN') != None and os.getenv('T_MIN')) else "60"
        self.DATABASE = os.getenv('database_name') if (os.getenv('database_name') != None and os.getenv('database_name')) else "oxygenCsGrp2Eq1E23Db"
        
        try:
            createDb(self.DATABASE)
            self.mydb = connectToDatabase(self.DATABASE)
            self.mycursor = self.mydb.cursor()
        except requests.exceptions.RequestException as e:
            print(e)

    def __del__(self):
        if self._hub_connection != None:
            self._hub_connection.stop()

    def setup(self):
        self.setSensorHub()

    def start(self):
        self.setup()
        self._hub_connection.start()

        print("Press CTRL+C to exit.")
        while True:
            time.sleep(2)

    def setSensorHub(self):
        self._hub_connection = (
            HubConnectionBuilder()
            .with_url(f"{self.HOST}/SensorHub?token={self.TOKEN}")
            .configure_logging(logging.INFO)
            .with_automatic_reconnect(
                {
                    "type": "raw",
                    "keep_alive_interval": 10,
                    "reconnect_interval": 5,
                    "max_attempts": 999,
                }
            )
            .build()
        )
        self._hub_connection.on("ReceiveSensorData", self.onSensorDataReceived)
        self._hub_connection.on_open(lambda: print("||| Connection opened."))
        self._hub_connection.on_close(lambda: print("||| Connection closed."))
        self._hub_connection.on_error(lambda data: print(f"||| An exception was thrown closed: {data.error}"))

    def onSensorDataReceived(self, data):
        try:
            dateFormat='%Y-%m-%dT%H:%M:%S.%f'
            print(data[0]["date"] + " --> " + data[0]["data"], flush=True)
            date = data[0]["date"]
            convertedDate = datetime.datetime.strptime(date[:25], dateFormat)
            dp = float(data[0]["data"])
            #self.send_temperature_to_fastapi(date, dp)
            self.send_event_to_database(convertedDate, dp)
            self.analyzeDatapoint(date, dp)
        except Exception as err:
            print(err)

    def analyzeDatapoint(self, date, data):
        if float(data) >= float(self.T_MAX):
            self.sendActionToHvac(date, "TurnOnAc", self.TICKETS)
        elif float(data) <= float(self.T_MIN):
            self.sendActionToHvac(date, "TurnOnHeater", self.TICKETS)

    def sendActionToHvac(self, date, action, nbTick):
        r = requests.get(f"{self.HOST}/api/hvac/{self.TOKEN}/{action}/{nbTick}")
        details = json.loads(r.text)
        print(details)

    def send_event_to_database(self, timestamp, event):
        try:
            createSensorDataEntry(self.mydb, self.mycursor, timestamp, event)
        except requests.exceptions.RequestException as e:
            print(e)


if __name__ == "__main__":
    main = Main()
    main.start()
