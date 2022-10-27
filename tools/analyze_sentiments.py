import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# a csv file should have headers 'tweet', 'others', 'joy', 'sadness', 'anger', 'surprise', 'disgust', 'fear'
data = pd.read_csv('tweets_with_coordinations_and_sentiments.csv', sep=',')
df = pd.DataFrame(data=data)

o = df['others'].median()
j = df['joy'].median()
sad = df['sadness'].median()
a = df['anger'].median()
su = df['surprise'].median()
d = df['disgust'].median()
f = df['fear'].median()

plt.bar(['others', 'joy', 'sadness', 'anger', 'surprise', 'disgust', 'fear'], [o, j, sad, a, su, d, f])
plt.title('Median probabilities for all sentiments in all tweets')
plt.savefig('medians_for_sentiments.png')

# Sadness and other are most common sentiments, let's focus on them.
fig, ax = plt.subplots()
ax.boxplot(x=[df['sadness'], df['others']], vert=False, labels=['sadness', 'others'])
plt.title('Probabilities for \'sadness\' and \'others\' in all tweets')
plt.savefig('boxplot_sad_others.png')

# There seems to be great variation of probabilites for both sentiments. 
oth = df['others'].to_numpy()
print(np.std(oth))

sad = df['sadness'].to_numpy()
print(np.std(sad))

print(np.mean(oth))
print(np.mean(sad))

# Plot tweets to wordmap with sadness 
import plotly.express as px

df['long'] = df['long'].apply(lambda x: str(x).split()[1])
df['lat'] = df['lat'].apply(lambda x: str(x).split()[1])

fig = px.scatter_geo(df,lat='lat',lon='long', hover_name='tweet', color='anger')
fig.update_layout(title = 'Tweets reacting to the passing of Queen Elizabeth II', title_x=0.5)
fig.show()