import datetime
from DBHandler import *


#add new username
def add_username(username,hashtag,data_scrapped):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO followed_users(username, hashtag, data_scrapped, date_added) VALUES(%s,%s,%s,%s)",(username, hashtag, data_scrapped, now))
    mydb.commit()

def get_username():
    mydb = DBHandler.get_mydb ()
    cursor = mydb.cursor ()
    cursor.execute ("SELECT username FROM followed_users")
    users = [x for item in cursor.fetchall() for x in item]
    return users

def get_username_to_scrapped():
    mydb = DBHandler.get_mydb ()
    cursor = mydb.cursor ()
    # think about adding  in order in order to scrap only new username
    cursor.execute("SELECT username FROM followed_users WHERE data_scrapped IS NOT TRUE ")
    users = [x for item in cursor.fetchall () for x in item]
    return users


def add_username_data(username):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO followed_users(username, date_added) VALUES(%s,%s)",(username, now))
    mydb.commit()

