#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import matplotlib.pyplot as plt 
from sklearn import linear_model


# In[48]:


ipl_matches = pd.read_csv("C:\\Users\shubham\Desktop\matches.csv")
ipl_matches


# In[52]:


ipl_delveries = pd.read_csv("C:\\Users\shubham\Desktop\deliveries.csv")
ipl_deliveries


# In[43]:


ipl_matches.info()


# In[42]:


ipl_matches.describe()


# In[49]:


ipl_matches.columns


# In[20]:


for col in ipl_matches:
    print(ipl_matches[col].unique())


# In[21]:


#the first index that doesn't contain a NaN value 
ipl_matches.umpire3.first_valid_index()


# In[23]:


#Confirming the first valid index
ipl_matches.loc[633:640]


# In[24]:


ipl_matches.isnull().sum()


# In[54]:


ipl_matches = ipl_matches.drop(columns=['umpire3'], axis=1)


# In[55]:


ipl_deliveries.info()


# In[56]:


#Replacing the Full names of IPL TEAMS by short names
ipl_matches.replace(['Mumbai Indians','Kolkata Knight Riders','Royal Challengers Bangalore','Deccan Chargers','Chennai Super Kings',
                 'Rajasthan Royals','Delhi Daredevils','Gujarat Lions','Kings XI Punjab',
                 'Sunrisers Hyderabad','Rising Pune Supergiants','Kochi Tuskers Kerala','Pune Warriors','Rising Pune Supergiant']
                ,['MI','KKR','RCB','DC','CSK','RR','DD','GL','KXIP','SRH','RPS','KTK','PW','RPS'],inplace=True)


# In[57]:


#Replacing the Full names of IPL TEAMS by short names
ipl_deliveries.replace(['Mumbai Indians','Kolkata Knight Riders','Royal Challengers Bangalore','Deccan Chargers','Chennai Super Kings',
                 'Rajasthan Royals','Delhi Daredevils','Gujarat Lions','Kings XI Punjab',
                 'Sunrisers Hyderabad','Rising Pune Supergiants','Kochi Tuskers Kerala','Pune Warriors','Rising Pune Supergiant']
                ,['MI','KKR','RCB','DC','CSK','RR','DD','GL','KXIP','SRH','RPS','KTK','PW','RPS'],inplace=True)


# In[61]:


# merging seasons column in deliveries dataset which will be helpful in further analysis for each season
ipl_deliveries = ipl_deliveries.merge(ipl_matches["season"], left_on=ipl_deliveries.index, right_on=ipl_matches.index)


# In[62]:


#EXPLORATORY Exploratory Data Analysis(EDA) is an approach to analyzing data sets to summarize their main characteristics, often with visual methods.



import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.color_palette("Paired")
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (12, 8)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# In[63]:


teams_per_season = ipl_matches.groupby('season')['winner'].value_counts()
teams_per_season


# In[65]:


"""
for i, v in win_per_season.iteritems():
    print(i, v)
    
for items in win_per_season.iteritems():
    print(items)    
"""
year = 2008
win_per_season_df = pd.DataFrame(columns=['year', 'team', 'wins'])
for items in teams_per_season.iteritems():    
    if items[0][0]==year:
        print(items)
        win_series = pd.DataFrame({
            'year': [items[0][0]],
            'team': [items[0][1]],
            'wins': [items[1]]
        })
        win_per_season_df = win_per_season_df.append(win_series)
        year += 1   


# In[73]:


plt.title("Team Wise Win Per Season")
sns.barplot('wins', 'team', hue='year', data=win_per_season_df, palette='Paired');


# In[85]:


venue_ser = ipl_matches['venue'].value_counts()


# In[87]:


venue_df = pd.DataFrame(columns=['venue', 'matches'])
for items in venue_ser.iteritems():
    temp_df = pd.DataFrame({
        'venue':[items[0]],
        'matches':[items[1]]
    })
    venue_df = venue_df.append(temp_df, ignore_index=True)


# In[89]:


plt.title("IPL Venues")
sns.barplot(x='matches',y='venue', data=venue_df);


# In[93]:


venue_df


# In[95]:


team_wins_ser = ipl_matches['winner'].value_counts()

team_wins_df = pd.DataFrame(columns=["team", "wins"])
for items in team_wins_ser.iteritems():
    temp_df1 = pd.DataFrame({
        'team':[items[0]],
        'wins':[items[1]]
    })
    team_wins_df = team_wins_df.append(temp_df1, ignore_index=True)


# In[96]:


team_wins_df


# In[97]:


plt.title("Total Victories of IPL Teams")
sns.barplot(x='wins', y='team', data=team_wins_df, palette='Paired');


# In[99]:


mvp_ser = ipl_matches['player_of_match'].value_counts()

mvp_ten_df = pd.DataFrame(columns=["player", "wins"])
count = 0
for items in mvp_ser.iteritems():
    if count>9:
        break
    else:
        temp_df2 = pd.DataFrame({
            'player':[items[0]],
            'wins':[items[1]]
        })
        mvp_ten_df = mvp_ten_df.append(temp_df2, ignore_index=True)
        count += 1   


# In[100]:


mvp_ten_df


# In[101]:


plt.title("Top Ten IPL Players")
sns.barplot(x='wins', y='player', data=mvp_ten_df, palette='Paired');


# In[103]:


toss_ser = ipl_matches['toss_winner'].value_counts()

toss_df = pd.DataFrame(columns=["team", "wins"])

for items in toss_ser.iteritems():
    temp_df3 = pd.DataFrame({
        'team':[items[0]],
        'wins':[items[1]]
    })
    toss_df = toss_df.append(temp_df3, ignore_index=True)


# In[104]:


plt.title("How IPL Teams fared in toss?")
sns.barplot(x='wins', y='team', data=toss_df, palette='Paired');


# In[ ]:




