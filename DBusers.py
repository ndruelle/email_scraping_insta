import datetime
from DBHandler import *


#add new username
def add_user(username):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO followed_users(username, date_added) VALUES(%s,%s)",(username, now))
    mydb.commit()


def add_user_data(username):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO followed_users(username, date_added) VALUES(%s,%s)",(username, now))
    mydb.commit()