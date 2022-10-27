import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
import numpy as np

# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')
# nltk.download("stopwords")

data = pd.read_csv('tweets_with_coordinations_and_sentiments.csv', sep=',')
df = pd.DataFrame(data=data)

# Removes punctuation and stopwords (including usuario as placeholder for username and 
# words used to name the queen) and lemmatizes words in column 'tweet'. Returns dataframe 
# with columns 'word', 'count' and 'frequency'.
def count_words_in_tweet(df_org):
    df = df_org
    stopwords_list = stopwords.words('english') 
    extra_stopwords = ['queen', 'quen', 'queenelizabeth', 'queenelizabethii', 'elizabeth', 
                        'elizabethii', 'elizabeth2','nelizabeth', 'elisabet', 'elisabeth',
                        'elizabet', 'ii', 'url', 'usuario']
    lemmatizer = WordNetLemmatizer()
    df['tweet'] = df['tweet'].str.replace(r'[^\w\s]+', '', regex=True)
    df['tweet'] = df['tweet'].apply(lambda x: ' '.join([word for word in str(x).split() if word not in (stopwords_list)]))
    df['tweet'] = df['tweet'].apply(lambda x: ' '.join([lemmatizer.lemmatize(w) for w in str(x).split()]))
    df['tweet'] = df['tweet'].apply(lambda x: ' '.join([word for word in str(x).split() if word not in (extra_stopwords)]))
    df['tweet'] = df['tweet'].apply(lambda x: ''.join([i if ord(i) < 128 else '' for i in x]))

    # Tweets to one string
    tweets = df.tweet.str.cat(sep=' ')

    # Tokenize tweets and count word frequencies
    tokens = nltk.tokenize.word_tokenize(tweets)
    frequency = nltk.FreqDist(tokens)

    df_words = pd.DataFrame(frequency.items(), columns=['word', 'count'])
    words_in_df = df_words['count'].sum()
    df_words['frequency'] = df_words['count'].apply(lambda x: float(x)/words_in_df)
    
    return df_words

# Find out frequency of words in all tweets
df_freq = count_words_in_tweet(df)
df_freq.to_csv('word_freq_new.csv', index=False)

df_freq = df_freq.sort_values('frequency', ascending=False)
df_top = df_freq.iloc[0:100].copy()
print(df_top.head)

hist = df_top.plot.bar(x='word', y='frequency')
plt.title('100 most common words in all tweets')
plt.show() 

# Find out frequency of words in sad tweets
d = pd.read_csv('tweets_with_coordinations_and_sentiments.csv', sep=',')
sents = pd.DataFrame(data=d)

sads = sents.loc[sents.sadness.values >= 0.90].copy()
sads_freq = count_words_in_tweet(sads)
sads_freq = sads_freq.sort_values('frequency', ascending=False)
top_sads = sads_freq.iloc[0:100].copy()
print(top_sads.head)

hist = top_sads.plot.bar(x='word', y='frequency')
plt.title('100 most common words in tweets, where sadness >= 0.9')
plt.show() 

# Find out frequency of words in 'others' tweets
oths = sents.loc[sents.others.values >= 0.90].copy()
oths_freq = count_words_in_tweet(oths)
oths_freq = oths_freq.sort_values('frequency', ascending=False)
top_oths = oths_freq.iloc[0:100].copy()
print(top_oths.head)

hist = top_oths.plot.bar(x='word', y='frequency')
plt.title('100 most common words in tweets, where others >= 0.9')
plt.show()