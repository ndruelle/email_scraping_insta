from igramscraper.instagram import Instagram

instagram = Instagram()
#proxies = {'http': 'http://123.45.67.8:1087','https': 'http://123.45.67.8:1087'}

#instagram.set_proxies(proxies)
instagram.with_credentials('nicolas.druelle@ieseg.fr','rsk7b9252594','chache')
instagram.login()


#medias = instagram.get_medias_by_tag('kauflokal', count=20)

account = instagram.get_account('kauflokal')
print(account)