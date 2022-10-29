import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import numpy as np

# csv file should have headers 'tweet', 'others', 'joy', 'sadness', 'anger', 'surprise', 'disgust', 'fear', 'cat_location'
data = pd.read_csv('tweets_with_emotions_and_cat_loc.csv', sep=',')
df = pd.DataFrame(data=data)

df_emots = df[['others', 'joy', 'sadness', 'anger', 'surprise', 'disgust', 'fear']].copy()
median_bar = sns.barplot(data=df_emots, estimator='median', errorbar=None).set_title('Median probabilties for all emotions in all tweets') #confidence interval
plt.savefig('median_bar.png')

others_box= sns.catplot(
    data=df, x="cat_location", y="others",
    kind="box", dodge=False, fliersize=2,
).set_titles('Probabilites for \'other\' emotions by location')
others_box.set(xlabel='location')
plt.savefig('others_box.png')

sadness_box = sns.catplot(
    data=df, x="cat_location", y="sadness",
    kind="box", dodge=False, fliersize=2,
).set_titles('Probabilites for \'sadness\' by location')
sadness_box.set(xlabel='location')
plt.savefig('sadness_box.png')

# Sadness and other are most common sentiments, alhough
# there seems to be great variation of probabilites for both sentiments. 
# oth = df['others'].to_numpy()
# print(np.std(oth))
df['sadness'].std() #0.4522968936678804
df['sadness'].mean() # 0.4353546254864449
df['others'].std() # 0.41552247498750094
df['others'].mean() # 0.4009442069728749

# Make interactive map of the sadness probabilities globaly. Show all datapoints.

df['long'] = df['long'].apply(lambda x: str(x).split()[1])
df['lat'] = df['lat'].apply(lambda x: str(x).split()[1])

fig = px.scatter_geo(df,lat='lat',lon='long', hover_name='tweet', color='sadness')
fig.update_layout(title = 'Tweets reacting to the passing of Queen Elizabeth II', title_x=0.5)
fig.show()
