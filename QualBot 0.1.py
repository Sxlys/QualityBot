# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:20:55 2018

@author: USER
"""

#!/usr/bin/python
import praw
import pdb
import re
import os
import requests
import json





#reddit = praw.Reddit(
#                     client_id='DqmvlWPBNaULDA',
 #                    client_secret='K8TAhY46GEzdD7h3vI5OADhl7oA',
 #                    password='3pkAero!',
 #                    user_agent='Quality Bot 0.1',
 #                    username='QualBot',)
# Create the Reddit instance 
# and login
#class User:
##        self.url = https://www.reddit.com/message/mentions.json.format(self.username)
 #       self.post_data = request.get(self.url, headers={'user agent': 'Chrome'})

user1 = User('QualBot') 
    

def bot_login():
    print("Logging in")
    reddit = praw.Reddit('Bot1')
    if (reddit.user.me()) == 'QualBot':
        print('Connection Succesfull...')
        r = 1
    else:
        print('Login Failed...')
        r = 0


        
        
def run_bot(r):
	for mention in r.inbox.mentions(new):
		print("found a mention")
        parse(['data']['children']['data'].max(['created_utc']['body'(reddit.user")]),r.inbox.mentions())
        reddit.user get_comments(limit=none)
        parse(['data']['0']['data']['score', len('selftext')])
       if not os.path.isfile("posts_replied_to.txt"):
           posts_replied_to = []


        
r = bot_login()

while r == 1:
    run_bot(r)
    
    
# Old way i thought of searching for comments.
#subreddit = r.subreddit("All")

#for comment in subreddit.stream.comments():
#    print(comment.body)
 #   if re.search("Marvin Help", comment.body, re.IGNORECASE):
  #          marvin_reply = "Marvin the Depressed Robot says: "
   #         comment.reply(marvin_reply)
    #        print(marvin_reply)
			