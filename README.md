# datascience-mini-project

## files

### Folder 'smaller_dataset':
- queen.csv: Tweets after queen Elizabeth II's death, loaded from [Kaggle](https://www.kaggle.com/datasets/aneeshtickoo/tweets-after-queen-elizabeth-iis-death). (licence: CC0, public domain)
- eng_tweets.csv: tweets whose language=en
- unique_users_ids.txt: ids of the unique users of the dataset
- unique_users_all.csv: all unique users (id, username, name, location)
- unique_users_with_locations.csv: those unique users whose location field has some content
- tweets_with_locations.csv: english tweets and tweeters' locations in one table

### Folder 'larger_dataset':
data files:
- raw_tweets_queens_death.xlsx: tweets surrounding the immediate time frame of death of the queen Elizabeth II, from [Kaggle](https://www.kaggle.com/datasets/welcomehere/death-of-the-queen?select=raw_tweets_queens_death.xlsx)
- en_tweets.csv: tweets whose language=en
- located_users_tweets.csv: tweets of users whose has something in location field
- unique_users_all.csv: all unique users (id, username, name, location)
- users_with_locations.csv: those unique users whose location field has some content
- tweets_with_locations.csv: english tweets and tweeters' locations in one table
- tweets_with_coordinates.csv: joined location diteils from users (file ../user_locations.csv)
- word_freq.csv: unique, lemmatized, lowercase words in tweets_with_coordinates.csv and their frequencies (made with file tools/word_frequency.py)

python scripts:
- predict_sentiment.py: predict emotions for tweets in file 'tweets_with_coordinates.csv'. Tweets undergo some text cleaning: hashtags are removed and usernames and urls are replaced with palceholder-strings. No stemming is done. New dataframe is saved to file 'tweets_with_coordinations_and_sentiments.csv'. Emotion are predicted using [pysentimento](https://github.com/pysentimiento/pysentimiento). (Juan Manuel Pérez and Juan Carlos Giudici and Franco Luque, 'pysentimiento: A Python Toolkit for Sentiment Analysis and SocialNLP tasks', 2021, 
https://doi.org/10.48550/arXiv.2106.09462)
- create_cat_location.py': create a new column for categorical location data, and unnecessary columns are dropped. New dataframe is saved in file 'tweets_with_emotions_and_cat_loc.csv'. This dataframe is used to analyze the emotions.
- analyze_data.py: do visualizations and calculate statistics from data in 'tweets_with_emotions_and_cat_loc.csv'. Show sadness scores in map, calculate [medians for all emotions in tweets](https://github.com/evilditch/datascience-mini-project/blob/main/larger_dataset/median_bar.png), create boxplot for [sadness](https://github.com/evilditch/datascience-mini-project/blob/main/larger_dataset/sadness_box.png) and [others](https://github.com/evilditch/datascience-mini-project/blob/main/larger_dataset/others_box.png) in different categorical locations.
- create_maps.py: create [map](https://github.com/evilditch/datascience-mini-project/blob/main/larger_dataset/world_sadness.png) of sadness propabilites of all tweets.


### Folder 'tools':
- word_frequency.py: code for counting word frequencies with [nltk tools](https://www.nltk.org/)

### Folder 'geonames':
- cities15000.txt: all cities such that their population is > 15000 + capitals (in case they are smaller than that). Source: [GeoNames Gazetteer files](http://download.geonames.org/export/dump/). Reeleased under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/).
