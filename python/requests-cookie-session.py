#!/usr/bin/env python3

import requests

# If you need to keep track of cookies between requests, easier to use a 'session'
# acts exactly like normal requests, just passes cookies between requests:
s = requests.session()

#cookie: asdf:qwer
s.get('http://httpbin.org/cookies/set/asdf/qwer')

#cookie: asdf:qwer, qwer:zxcv
s.get('http://httpbin.org/cookies/set/qwer/zxcv')

#should print both cookies
print(s.get('http://httpbin.org/cookies').text)