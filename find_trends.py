import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import re
import scipy

#time it takes to run script
from datetime import datetime
startTime = datetime.now()
#import matplotlib.pyplot as plt

#Read CSV file of Election Day Tweets
tweets_data = pd.read_csv('../TweetViz/election_day_tweets_small.csv', sep=',')

#print the first 5 entires    (5 rows x 34 cols)
#print(tweets_data.head())
#print num of tweets   397629
#count = len(tweets_data)
#create dataframe for wanted tweet attributes
tweets_list = pd.DataFrame()
        #add text
        #for i in tweets_data.values:
        #    tweets['text'] = map(lambda tweet: tweet, i)

        #tweets['text'] = map(lambda tweet: tweet[0], tweets_data.values)
        #creates a list of all text from tweets
tweets_list = map(lambda tweet: tweet[0], tweets_data.values)
hashtags_unsorted = []
#filters hashtags from tweets_list,
for x in tweets_list:
    match = re.findall(r"#(\w+)", x)
    if match: hashtags_unsorted.append(match)   # ignores tweets without hashtags

#converts list back to DataFrame for col mapping
hashtags_unsorted = pd.DataFrame(hashtags_unsorted, dtype='a')

#concatenate all hashtag cols into one for groupby
hashtags_sorted = hashtags_unsorted[0]
for i in hashtags_unsorted.columns:
    hashtags_sorted = hashtags_sorted.append(hashtags_unsorted[i]).reset_index(drop=True)

#drop all rows with value NaN, None
#hashtags_sorted = hashtags_sorted.dropna(how='any')

#hastags_sorted is a pandas Series
#map with groupBy to get hashtag occurences
#print hashtags_sorted.groupby([0]).size().reset_index(name='count')
hashtags_sorted = hashtags_sorted.str.lower()

grouped = hashtags_sorted.groupby(hashtags_sorted).size().reset_index(name='count')

#remove any hashtags lower than 1000 mentions (1000 because anyless is uninterseting) (anything )
hashtags = grouped[grouped['count'] >= 1000]
#sort most > least
hashtags = hashtags.sort_values(['index','count'], ascending=[True,False])
#output hashtags with most occurrences
print hashtags
    #['hashtag', 1234]
    #['hashtag', 'hashtagabc', 452]
    #['hashtag', 'hashtagabc','ha', 1] =>
        #['hashtag', 'hashtagabc', i+1],
        #['hashtag', 'ha', i+1],
        #['hashtagabc', 'ha', i+1]

#have an array list that keeps track of hashtag count
#have an array that keeps track of hashtag pairs

#create dataset for hashtags [hashtag, count]

#run relational/distance algorithm to find similarity between hashtags

#visualize/suggest hashtags

### sort into hashtag groups (#donaldtrump #trump #trump2016 #makeamericagreatagain #hillaryclinton #hillary #hillary2016 #imwithher #drumpf #crookedhillary #nastywoman #strongertogether)
    ## hashtags [hashtag, count]

    ## use only most used hashtags
    ## do k-means on hashtags to find distance from one another
### keep track of relational hashtags (mentioned in one tweet together)
### Use


#output time to run script
print datetime.now() - startTime
