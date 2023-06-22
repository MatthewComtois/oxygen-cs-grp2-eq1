import datetime
import logging
import json
import time
import os
import requests
from dotenv import load_dotenv
from signalrcore.hub_connection_builder import HubConnectionBuilder
from database import *


load_dotenv()


class Main:
    def __init__(self):
        self._hub_connection = None
        self.host = (
            os.getenv("HOST")
            if (os.getenv("HOST") is not None and os.getenv("HOST"))
            else "http://34.95.34.5"
        )
        if os.getenv("TOKEN") is not None and os.getenv("TOKEN"):
            self.token = os.getenv("TOKEN")
        else:
            raise Exception(
                "La variable 'Token' doit être définie comme variable d'environnement."
            )
        self.tickets = (
            os.getenv("TICKETS")
            if (os.getenv("TICKETS") is not None and os.getenv("TICKETS"))
            else "25"
        )
        self.t_max = (
            os.getenv("T_MAX")
            if (os.getenv("T_MAX") is not None and os.getenv("HOST"))
            else "80"
        )
        self.t_min = (
            os.getenv("T_MIN")
            if (os.getenv("T_MIN") is not None and os.getenv("T_MIN"))
            else "60"
        )
        self.database = (
            os.getenv("database_name")
            if (os.getenv("database_name") is not None and os.getenv("database_name"))
            else "oxygenCsGrp2Eq1E23Db"
        )

        try:
            create_db(self.database)
            self.mydb = connect_to_database(self.database)
            self.mycursor = self.mydb.cursor()
        except requests.exceptions.RequestException as err:
            print(err)

    def __del__(self):
        """Delete connection"""
        if self._hub_connection is not None:
            self._hub_connection.stop()

    def setup(self):
        """Setup hub sensor"""
        self.set_sensor_hub()

    def start(self):
        """Start hub connection"""
        self.setup()
        self._hub_connection.start()

        print("Press CTRL+C to exit.")
        while True:
            time.sleep(2)

    def set_sensor_hub(self):
        """Set sensor hub"""
        self._hub_connection = (
            HubConnectionBuilder()
            .with_url(f"{self.host}/SensorHub?token={self.token}")
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
        self._hub_connection.on("ReceiveSensorData", self.on_sensor_data_received)
        self._hub_connection.on_open(lambda: print("||| Connection opened."))
        self._hub_connection.on_close(lambda: print("||| Connection closed."))
        self._hub_connection.on_error(
            lambda data: print(f"||| An exception was thrown closed: {data.error}")
        )

    def on_sensor_data_received(self, data):
        """Handle received data"""
        try:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            print(data[0]["date"] + " --> " + data[0]["data"], flush=True)
            date = data[0]["date"]
            converted_date = datetime.datetime.strptime(date[:25], date_format)
            datapoint = float(data[0]["data"])
            # self.send_temperature_to_fastapi(date, dp)
            self.send_event_to_database(converted_date, datapoint)
            self.analyze_datapoint(date, datapoint)
        except Exception as err:
            print(err)

    def analyze_datapoint(self, date, data):
        """Analyze data"""
        if float(data) >= float(self.t_max):
            self.send_action_to_hvac(date, "TurnOnAc", self.tickets)
        elif float(data) <= float(self.t_min):
            self.send_action_to_hvac(date, "TurnOnHeater", self.tickets)

    def send_action_to_hvac(self, date, action, nb_tick):
        """Send data to hvac"""
        request = requests.get(f"{self.host}/api/hvac/{self.token}/{action}/{nb_tick}")
        details = json.loads(request.text)
        print(details)

    def send_event_to_database(self, timestamp, event):
        """Send data to database"""
        try:
            create_sensor_data_entry(self.mydb, self.mycursor, timestamp, event)
        except requests.exceptions.RequestException as err:
            print(err)


if __name__ == "__main__":
    main = Main()
    main.start()
