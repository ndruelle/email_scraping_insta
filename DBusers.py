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
    cursor.execute("SELECT username FROM followed_users WHERE data_scrapped = 0 ")
    users = [x for item in cursor.fetchall () for x in item]
    return users


def add_scrapped_data(id, username, full_name, biography, nbr_followers, nbr_follows, business_address, business_email, business_phone_number, inferred_email, inferred_phone_number):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO scrapped_username(id, username, full_name, biography, nbr_followers, nbr_follows, business_address, business_email, business_phone_number, inferred_email, inferred_phone_number, date_scrapped) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id, username, full_name, biography, nbr_followers, nbr_follows, business_address, business_email, business_phone_number, inferred_email, inferred_phone_number , now))
    mydb.commit()

def update_user_scrapped(username):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    #when username is scrapped set value to 1 to not scrap it again
    cursor.execute("UPDATE followed_users SET data_scrapped = %s WHERE username = %s",(1,username))
    mydb.commit()
