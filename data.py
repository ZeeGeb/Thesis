import tweepy
import requests
import os
import json
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

consumer_key ="XoPPevTZbChpxJJSgBca2vYNj"
consumer_secret = "79Y9GMQ3QKE9iNAd86GhgIt9Vr9vJ3bb5WUEdmjQgjvLNTbgVQ" 
access_token = "1111663317372809217-2xWducPx9aU28M111XBgf3RQpriBSY"
access_token_secret = "Pob3i7C6DSt2mBAN6mEbzjaffN2Ms4CWD30ocC0cMY8Vi"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)
user = "GebengaZizipho"
# user = api.me()
# print("------------------------------User Information---------------------------------------- \n")
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
    # print(friend.screen_name)

#public_tweets = api.home_timeline()
tweets = api.home_timeline(screen_name=user, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
# print('\n')
# print("------------------------------Tweets in timeline-------------------------------------- \n")

for tweet in tweets:
    tweet.full_text.encode("utf-8")
    media = tweet.entities.get('media', [])
    outtweets = [[tweet.id_str, 
              tweet.created_at, 
              tweet.favorite_count, 
              tweet.retweet_count, 
              tweet.full_text.encode("utf-8").decode("utf-8"),tweet.user.followers_count]
             for idx,tweet in enumerate(tweets)]
    if(len(media) > 0):
            #print(url)
            outtweets.append(media)
    
    df = DataFrame(outtweets,columns=["id","created_at","favorite_count","retweet_count", "text", "followers_count"])
    df.to_csv('%s_tweets8.csv' % user,index=False)
    df.head(3)
    ylabels = ["favorite_count","retweet_count"]

    fig = plt.figure(figsize=(13,3))
    fig.subplots_adjust(hspace=0.01,wspace=0.01)

    n_row = len(ylabels)
    n_col = 1
    for count, ylabel in enumerate(ylabels):
        ax = fig.add_subplot(n_row,n_col,count+1)
        ax.plot(df["created_at"],df[ylabel])
        ax.set_ylabel(ylabel)
    plt.show()
     

# if len(tweets) == 0:
#         break
#oldest_id = tweets[-1].id

# columns = set()
# datatypes = [str, int]
# tweets_data = []

# for tweet in public_tweets:
#     status_dict = dict(vars(tweet))
#     keys = status_dict.keys()
#     single_tweet = {"user": tweet.user.screen_name, "author": tweet.author.screen_name}
#     for k in keys:
#         try:
#             d_type = type(status_dict[k])
#         except:
#             d_type = None 
#         if d_type != None:    
#             if d_type in datatypes:
#                 single_tweet[k] = status_dict[k]
#                 columns.add(k)
#     # print(tweet.text)
#     tweets_data.append(single_tweet)
# header_columns = list(columns)
# #header_columns.append("user")
# #header_columns.append("author")
# df = pd.DataFrame(tweets_data,columns=header_columns)
# print(df.head)

# df.to_csv(r"Desktop\export_dataframe.csv",index=False)