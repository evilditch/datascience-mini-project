#!/usr/bin/python3
import pandas as pd
import re

# prepping dataframes
user_locations=pd.read_csv('larger_dataset/users_with_locations.csv', usecols=['id', 'location'])
geo=pd.read_csv('geonames/cities15000.txt', sep='\t', usecols=['geonameid', 'name', 'aliases', 'lat', 'long', 'place'])
wcities=pd.read_csv('geonames/world-cities.csv')
l=pd.merge(geo, wcities, how='left', on=['geonameid', 'name']).drop('geonameid', axis=1)

user_locations['location']=user_locations['location'].astype(str).apply(lambda x: x.lower())


for col in ['name', 'aliases', 'place', 'country', 'subcountry']:
    l[col]=l[col].astype(str).apply(lambda x: x.lower())

d=pd.DataFrame(columns=['name', 'subcountry', 'country', 'lat', 'long'], index=range(len(user_locations['id'])))
user_locations=pd.concat([user_locations, d], join='outer', axis=1)

states=pd.read_json('state_abbreviations.json', dtype={'State': str, 'Abbreviations': str})
for col in ['State', 'Abbreviations']:
    states[col]=states[col].apply(lambda x: x.lower())

states.columns=['subcountry', 'abbreviation']
l=pd.merge(l, states, how='left', on=['subcountry'])

# this is what adds the location data from l to a matching 'location' in row (in user_locations)
def for_rows_user(row):
    # basically, first we get the individual words without weird characters
    # then, clean empty strings
    # so when we iterate over big_x, the idea is that x \in big_x are strings of alphanumeric value
    # why numeric? no reason
    # then we iterate over x
    # while doing so, calculate a boolean mask for l (now copied into z) such that it contains
    # ...every 'in'-type hit from x
    # then get the subset of z where mask is true
    # and do the same for next x
    #
    # in essence, the query is
    # (x_1 in country OR x_1 in subcountry OR x_1 in name OR x_1 in abbreviation) AND (x_2 in country OR x_2 in sub..)
    # AND (x_3 ...) ... AND (x_n )
    # 
    # if the query yields something, we just pick a 'random' one and call it our place
    # all californians end in some town that starts with 'a', but that's not a huge loss
    z=l.copy()
    big_x = [re.sub(r'[^a-zA-Z0-9]', '', x).strip(' ') for x in row[1].split(' ')]
    if '' in big_x:
        big_x.remove('')
    for x in big_x:
        mask=z['country'].str.contains(x)
        for col in ['subcountry', 'abbreviation', 'name']:
            mask = (mask) | (z[col].str.contains(x)) # OR operator on the boolean mask
        z=z[mask]
    if not z.empty:
        a=z.sort_values(by='name').iloc[0]
        #print(a)
        row.country=a.country
        row.subcountry=a.subcountry
        row.values[2]=a.values[0] # as Series.name already exists and refers to its position in it's home dataframe
        row.lat=a.lat
        row.long=a.long
        print(row.name)
        return(row)

xd=user_locations.apply(for_rows_user, axis=1)
xd.to_csv('user_locations.csv')

