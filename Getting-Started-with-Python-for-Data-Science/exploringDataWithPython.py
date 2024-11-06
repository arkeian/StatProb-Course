# %% [markdown]
# ##### 1: Importing Datasets

# %%
import pandas as pd

# %%
laptops = pd.read_csv('laptops.csv')

# %%
laptops.head()

# %% [markdown]
# ##### 2: Data Types
# ###### Types of data:
# ###### a. Numeric Data (float64, int64)
# ###### b. Text Data (object) -> for text-based or unrecognized data
# ###### c. Categorical Data (category) -> for data with predefined values

# %%
laptops.dtypes

# %% [markdown]
# ##### 3: Variables

# %%
var1 = 3.14
var1 = 'Python'
type(var1)

# %%
var2 = pd.read_csv('laptops.csv')
type(var2)

# %% [markdown]
# ##### 4: Lists

# %%
commands = ["import pandas", "pd.read_csv()"]
commands

# %%
commands[0] = "import pandas as pd"
commands

# %%
commands.append("dataframe.head()")
commands

# %%
number_of_commands = len(commands)
number_of_commands

# %% [markdown]
# ##### 5: Dictionaries

# %%
kitchen = {
    "coffee makers": 3635,
    "food processors": 2450,
    "kettles": 1282
}

kitchen

# %%
kitchen["coffee makers"] += 2
kitchen

# %%
kitchen["toasters"] = 910
kitchen

# %% [markdown]
# ##### 6: Methods

# %%
laptops.head(n=10)

# %%
category = 'LAPTOP'
category_counts = [2265,4139,704]

category.lower()

# %%
category_counts.sort()
category_counts

# %%
category_counts.sort(reverse=True)
category_counts

# %% [markdown]
# ##### 7: Summarizing Categorical Data

# %%
# Accessing columns as Pandas Series
laptops['brand']

# %%
# Accessing columns as Lists
laptops[['brand']]

# %%
laptops[['brand']].head(n=10)

# %%
# Count values as raw numbers from largest to smallest
laptops['brand'].value_counts()

# %%
# Count values as percentages
laptops['brand'].value_counts(normalize=True)

# %%
# Count values as percentages from smallest to largest
laptops['repair_status'].value_counts(ascending=True, normalize=True)

# %% [markdown]
# ##### 8: Summarizing Numerical Data

# %%
laptops['age'].describe()

# %%
laptops['repair_status'].describe()

# %%
laptops['age'].describe().loc['max']

