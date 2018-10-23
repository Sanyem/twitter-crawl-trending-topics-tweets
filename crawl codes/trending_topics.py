import tweepy
consumer_key = 'uU8wcv2l2MrfB248u7vWxQyzr'
consumer_secret = '2DNgOIgx9wzae76BUX26yYuP5TNHGs1v2KvKofzNWpzsrXkut2'
access_token = '825220709618061312-Uy2877g1iUPbF6vaC56xnFg5WWnfMos'
access_token_secret = 'S21VPpnfDXl8O17mSsyVoMjZLoxoPAbvuCjBLRw6s77wW'
# OAuth process, using the keys and tokens
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    trends1 = api.trends_place(23424977) # from the end of your code
    #23424848 india code
    #23424977 usa code
    # trends1 is a list with only one element in it, which is a 
    # dict which we'll put in data.
    data = trends1[0] 
    # grab the trends
    trends = data['trends']
    # grab the name from each trend
    names = [trend['name'] for trend in trends]
    # put all the names together with a ' ' separating them
    trendsName = ' '.join(names)
    print(trendsName)
except Exception as e:
    print (e)