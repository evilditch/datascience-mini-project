from pysentimiento import EmotionAnalyzer
from pysentimiento.preprocessing import preprocess_tweet
import pandas as pd

# Path to csv file containing tweets. File must have headers 'id', 'location', 'tweet' 
filepath = 'tweets_with_coordinates.csv'

# Read, drop empty lines and duplicates and preprocess the tweets
data = pd.read_csv(filepath, sep=',')
df = pd.DataFrame(data=data)
df = df.dropna(subset=['id', 'location', 'tweet'])
df = df.drop_duplicates()
df['tweet'] = df['tweet'].str.lower()
df['tweet'] = df['tweet'].apply(lambda x: preprocess_tweet(x, lang='en')) # takes care of hashtags etc 

# Predict the sentiment, this might take some time
em_analyzer = EmotionAnalyzer(lang='en')
df["sentiment"] = df.apply(lambda row : em_analyzer.predict(row["tweet"]).probas, axis = 1)

# Make column for each sentimentprobability
def get_sentiment_prob(sent, row):
    dictionary = row['sentiment']
    return dictionary[sent]

def sentiments_to_columns(df):
    sentiments = ['others', 'joy', 'sadness', 'anger', 'surprise', 'disgust', 'fear']
    
    for s in sentiments:
        new_col = []
        for i, row in df.iterrows():    
            new_col.append(get_sentiment_prob(s, row))
        df.insert(0, s, new_col)

    return df

df = sentiments_to_columns(df)

# Save dataframe to a csv file
df.to_csv('tweets_with_coordinations_and_sentiments.csv', sep=',')