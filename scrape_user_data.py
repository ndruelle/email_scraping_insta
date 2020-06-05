from time import sleep
import json
from selenium import webdriver
import re
import random
from igramscraper.instagram import Instagram
import DBusers


with open('settings.json','r') as settings:
    credentials = json.load(settings)
    username_insta = credentials['instagram']['user']
    password_insta = credentials['instagram']['pass']
    hashtags = credentials['config']['hashtags']

def login():

    # fetch webriver path
    chromedriver_path = '/Users/nicolasdruelle/PycharmProjects/email_scraping_insta/chromedriver'
    global webdriver
    webdriver = webdriver.Chrome (chromedriver_path)

    #Open the instagram login page
    webdriver.get ('https://www.instagram.com/accounts/login/?source=auth_switcher')
    #sleep for 3 seconds to prevent issues with the server


    sleep(3)
    #Find username and password fields and set their input using our constants

    username = webdriver.find_element_by_name('username')
    username.send_keys(username_insta)
    password = webdriver.find_element_by_name('password')
    password.send_keys (password_insta)

    #Get the login button
    try:
        button_login = webdriver.find_element_by_xpath (
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
    except:
        button_login = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/button/div')

    #sleep again
    sleep(2)
    #click login
    button_login.click()
    sleep(3)

    saved_password = webdriver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div/section/div/button')

    saved_password.click()

    sleep(1)

    notnow = webdriver.find_element_by_css_selector (
            'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notnow.click ()

def get_username():

    #looping through the list of hastag in setting.json
    for hashtag in hashtags :

        #checking if username has alredy been scraped
        prev_user_list = DBusers.get_username()

        #html request on hastag in list

        webdriver.get ('https://www.instagram.com/explore/tags/' + hashtag + '/')
        sleep (5)

        # Get the first post thumbnail and click on it
        first_thumbnail = webdriver.find_element_by_xpath (
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

        first_thumbnail.click ()


        #define the number of picture to scrape in this range
        for x in range (0,5000):

            sleep(random.randint(3, 5))
            try:
                username = webdriver.find_element_by_xpath ('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]').text
            except:
                username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text


            # if user already exist, click next to move on otherwise log username to db
            if username not in prev_user_list:
                data_scrapped = False
                DBusers.add_username(username,hashtag,data_scrapped)

            webdriver.find_element_by_link_text ('Next').click ()
            sleep (random.randint (2, 4))

def get_data(username_insta, password_insta):

    #get username from db that haven't been scrapped before
    users = DBusers.get_username_to_scrapped

    #Instantiate Instagram class from igramscraper.instagram package
    instagram = Instagram()
    instagram.with_credentials(username_insta, password_insta, 'chache')
    instagram.login()

    for user in users():
        if 'Verified' not in user:
            try:
                account = instagram.get_account(user)
                id = account.identifier
                username = account.username
                full_name = account.full_name
                biography = account.biography
                nbr_followers = account.followed_by_count
                nbr_follows = account.follows_count
                business_address = account.business_address_json
                business_email = account.business_email
                business_phone_number = account.business_phone_number

                inferred_email = ','.join(re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", biography))
                inferred_phone_number = ','.join(re.findall("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", biography))

                DBusers.add_scrapped_data(id,username,full_name,biography,nbr_followers,nbr_follows,business_address,business_email,business_phone_number,inferred_email,inferred_phone_number)
                DBusers.update_user_scrapped(username)
            except:
                continue


#login()
#get_username()
#get_data(username_insta, password_insta)


