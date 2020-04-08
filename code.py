# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:33:29 2020

@author: Ziyad Meftah
"""

import nasty
import pandas as pd 
from datetime import datetime


f=[["Tweet_id","Text","User_id","date_published", "tweet url","keyword","language"]]

c= ["#Merkelrede","#Bundeskanzlerin","#Merkel","#angelamerkel","#ansprache"]



tweet_stream = nasty.Search(c[4],since=datetime(2020, 3, 18), until=datetime(2020, 4, 8),lang="de", max_tweets= 400).request()
for tweet in tweet_stream:
    f.append([tweet.id,tweet.text,tweet.user.id, tweet.created_at.strftime("%m/%d/%Y"),tweet.url,c[4], "DE"])
    
tweet_stream = nasty.Search(c[4],since=datetime(2020, 3, 18),until=datetime(2020, 4, 8),lang="en", max_tweets= 400).request()
for tweet in tweet_stream:
    f.append([tweet.id,tweet.text,tweet.user.id, tweet.created_at.strftime("%m/%d/%Y"),tweet.url,c[4],"EN"])
    


df = pd.DataFrame(f[1:], columns=f[0])
df=df.drop_duplicates()

df['date_published']=df.astype('str')
df.to_csv('merkel.csv')