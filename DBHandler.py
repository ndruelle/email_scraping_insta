import mysql.connector
import json

with open ('settings.json', 'r') as json_file:
    settings = json.load (json_file)
    host = settings['db']['host']
    user = settings['db']['user']
    dbname = settings['db']['database']
    password = settings['db']['pass']
    auth_plugin = settings['db']['auth_plugin']

class DBHandler:
    def __init__(self):
        self.host = host
        self.user = user
        self.dbname = dbname
        self.password = password
        self.auth_plugin = auth_plugin


    @staticmethod
    def get_mydb():
        db = DBHandler()
        mydb = db.connect()
        return mydb


    def connect(self):
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database = dbname,
            auth_plugin=auth_plugin
        )
        return mydb
