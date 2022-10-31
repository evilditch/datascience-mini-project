# Technical report for project 'Local differences in lexicon on Twitter, regarding the passing of Queen Elizabeth II'

MOODLEN OHJEET: Technical report: The technical report is simply an essay you can return in PDF (max 5 pages). This is the place to describe the technical components of your work, and refer to all the methods you used backend and usually are not interesting to your target audience. Reflect on your initial mini-project canvas: what worked? What didn't (and why)? What changes did you have to make from your initial plan and why? What would you have done differently now? What would possible future steps be? Tell us about your experience, technical implementation of the project and reflect on your learning outcomes. The structure of the report is up to you. If it helps, you can use the elements of the mini-project canvas, e.g. data collection, preprocessing, visualisations, machine learning, communication of results, building the platform, etc.

## Motivation

Our initial plan was to illustrate the possible differences in reactions to the passing of Queen Elizabeth II, as expressed in Twitter. We were interested finding out details about the lexicon  used in tweets and wheather we could predict sentiments expressed by them. Could we perhaps find out global differences in political views and attitude towards the Brittish monarchy.  Our findings could be used to further study these issues, which we belive to interest political and social researches. 

## Twitter API 

Our first task was to collect the data. We spend time familiarizing with the Twitter API, which was new to all of us.  We noticed that Twitter API allows non-resear users only to pull tweets from the last two weeks, which ment, that we could not pull them ourselves, since our topic of interest was to study the immidate reactions to the death of Queen Elizabeth II. We decided to use pre-exsting datasets that we found on Kaggle. 

Only a small fraction of twiits include location information. So that we could combine location information with tweets, we searched from the Twitter API the information of all users whose tweets were included in the dataset we downloaded from Kaggle. To locate the tweets, we used the locations that users freely provided in their profile.

## Location information

The location information of user profiles is a free text field. In practise, the location string could be anything from the obvious "London, UK" to the location-impossible "Universum". There were also variations of the spelling of places; for example there could be "United States", "USA", "U.S." or "U.S.A.".

We wanted to connect freely provided location information with latitude and longitude coordinates. For that, we used the geoname set of all cities with a population is larger than 15000. The set has also aliases of the name of places, so we could find the same place despite the spelling variations.

We compared the location information string of the user profiles with set of geonames, and selected users whose location we could identify.
(moniosaisten nimien ongelma)

## Github storage
Problems with large datafiles...

## Sentiment analysis
For sentiment analysis we planned to use pre-existing lists of words descirbing positive and negative sentiments and some python library, that would calculate the sentiment possibilities for each tweet. We found good tools for this, but quickly realised, that dividing tweets into positive and negative categories wasn’t going to work in our task, since word lists (and  machinelearning algorithims) tend to categorise words associated to death as highly neagtive. Naturally, great deal of our tweets contained words such as ‘died’, ‘death’, ‘passing’, although the tweets themselves were neutral or sympathetic in tone. Simply turning the interputiation of positive to negative and negative to positve would also not have worked, since sentence like ‘The Queen died today’ and ’The Queen was bad’ would still gain roughly the same sentiment scores. 

We decided to use more detailed approch to study the emotions behind the tweets. We used pysentimento library to calculate probabilites for five emotions and emotion called ‘others’, that covers uncertain emotions. Not-suprisingly sadness and others were the most common emotions, although the standard deviation within the emotiongroups was high. …
It would be interesting to analyse the emotions by finding most common phrases with n-grams. In this way we could eliminate some common phrases such as ‘we are saddened’ and ‘rest in peace’, and gain more detailed view of the opinions expressed in tweets. Unfortunately constructing these kind of n-grams proved to be to laborous for this project.



 