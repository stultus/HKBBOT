HKBBOT v1.0
==============
A twitter bot written in python. which searchs for a particular keyword 
and retweets it


SETUP
----------
* Install the dependencies:

  SimpleJson
    http://cheeseshop.python.org/pypi/simplejson

  SimpleGeo's OAuth2
    http://github.com/simplegeo/python-oauth2 or
    http://pypi.python.org/pypi/oauth2

  HTTPLib2 (installed along with oauth2 if you use setuptools)
    http://code.google.com/p/httplib2/

 Python-twitter library from:
  http://code.google.com/p/python-twitter/
  

* Create a twitter account
* Go to https://dev.twitter.com/apps/new and log in
* Supply the necessary required fields, accept the TOS, and solve the CAPTCHA.
* Submit the form
* Copy the consumer key (API key) and consumer secret from the screen into hkbbot.py
* Ensure that your application is configured correctly with the permission level (read-write-with-direct messages/read-write)
* On the application's detail page, invoke the "Your access token" feature to automatically negotiate the access token at the permission level you need.
* Copy the indicated access token and access token secret from the screen into hkbbot.py
* change the search text by providing it to the SEARCH variable



RUN
---------
$ python hkbbot.py



