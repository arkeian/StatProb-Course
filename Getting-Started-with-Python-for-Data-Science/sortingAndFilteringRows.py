# %% [markdown]
# ##### 1: Row Indexes

# %%
import pandas as pd
vehicles = pd.read_csv('vehicles.csv')
vehicles.head()

# %%
vehicles.index

# %%
transmission_counts = vehicles['transmission'].value_counts()
transmission_counts

# %%
transmission_counts.index

# %%
# Resetting to the standard RangeIndex
transmission_counts.reset_index()

# %% [markdown]
# ##### 2: Sorting Rows

# %%
vehicles = vehicles.sort_values(by='year')
vehicles.head()

# %%
vehicles = vehicles.sort_values(by='best_mpge', ascending=False)
vehicles.head()

# %%
vehicle_years = vehicles['year'].value_counts()
vehicle_years

# %%
vehicle_years.sort_index()

# %% [markdown]
# ##### 3: Selecting Specific Rows

# %%
vehicles = vehicles.sort_values(by='year', ascending=False)
vehicles.head()

# %%
vehicles.loc[[1940, 718], ['manufacturer']]

# %%
vehicles.iloc[[0, 1], [6]]

# %% [markdown]
# ##### 4: Selecting Ranges of Rows
# ###### NOTE:
# ###### The slice's stopping index is incluced in loc, while not in iloc

# %%
vehicles = vehicles.sort_index()
vehicles.head()

# %%
vehicles.iloc[:4, :5]

# %%
vehicles.loc[1:2, 'vehicle_type':'fuel_configuration']

# %%
vehicles.loc[:20, 'year':]

# %% [markdown]
# ##### 5: Boolean Masks

# %%
gt25 = vehicles['best_mpge'] >= 25
gt25.head()

# %%
is_sedanwagon = vehicles['vehicle_type'] == 'sedan/wagon'
is_sedanwagon.head()

# %% [markdown]
# ##### 6: Filtering Rows with Booleans

# %%
gt40 = vehicles['best_mpge'] > 40
vehicles[gt40].head()

# %%
vehicles[vehicles['transmission'] == 'auto'].head()

# %% [markdown]
# ##### 7: Combining Booleans with AND

# %%
vehicle_year = vehicles['year'] > 2016
vehicle_fuel = vehicles['fuel'] == 'electric'
combined = vehicles[vehicle_year & vehicle_fuel]
combined.sort_values(by='year', ascending=False).head()

# %%
vehicles[(vehicles['fuel'] == 'biodiesel (b20)') & (vehicles['best_mpge'] > 40)].sort_values(by='year', ascending=False).head()

# %% [markdown]
# ##### 8: Combining Booleans with OR

# %%
is_ethanol = vehicles['fuel'] == 'ethanol (e85)'
is_methanol = vehicles['fuel'] == 'methanol'
combined = is_ethanol | is_methanol
vehicles[combined].sort_values(by='year', ascending=False).head()

# %%
is_electric = vehicles['fuel'] == 'electric'
gt40 = vehicles['best_mpge'] > 40
electric_or_above_average = vehicles[is_electric | gt40]
electric_or_above_average.head()

# %% [markdown]
# ##### 9: Inverting Booleans with NOT

# %%
is_ford = vehicles['manufacturer'] == 'ford'
is_truck = vehicles['vehicle_type'] == 'pickup'
is_ford_truck = is_ford & is_truck
not_ford_truck = ~is_ford_truck
vehicles[not_ford_truck].head()

# %%
is_chevrolet = vehicles['manufacturer'] == 'chevrolet'
is_gmc = vehicles['manufacturer'] == 'gmc'
not_chevrolet_gmc = vehicles[~(is_chevrolet | is_gmc)]
not_chevrolet_gmc.head()