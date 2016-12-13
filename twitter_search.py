# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

import config
# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

oauth = OAuth(config.ACCESS_TOKEN, config.ACCESS_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

# Search for latest tweets about "#nlproc"
latest = twitter.search.tweets(q='#imwithher')

print json.dumps(latest, indent=4)


# Get a list of followers of a particular user
#followers = twitter.followers.ids(screen_name="chensusays")

#print json.dumps(followers, indent=4)


# Get a particular user's timeline (up to 3,200 of his/her most recent tweets)
#recent_tweets = twitter.statuses.user_timeline(screen_name="chensusays")
#print json.dumps(recent_tweets, indent=4)
