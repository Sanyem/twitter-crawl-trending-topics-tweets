import tweepy
import csv
import pandas as pd
import json
####input your credentials here
consumer_key = 'uU8wcv2l2MrfB248u7vWxQyzr'
consumer_secret = '2DNgOIgx9wzae76BUX26yYuP5TNHGs1v2KvKofzNWpzsrXkut2'
access_token = '825220709618061312-Uy2877g1iUPbF6vaC56xnFg5WWnfMos'
access_token_secret = 'S21VPpnfDXl8O17mSsyVoMjZLoxoPAbvuCjBLRw6s77wW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
#csvFile = open('ua.csv', 'a')
#Use csv Writer
#csvWriter = csv.writer(csvFile)
data={}
for tweet in tweepy.Cursor(api.search,q="#MeToo",
                           lang="en",
                           since="2018-10-01",tweet_mode="extended",truncated="true").items(1):
    if tweet.in_reply_to_status_id is None:
        if 'retweeted_status' in dir(tweet):
            if tweet.retweeted is False:
                data['created_at'] = str(tweet.created_at)
                data['id'] = tweet.id
                data['text'] = tweet.retweeted_status.full_text
                data['source'] = tweet.source
                data['user_id'] = tweet.user.id
                data['name'] = tweet.user.name
                data['screen_name'] = tweet.user.screen_name
                data['followers_count'] = tweet.user.followers_count
                data['friends_count'] = tweet.user.friends_count
                data['listed_count'] = tweet.user.listed_count
                data['favourites_count'] = tweet.user.favourites_count
                data['statuses_count'] = tweet.user.statuses_count
                data['description'] = tweet.user.description
                data['verified'] = tweet.user.verified
                json_data = json.dumps(data)
                print(json_data)





        # print(tweet.created_at)
        # print(tweet.id)
        #print(tweet.full_text)
        #print(tweet.text)
        # if 'retweeted_status' in dir(tweet):
        #     print(tweet.retweeted_status.full_text)
        # else:
        #     print(tweet.full_text)
        # print(tweet.source)
        # print(tweet.user.id)
        # print(tweet.user.name)
        # print(tweet.user.screen_name)
        # print(tweet.user.followers_count)
        # print(tweet.user.friends_count)
        # print(tweet.user.listed_count)
        # print(tweet.user.favourites_count)
        # print(tweet.user.statuses_count)
        # print(tweet.user.description)
        # print(tweet.user.verified)
        # print(tweet.retweeted)
        # print(tweet.truncated)
        #print(api.get_status(tweet.id_str, tweet_mode='extended')._json['full_text'])
        #print(tweet.quote_count)
        #print(tweet.reply_count)
        #print(tweet.retweet_count)
        #print(tweet.favourite_count)
        # print(tweet.entities.hashtags)
        # print(tweet.entities.urls)
        # print(tweet.entities.user_mentions)

#    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])