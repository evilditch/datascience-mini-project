# datascience-mini-project

## files

Folder 'smaller_dataset':
- queen.csv: Tweets after queen Elizabeth II's death, loaded from [Kaggle](https://www.kaggle.com/datasets/aneeshtickoo/tweets-after-queen-elizabeth-iis-death). (licence: CC0, public domain)
- eng_tweets.csv: tweets whose language=en
- unique_users_ids.txt: ids of the unique users of the dataset
- unique_users_all.csv: all unique users (id, username, name, location)
- unique_users_with_locations.csv: those unique users whose location field has some content
- tweets_with_locations.csv: english tweets and tweeters' locations in one table

Folder 'larger_dataset':
- raw_tweets_queens_death.xlsx: tweets surrounding the immediate time frame of death of the queen Elizabeth II, from [Kaggle](https://www.kaggle.com/datasets/welcomehere/death-of-the-queen?select=raw_tweets_queens_death.xlsx)
- en_tweets.csv: tweets whose language=en
- located_users_tweets.csv: tweets of users whose has something in location field
- unique_users_all.csv: all unique users (id, username, name, location)
- users_with_locations.csv: those unique users whose location field has some content
- tweets_with_locations.csv: english tweets and tweeters' locations in one table

Folder 'tools':
- sadness_lexicon.txt: lemmas of words indicating sadness, extracted from [NRC Emotion Lexicon](http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm). (Saif Mohammad and Peter Turney. 'Crowdsourcing a Word-Emotion Association Lexicon'. <i>Computational Intelligence</i>, 29(3): 436-465, 2013. Wiley Blackwell Publishing Ltd.) (Saif Mohammad and Peter Turney. 'Emotions Evoked by Common Words and Phrases: Using Mechanical Turk to Create an Emotion Lexicon.' <i>In Proceedings of the NAACL-HLT 2010 Workshop on Computational Approaches to Analysis and Generation of Emotion in Text</i>, June 2010, LA, California.)
- predict_sentiment.py: code for sentiment prediction with [pysentimento](https://github.com/pysentimiento/pysentimiento). Citation: Juan Manuel Pérez and Juan Carlos Giudici and Franco Luque, 'pysentimiento: A Python Toolkit for Sentiment Analysis and SocialNLP tasks', 2021, 
https://doi.org/10.48550/arXiv.2106.09462


Folder 'geonames':
- cities15000.txt: all cities such that their population is > 15000 + capitals (in case they are smaller than that). Source: [GeoNames Gazetteer files](http://download.geonames.org/export/dump/). Reeleased under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/).
