# %% [markdown]
# ##### 1: Inner Merges

# %%
import pandas as pd
games = pd.read_csv('c01-games.csv')
locations = pd.read_csv('c01-locations.csv')
scores = pd.read_csv('c01-scores.csv')
games.head()

# %%
merged_df = pd.merge(left=games,
                     right=scores,
                     left_on='scores_id',
                     right_on='id',
                     how='inner')
merged_df.head()

# %%
merged_df.sort_values(by='home_score', ascending=False).head()

# %%
locations.head()

# %%
full_df = pd.merge(left=merged_df,
                   right=locations,
                   left_on='location_id',
                   right_on='id',
                   how='inner')
full_df.sort_values(by='home_score', ascending=False).head()

# %% [markdown]
# ##### 2: Left Merges

# %%
leftMerged_df = pd.merge(left=games,
                     right=scores,
                     left_on='scores_id',
                     right_on='id',
                     how='left')
leftMerged_df.head()
# %%
leftMerged_df[leftMerged_df['home_score'].isna()]

# %%
innerMerged_df = pd.merge(left=games,
                     right=scores,
                     left_on='scores_id',
                     right_on='id',
                     how='inner')
innerMerged_df[innerMerged_df['home_score'].isna()]

# %% [markdown]
# ##### 3: Right Merges

# %%
rightMerged_df = pd.merge(left=games,
                          right=scores,
                          left_on='scores_id',
                          right_on='id',
                          how='right')
rightMerged_df[rightMerged_df['home_team'].isna()]

# %%
innerMerged_df[innerMerged_df['home_score'].isna()]

# %% [markdown]
# ##### 4: Outer Merge

# %%
outerMerge_df = pd.merge(left=games,
                         right=scores,
                         left_on='scores_id',
                         right_on='id',
                         how='outer')
outerMerge_df[outerMerge_df.isna().any(axis=1)]

# %% [markdown]
# ##### 5: Multiple Columns

# %%
shootouts = pd.read_csv('c01-shootouts.csv')
goals = pd.read_csv('c01-goalscorers.csv')
goals.head()

# %%
multiMerged_df = pd.merge(left=shootouts,
                          right=goals,
                          left_on=['shootout_date', 'home_team', 'away_team'],
                          right_on=['game_date', 'home_team', 'away_team'],
                          how='left')
multiMerged_df.head()

# %%
multiMerged_df[multiMerged_df['shootout_date'] == '2022-12-18']

# %% [markdown]
# ##### 6: Choosing a Merge Method

# %%
results = pd.read_csv('c01-finalscore.csv')
worldcupgames = pd.read_csv('c01-worldcupgames.csv')
results.head()

# %%
worldcupgames.head()

# %%
# -> Determine the number of goals scored in each FIFA World Cup.
numGoals_df = pd.merge(left=results,
                       right=worldcupgames,
                       left_on=['date','home_team','away_team'],
                       right_on =['date','home_team','away_team'],
                       how = 'inner')
numGoals_df.head()

# %%
# -> Determine the amount of goals scored in world cup games compared to goals scored in other games.
amountGoals_df = pd.merge(left=results,
                       right=worldcupgames,
                       left_on=['date','home_team','away_team'],
                       right_on =['date','home_team','away_team'],
                       how = 'left')
amountGoals_df.head()