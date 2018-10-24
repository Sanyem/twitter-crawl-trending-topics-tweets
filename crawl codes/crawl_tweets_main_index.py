import tweepy
import csv
import pandas as pd
import json
consumer_key = 'uU8wcv2l2MrfB248u7vWxQyzr'
consumer_secret = '2DNgOIgx9wzae76BUX26yYuP5TNHGs1v2KvKofzNWpzsrXkut2'
access_token = '825220709618061312-Uy2877g1iUPbF6vaC56xnFg5WWnfMos'
access_token_secret = 'S21VPpnfDXl8O17mSsyVoMjZLoxoPAbvuCjBLRw6s77wW'
t = open("trends_file.txt","a")
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    trends1 = api.trends_place(23424848) # from the end of your code
    data = trends1[0] 
    trends = data['trends']
    names = [trend['name'] for trend in trends]
    trendsName = ' '.join(names)
    file_num = 1680
    #print(names)
    for trend in names:
        if trend[0] == '#':
            i=1
            print(trend)
            t.write(trend)
            t.write('\n')
            data={}
            for tweet in tweepy.Cursor(api.search,q=trend,
                            lang="en",
                            since="2018-10-24",tweet_mode="extended",truncated="true").items():
                file_name = str(file_num) + '.txt'
                f = open(file_name,"w")
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
                            f.write(json_data)
                            print(file_num)
                            file_num = file_num+1
                            f.close()
                            i = i+1
                if i >= 11:
                    break
    t.close()
except Exception as e:
    print (e)