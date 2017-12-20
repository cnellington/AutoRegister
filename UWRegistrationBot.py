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
print("Done")
