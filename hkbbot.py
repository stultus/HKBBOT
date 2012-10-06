#! /usr/bin/env python
# -*- coding: utf-8 -*-

# hkbbot.py
# Version 1.0
#
# Copyright (C) 2012 - Hrishikesh K B <hrishi.kb@gmail.com>
#
# Licensed under GPL Version 3
 
 
        
#	                 _.-'\          |\-"""-/|          /`-._
#	             _.-`     `.       /         \       ,'     '-._
#	          _.'           `._   ;   \   /   ;   _,'           `._
#	        .'                 `-.:           :.-'                 `.
#	      ,`                           , ,                           '.
#	    ,`                                                             '.
#	   /                             STULTUS                             \
#	  :,-"""-,                      =========                      ,-"""-,:
#	 /'       `                                                   '       '\
#	          :                                                   :
#	          : ,-"""-,                                   ,-"""-, :
#	          /'       `.       _.-'         '-._       .'       '\
#	                     \    .`    :       :    '.    /
#	                      . .`       :     :       '. .
#	                      :/          :   :          \:
#	                      :            : :            :
#	                                    :




import twitter
import time
import os
import sys

# provide the complete path to our fellow bot's directory  
os.chdir('/home/stultus/Desktop/HkbBot')



# Credentials please ... (Check the README file for more details)
api = twitter.Api(consumer_key='CONSUMER KEY HERE',
                  consumer_secret='CONSUMER SECRET HERE',
                  access_token_key='ACCESS TOKEN KEY HERE',
                  access_token_secret='ACCESS TOKEN SECRET HERE')


# the heart of this program --> provide the search querry below
SEARCH ='#foo'




print "----------------------HKBBOT--------------------------------"
print ".......... a twitter retweet bot by Hrishi.................."
print "...........Testing the connection..........................."
print api.VerifyCredentials()
print "----------------------..................--------------------------------"





# I can't rely on my memory. need a place to write down the last tweet I retweeted 
LATESTFILE = 'latest.txt'



# and the Magic Follows... 

while 1:
  if os.path.exists(LATESTFILE):
    fp = open(LATESTFILE)
    lastid = fp.read().strip()
    fp.close()

    if lastid == '':
        lastid = 0
  else:
    lastid = 0
    
  
                  
  
  print "Searching for "+SEARCH
  results = api.GetSearch(SEARCH, since_id=lastid)
  print 'Found %s results.' % (len(results))
  if len(results) == 0:
    print 'Nothing to retweet. Exiting from inner loop.'
    continue
  repliedTo = []
  for statusObj in results:
      if statusObj.user.screen_name=="hkbbot":
        print "naa.. its my tweet only"
        continue
      try:
         print "Trying to post this : RT @"+statusObj.user.screen_name+" "+statusObj.text.lower()
         api.PostUpdates("RT @"+statusObj.user.screen_name+" "+statusObj.text.lower())
         print "I think I posted it successfully"       
         time.sleep(1)      
      except Exception:
            print "Unexpected error:", sys.exc_info()[0:2]

      
  fp = open(LATESTFILE, 'w')
  fp.write(str(max([x.id for x in results])))
  fp.close()
    
  print "Sleeping for 30 seconds...zzz...zzz..zzzzzzz"
  print "---------"
  time.sleep(1*30)
  
  
 
# and dear code.. Please work.. :)  
