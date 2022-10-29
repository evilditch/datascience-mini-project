import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tweets_with_coordinations_and_sentiments.csv', sep=',')

# Creates column, which tells is the tweeter from uk, other commonwealth country, usa or 
# somewhere else (ot). Drop unnecessary columns.
def create_cat_loc(cw, dataf):
    cat_list = ['other'] * len(dataf)
    for i, row in dataf.iterrows():
        if 'united kingdom' in row['country']:
            cat_list[i]='uk'
        elif 'united states' in row['country']:
            cat_list[i]='us'
        else:
            for place in cw:
                if place in row['country']:
                    cat_list[i]='commonwealth'
    dataf.insert(0, 'cat_location', cat_list)
    dataf = dataf.drop(['Unnamed: 0', 'sentiment', 'id', 'user_id'], axis=1)
    return dataf

commonwealth = ['antigua and barduba', 'australia', 'bahamas', 'bangladesh', 'barbados', 'belize', 'botswana', 'brunei', 
'cameroon', 'canada', 'cyprus', 'dominica', 'eswatini','fiji', 'gabon', 'gambia', 'ghana', 'grenada', 'guyana', 
'india', 'jamaica', 'kenya', 'kiribati', 'lesotho', 'malawi', 'malaysia', 'maldives', 'malta', 'mauritius', 'mozambique', 'namibia', 'nauru', 'new zealand', 
'nauru', 'nigeria', 'pakistan', 'papua new guinea', 'rwanda', 'singapore', 'saint kitts and nevis', 'saint lucia', 'saint vincent and the greanadines', 'samoa', 'seychelles', 'sierra leone', 'singapore', 'solomon islands','south africa', 'sri lanka', 
'tanzania', 'togo', 'tonga', 'trinidad and tobago', 'tuvalu', 'uganda', 'vanuatu', 'zambia']
all_df = create_cat_loc(commonwealth, df)

all_df.to_csv('tweets_with_emotions_and_cat_loc.csv', sep=',')