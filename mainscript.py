import csv
import tweepy
import pandas as pd

consumer_key = "*Enter the details*"
consumer_secret = "*Enter the details*"
access_token = "*Enter the details*"
access_secret = "*Enter the details*"
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
 
# update these for whatever tweet you want to process replies to
# the template is twitter.com/name/status/target_tweet_id
# this can be found using the link of the tweet

name = "*Enter the @ of the account*"
target_tweet_id = "*Enter tweet id*"
 
replies=[]
for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(1000):
   if hasattr(tweet, 'in_reply_to_status_id_str'):
       if (tweet.in_reply_to_status_id_str==target_tweet_id):
           replies.append(tweet)
 
# update these for whatever tweet you want to process replies to
tweet_pd = pd.DataFrame(replies)

def tweetstoDataFrame(tweets):
 
   DataSet = pd.DataFrame()
 
   DataSet['tweetID'] = [tweet.id for tweet in tweets]
   DataSet['tweetText'] = [tweet.text for tweet in tweets]
   
   return DataSet
 
#Pass the tweets list to the above function to create a DataFrame
DataSet = tweetstoDataFrame(replies)

#Export the dataset to csv
DataSet.to_csv('tweets.csv')

print('Done')

