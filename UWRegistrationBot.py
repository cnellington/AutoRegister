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

class SessionUW:
    def __init__(self, url_login, url_auth, login, pwd):
        self.ses = requests.session()
        login_html = self.ses.get(url_login)
        soup_login = BeautifulSoup(login_html.content, "html.parser").find('form').find_all('input')
        my_dict = {}
        for u in soup_login:
            if u.has_attr('value'):
                my_dict[u['name']] = u['value']
        # override the inputs without login and pwd:
        my_dict['Email'] = login
        my_dict['Passwd'] = pwd
        self.ses.post(url_auth, data=my_dict)

    def get(self, URL):
        return self.ses.get(URL).text

def checkSeats(varCourse):

    url = varCourse
    uwResp = urlopen(url)
    uwPage = uwResp.read().decode('utf-8')
    print(uwPage)

# course = "https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=WIN+2018&SLN=11245"
url_login = "https://weblogin.washington.edu/"
url_auth = "https://weblogin.washington.edu/"
url = genURL("WIN", "2018", "12238")
webbrowser.open_new(url)
# url_auth = "https://sdb.admin.uw.edu/Shibboleth.sso/SAML2/POST"
# url_login = "https://accounts.google.com/ServiceLogin"
# url_auth = "https://accounts.google.com/ServiceLoginAuth"
# session = SessionUW(url_login, url_auth, input("UW NET ID: "), input("PASSWORD: "))
# print(session.get("https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=WIN+2018&SLN=13013"))
# webbrowser.open_new('https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=WIN+2018&SLN=13013')
# # checkSeats(course)

# uwnetid = input('UW NET ID: ')
# uwpass = input('PASSWORD: ')
# # Cookie / Opener holder
# cj = CookieJar()
# opener = build_opener(HTTPCookieProcessor(cj))

# # Login Header
# opener.addheaders = [('User-agent', 'UW-Login')]

# # Install opener
# install_opener(opener)

# # Form POST URL
# postURL = "https://weblogin.washington.edu/"

# # First request form data
# formData = {
#     'weblogin_netid': uwnetid,
#     'weblogin_password': uwpass,
#     'execution': 'e1s1',
#     '_eventId': 'submit',
#     'lt': 'xxxxxx',
#     'submit': 'Continue >'
# }

# # Encode form data
# data = urlencode(formData).encode('UTF-8')

# # First request object
# req = Request(postURL, data)

# # Submit request and read data
# resp = urlopen(req)
# respRead = resp.read().decode('utf-8')
# print(respRead)
