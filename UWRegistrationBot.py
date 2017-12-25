try:
    from http.cookiejar import CookieJar
except ImportError:
    from cookielib import CookieJar

try:
    input = raw_input
except NameError:
    pass

try:
    from urllib.request import HTTPCookieProcessor, build_opener, install_opener, Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import HTTPCookieProcessor, build_opener, install_opener, Request, urlopen
    from urllib import urlencode

import re
import time
import webbrowser
from random import randrange
from bs4 import BeautifulSoup
import requests
import datetime

def genURL(quarter, year, SLN):
    return "https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR="+quarter+"+"+year+"&SLN="+SLN

# course = "https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=WIN+2018&SLN=11245"
# url_login = "https://weblogin.washington.edu/"
# url_auth = "https://weblogin.washington.edu/"
# url = genURL("WIN", "2018", "12238")

# # url_auth = "https://sdb.admin.uw.edu/Shibboleth.sso/SAML2/POST"
# # url_login = "https://accounts.google.com/ServiceLogin"
# # url_auth = "https://accounts.google.com/ServiceLoginAuth"
# session = Session(url_login, url_auth, input("UW NET ID: "), input("PASSWORD: "))
# print(session.get(url))
# print(session.get("https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=WIN+2018&SLN=13013"))
# webbrowser.open_new('https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=WIN+2018&SLN=13013')
# # checkSeats(course)

login = input('UW NET ID: ')
pwd = input('PASSWORD: ')
# Cookie / Opener holder
cj = CookieJar()
opener = build_opener(HTTPCookieProcessor(cj))

# Login Header
opener.addheaders = [('User-agent', 'UW-Login')]

# Install opener
install_opener(opener)

# Form POST URL
url = "https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=WIN+2018&SLN=13013"
post_url = "https://weblogin.washington.edu/"
class_url = "https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=WIN+2018&SLN=13013"

# First request form data
formData = {
    'user': login,
    'pass': pwd,
    'execution': 'e1s1',
    '_eventId': 'submit',
    'lt': 'xxxxxx',
    'submit': 'Continue >'
}

# Encode form data
data = urlencode(formData).encode('UTF-8')

ses = requests.session()
login_url = ses.get(url)
post_url = login_url.url
# print(url_login.url)
# jsession = url_login.url[71:71+38-6]
# print(jsession)
soup_login = BeautifulSoup(login_url.content, "html.parser").find('form').find_all('input')
my_dict = {}
for u in soup_login:
    if u.has_attr('value'):
        my_dict[u['name']] = u['value']
# override the inputs without login and pwd:
my_dict['j_username'] = login
my_dict['j_password'] = pwd
# my_dict['j_username'] = jsession
print(my_dict)
ses.post(post_url, data=my_dict)
print(ses.get(url).text)
print(ses.get(class_url).url)


# # First request object
# req = Request(url, data)

# # Submit request and read data
# resp = urlopen(req)
# respRead = resp.read().decode('utf-8')
# print(respRead)
