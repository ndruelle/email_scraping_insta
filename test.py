from igramscraper.instagram import Instagram
import json

instagram = Instagram()
#proxies = {'http': 'http://123.45.67.8:1087','https': 'http://123.45.67.8:1087'}

#instagram.set_proxies(proxies)
instagram.with_credentials('nicolas.druelle@ieseg.fr','rsk7b9252594','chache')
instagram.login()

selected_users = ['kauflokal','nicolas_drll']

data = {'id':[],
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

for user in selected_users:
    account = instagram.get_account(user)
    data['id'].append(account.identifier)
    data['Username'].append(account.username)
    data['Full name'].append(account.full_name)
    data['Biography'].append(account.biography)
    data['Profile pic url'].append(account.profile_pic_url)
    data['External Url'].append(account.external_url)
    data['Number of followers'].append (account.followed_by_count)
    data['Number of follows'].append(account.follows_count)
    data['Is private'].append (account.is_private)
    data['Is verified'].append (account.is_verified)
    data['Number of published posts'].append (account.media_count)
    data['Business address'].append(account.business_address_json)
    data['Business email'].append (account.business_email)
    data['Business category'].append (account.business_category_name)
    data['Business phone number'].append (account.business_phone_number)
    data['Joined recently'].append(account.is_joined_recently)
    data['Is Business Account'].append(account.is_business_account)






print(data)

