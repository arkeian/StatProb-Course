# %% [markdown]
# ##### Project Task: Analyze Electric Vehicle Stations with Python

# %%
import pandas as pd
stations = pd.read_csv('stations.csv')
stations.head()

# %%
stations['fuel'].value_counts()

# %%
stations['owner'].value_counts()

# %%
stations['access'].value_counts()

# %%
stations['number_of_stations'].describe()

# %%
stations = stations.sort_values(by='number_of_stations', ascending=False)
stations.head()

# %%
stations = stations.sort_values(by='number_of_stations')
stations.head()

# %%
is_public_access = stations['access'] == 'public'
is_electric = stations['fuel'] == 'electric'
public_electric = stations[is_public_access & is_electric]

# %%
public_electric = public_electric.sort_values(by='number_of_stations')
public_electric.head()

# %%
is_privately_owned = public_electric['owner'] == 'private'
privately_owned = public_electric[is_privately_owned]
privately_owned.head()

# %%
privately_owned['state'].describe()

# %%
not_privately_owned = public_electric[~is_privately_owned]
not_privately_owned.head()

# %%
not_privately_owned['state'].describe()

# %%
not_privately_owned['number_of_stations'].describe()

# %%
is_above_17 = not_privately_owned['number_of_stations'] > 17
above_17 = not_privately_owned[is_above_17]
above_17.head()

# %%
above_17.sort_values(by='number_of_stations')

# %%
is_washington = public_electric['state'] == 'WA'
is_oregon = public_electric['state'] == 'OR'
WA_or_OR = public_electric[is_washington | is_oregon]
WA_or_OR.sort_values(by=['owner', 'number_of_stations'])
