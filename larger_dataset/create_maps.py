import geopandas as gp
import matplotlib.pyplot as plt
import pandas as pd

d = pd.read_csv('tweets_with_emotions_and_cat_loc.csv', sep=',')
df = pd.DataFrame(d)

df['long'] = df['long'].apply(lambda x: str(x).split()[1])
df['lat'] = df['lat'].apply(lambda x: str(x).split()[1])

gdf = gp.GeoDataFrame(
    df, geometry=gp.points_from_xy(df.long, df.lat))

world = gp.read_file(gp.datasets.get_path('naturalearth_lowres'))
world = world[(world.name != "Antarctica")]
base = world.plot(color='white', edgecolor='black')

ax=base
ax.set_axis_off()

gdf.plot(ax=ax, column='sadness', alpha=0.1, markersize=2, cmap='OrRd', legend=True)
plt.title('Sadness probabilities in all tweets')
#plt.savefig('world_sadness.png')
plt.show()