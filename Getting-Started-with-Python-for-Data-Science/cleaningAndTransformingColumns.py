# %% [markdown]
# ##### 1: Column Information

# %%
import pandas as pd
parks = pd.read_csv('nationalpark_visitors.csv')
parks.head()

# %%
parks.info()

# %% [markdown]
# ##### 2: Renaming and Removing Columns

# %%
new_column_name = {
    'Year2019': 'Visitors2019',
    'Year2020': 'Visitors2020',
    'Year2021': 'Visitors2021'
}
parks = parks.rename(mapper=new_column_name, axis=1)
parks.head()

# %%
parks = parks.drop(labels='index', axis=1)
parks.head()

# %% [markdown]
# ##### 3: Calculations in Python

# %%
grand_canyon_price = parks.loc[parks['Park'] == 'Grand Canyon', 'AnnualPassPrice'].item()
amount_saved = grand_canyon_price * 0.3
new_price = round(grand_canyon_price - amount_saved)
new_price

# %%
visitors2019, visitors2020 = [float(x) for x in parks.loc[parks['Park'] == 'Zion', ['Visitors2019', 'Visitors2020']].values[0]]
percentchange_2020 = (visitors2020 - visitors2019) / visitors2020 * 100
percentchange_2020

# %%
rounded_percent = round(percentchange_2020, 2)
rounded_percent

# %% [markdown]
# ##### 4: Column Calculations in Pandas

# %%
parks['Change2020'] = parks['Visitors2020'] - parks['Visitors2019']
parks.loc[:, 'Visitors2020':'Change2020']

# %%
parks['PercentChange2020'] = parks['Change2020'] / parks['Visitors2019'] * 100
parks.head()

# %%
parks['PercentChange2020'] = round(parks['PercentChange2020'], 2)
parks['PercentChange2020'].describe()

# %% [markdown]
# ##### 5: Splitting and Combining Columns

# %%
parks[['AreaValues', 'Area']] = parks['Area'].str.split(pat=' ', expand=True)
parks[['Area', 'AreaValues']].head()

# %%
parks['ParkTitle'] = parks['Park'].str.cat(parks['ParkType'], sep=' ') 
parks[['Park', 'ParkType', 'ParkTitle']].head()

# %%
parks['State'] = parks['Location'].str.split(pat=',', expand=True)[1]
parks[['Location', 'State']].head()

# %% [markdown]
# ##### 6: Modifying Text Data

# %%
parks['ParkTitle'] = parks['ParkTitle'].str.title()
parks['ParkTitle'].head()

# %%
parks['State'] = parks['State'].str.strip()
parks['State'].head()

# %%
parks['ParkTitle'] = parks['ParkTitle'].str.replace(pat='&', repl='And', regex=False)
parks.loc[37,:]

# %% [markdown]
# ##### 7: Changing Data Types

# %%
parks['AreaValues'] = parks['AreaValues'].astype('float64')

# %%
parks['State'] = parks['State'].astype('category')

# %%
parks.info()
