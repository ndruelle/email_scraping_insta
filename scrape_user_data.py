from time import sleep
import json
from selenium import webdriver
import random
from igramscraper.instagram import Instagram
import DBusers


with open('settings.json','r') as settings:
    credentials = json.load(settings)
    username_insta = credentials['instagram']['user']
    password_insta = credentials['instagram']['pass']
    hashtags = credentials['config']['hashtags']

'''
data = {'id': [],
            'Username': [],
            'Full name': [],
            'Biography': [],
            'Profile pic url': [],
            'External Url': [],
            'Number of followers': [],
            'Number of follows': [],
            'Is private': [],
            'Is verified': [],
            'Number of published posts': [],
            'Business address': [],
            'Business email': [],
            'Business category': [],
            'Business phone number': [],
            'Joined recently': [],
            'Is Business Account': []
            }
'''

def login():

    # fetch webriver path
    chromedriver_path = '/usr/local/bin/chromedriver'
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
        button_login = webdriver.find_element_by_xpath (
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/button/div')

    #sleep again
    sleep(2)
    #click login
    button_login.click()
    sleep(3)

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
        sleep (random.randint (1, 3))

        #define the number of picture to scrape in this range
        for x in range (0,5):

            try:
                username = webdriver.find_element_by_xpath ('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]').text
            except:
                username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text

            # if user already exist, click next to move on otherwise log username to db
            if username not in prev_user_list:
                data_scrapped = False
                DBusers.add_username(username,hashtag,data_scrapped)
            else:
                continue

            webdriver.find_element_by_link_text ('Next').click ()
            sleep (random.randint (2, 4))

def get_data(username_insta, password_insta):

    #get username from db that haven't been scrapped before
    #users = DBusers.get_username_to_scrapped
    users = ['ndruelle','marie']

    #Instantiate Instagram class from igramscraper.instagram package
    instagram = Instagram()
    instagram.with_credentials(username_insta, password_insta, 'chache')
    instagram.login()

    for user in users:
        account = instagram.get_account(user)
        id = account.identifier
        print (id)

'''
        data['id'].append (account.identifier)
        data['Username'].append (account.username)
        data['Full name'].append (account.full_name)
        data['Biography'].append (account.biography)
        data['Profile pic url'].append (account.profile_pic_url)
        data['External Url'].append (account.external_url)
        data['Number of followers'].append (account.followed_by_count)
        data['Number of follows'].append (account.follows_count)
        data['Is private'].append (account.is_private)
        data['Is verified'].append (account.is_verified)
        data['Number of published posts'].append (account.media_count)
        data['Business address'].append (account.business_address_json)
        data['Business email'].append (account.business_email)
        data['Business category'].append (account.business_category_name)
        data['Business phone number'].append (account.business_phone_number)
        data['Joined recently'].append (account.is_joined_recently)
        data['Is Business Account'].append (account.is_business_account)
'''




#login()
#get_username()
#get_data(username_insta, password_insta)
#df = pd.DataFrame(data)
#print(df)

