from time import sleep
import json
from selenium import webdriver
import random
from igramscraper.instagram import Instagram


with open('settings.json','r') as settings:
    credentials = json.load(settings)
    username_insta = credentials['instagram']['user']
    password_insta = credentials['instagram']['pass']
    hashtags = credentials['config']['hashtags']

chromedriver_path = '/usr/local/bin/chromedriver'
webdriver = webdriver.Chrome(chromedriver_path)


def login():
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
        button_login = webdriver.find_element_by_xpath (
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/button/div')

    #sleep again
    sleep(2)
    #click login
    button_login.click()
    sleep(3)

    try:
        notnow = webdriver.find_element_by_css_selector (
            'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notnow.click ()
    except:
        return

def get_username():

    selected_user = []
    print(selected_user)

    for hashtag in hashtags :
        for x in range(0,10):
            webdriver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
            sleep (5)

            # Get the first post thumbnail and click on it
            first_thumbnail = webdriver.find_element_by_xpath (
                '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

            first_thumbnail.click ()
            sleep(random.randint (1, 3))

            try:
                username = webdriver.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]').text

            except:
                username = webdriver.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text

            selected_user.append(username)
    return selected_user


def get_data(username_insta, password_insta, selected_users):
    instagram = Instagram()
    instagram.with_credentials (username_insta, password_insta, 'chache')
    instagram.login ()

    for user in selected_users:
        account = instagram.get_account(user)


login()
get_username()
get_data(username_insta, password_insta)
