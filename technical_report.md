# Technical report for project 'Local differences in lexicon on Twitter, regarding the passing of Queen Elizabeth II'

## Motivation
Our initial plan was to illustrate the possible differences in reactions to the passing of Queen Elizabeth II, as expressed in Twitter. We were interested finding out details about the lexicon  used in tweets and whether we could predict sentiments expressed by them. Could we perhaps find out global differences in political views or attitude towards the Brittish monarchy? Our findings could be used to further study these issues, which we belive to interest political and social researches.

## Twitter API 

Our first task was to collect the data. We spend time familiarizing with the Twitter API, which was new to all of us.  We noticed that Twitter API allows non-research users only to pull tweets from the last two weeks, which ment, that we could not pull them ourselves, since our topic of interest was to study the immidate reactions to the death of Queen Elizabeth II. We decided to use pre-exsting datasets that we found on Kaggle. 

Only a small fraction of tweets include location information. So that we could combine location information with tweets, we searched from the Twitter API the information of all users whose tweets were included in the dataset we downloaded from Kaggle. To locate the tweets, we used the locations that users freely provided in their profile.

## Location information

The location information of user profiles is a free text field. In practise, the location string could be anything from the obvious "London, UK" to the location-impossible "Universum". There were also variations of the spelling of places; for example there could be "United States", "USA", "U.S." or "U.S.A.".

We wanted to connect freely provided location information with latitude and longitude coordinates. For that, we merged geonames sets of countries, states of USA and all cities with a population larger than 15000. The total geoname set has also aliases and abbreviations, so we could get same places despite the spelling variations.

We compared the location information string of the user profiles with set of geonames: first comparing with countries, then with subcountries (like a state), then with cities and last with approviations and aliases. We selected users whose location info we could identify, and used their twiits.

There may be errors in identified locations, because we only compare strings with each other. For example, short words could correspond to the abbreviation of some place.

Some users are provided their location with emoji flags. We just use alphanumeric values, but by using also unicode-emoji-characters, we could have localized more users.

## Sentiment analysis
For sentiment analysis we originally planned to use pre-existing lists of words describing positive and negative sentiments or some python library, that would calculate the sentiment possibilities for each tweet. We found good tools for this, but quickly realised, that dividing tweets into positive and negative categories wouldn't work for our task, since word lists (and  machine learning algorithims) tend to categorise words associated with death as highly neagtive. Naturally, great deal of our data set contained words such as ‘died’, ‘death’, ‘passing’, although the tweets themselves were neutral or even sympathetic in tone. Simply turning the interpretation of positive to negative and negative to positive would also not have worked, since sentence like ‘The Queen died today’ and ’The Queen was bad’ would still gain roughly the same sentiment scores. 

We decided to use more detailed approch to study the emotions behind the tweets. We used pysentimento library to calculate probabilites for five emotions and category ‘others’, that covers uncertain emotions. Not-suprisingly sadness and others were the most common emotions, although the standard deviation within the emotiongroups was high.

It would be interesting to analyse the emotions by finding most common phrases with n-grams. In this way we could eliminate some common phrases such as ‘we are saddened’ and ‘rest in peace’, and gain more detailed view of the opinions expressed in tweets. Unfortunately constructing these kind of n-grams proved to be too laborous for this project.
## Data visualization
Our first plan for data visualization was to make an interactive map of all the tweets placed on a world map and their emotions. With plotly express this worked out great locally, but making an interactive map and embedding it to a website was a bit tricky. Our dataset was too large to use as is in plotly Chart Studios free version and only showing a small portion of the data would not have been much better than showing a static map of all tweets, which we ended up doing.

Because pysentimento library provaided us with probabilities for different emotions, it was quite straithforward to make some charts with them. Offcourse our dataset and time was limited, so we couldn't make that profound of an analysis. We divided the dataset to subcategories by emotion and by location information. Sadness and others were only big enouhg emotiongroups to study to. We decided location based categories by our our perception of possible political and social differencies regarding the death of Queen and by somewhat matching group sizes.

## Learning outcome and final thoughts
The project was a great way to learn about many different aspects of data science from data collection to visualization.
One of the most suprising realizations was, that collecting and manipulating data to a form suitable for an analysis was such a challengin task. This ate up more time than we anticipated, so we could not focus on the natural language prosessing aspect of the project as much as we originally intented to.

Data manipulation with python's pandas library became quite familiar during the project. We also had to study the use of many different python libraries and tecnologies (pyplot Chart Studio and pyplot express, geopandas, pysntimento, hugginface, git LFS...), although we didn't end up using all of them. We learned some basic aspects of natural language processing, such as problems with sentiment analyses and what they actually can tell about a text. The importance of preprocessing the data properly also became apparent, when we calculated some wordfrequencies (which didn't end up in the final product).

