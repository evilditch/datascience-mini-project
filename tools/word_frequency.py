import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer

# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')
# nltk.download("stopwords")

data = pd.read_csv('tweets_with_coordinations_and_sentiments.csv', sep=',')
df = pd.DataFrame(data=data)

# Remove punctuation, stopwords and lemmatize
stopwords_list = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
df['tweet'] = df['tweet'].str.replace(r'[^\w\s]+', '', regex=True)
df['tweet'] = df['tweet'].apply(lambda x: ' '.join([word for word in str(x).split() if word not in (stopwords_list)]))
df['tweet'] = df['tweet'].apply(lambda x: ' '.join([lemmatizer.lemmatize(w) for w in str(x).split()]))

# Tweets to one string
tweets = df.tweet.str.cat(sep=' ')

# Tokenize tweets and count word frequencies
tokens = nltk.tokenize.word_tokenize(tweets)
frequency = nltk.FreqDist(tokens)
most_common = frequency.most_common(100)

df_freq = pd.DataFrame(frequency.items(), columns=['word', 'frequency'])
df_freq.to_csv('word_freq.csv', index=False)