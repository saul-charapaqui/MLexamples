from textblob import TextBlob
import tweepy
import time
#Using Twitter API and TextBlob to analyze emotions in some tweets
#We need to use SCV to label in a database. CHALLENGE
'''
wiki = TextBlob("Everyone has come extremely depressed to class ")

print(wiki.tags)

print(wiki.sentiment.polarity)
'''
consumer_key = 'DPkTK4jOK5CyujPq6St7rMkQS'
consumer_secret = 'tJqGqwWi4s47FwspchH2Q5izMdNyawDh4FcbH9fDITnlfSmrJV'

access_token = '1018371226811682816-AWTNkamDXWO61ZIlsxbg47yB0jLZwg'
access_token_secret = 'kDOXog87m3uyZ38cpQkESt4N1wwBFOkISJCiQHayNEDHm'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth) #create, delete, find tweets

public_tweets = api.search('religion')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	time.sleep(2)
