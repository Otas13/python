# funguje, prihlasi se

import cookielib
import urllib
import urllib2

url = 'https://www.reddit.com/post/login'
values = {'user' : '<login>',
          'passwd' : '<pass>' }

data = urllib.urlencode(values)
cookies = cookielib.CookieJar()

opener = urllib2.build_opener(
    urllib2.HTTPRedirectHandler(),
    urllib2.HTTPHandler(debuglevel=0),
    urllib2.HTTPSHandler(debuglevel=0),
    urllib2.HTTPCookieProcessor(cookies))

response = opener.open(url, data)
the_page = response.read()
http_headers = response.info()

print the_page
