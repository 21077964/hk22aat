#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import numpy as np
from typing import Iterable, TypeVar
import matplotlib.pyplot as plt

T = TypeVar('T', pd.DataFrame, pd.DataFrame)

def load_data(filename: str) -> Iterable[T]:
    # load the Csv File
    data = pd.read_csv(filename)
    years_as_col = data.iloc[:, 4:data.shape[1] -1]
    countries_as_col = data.transpose()
    countries_as_col.columns = countries_as_col.iloc[0, :]
    countries_as_col = countries_as_col.iloc[4:, :]
    return countries_as_col, years_as_col


# In[48]:


countries, years = load_data("C:/Users/prana/Desktop/Harish/API_EN.ATM.CO2E.PP.GD.KD_DS2_en_csv_v2_4684991.csv")


# In[49]:


countries.head()


# In[50]:


# perfromance by country: A yearly comparison of the World CO2 Emmission Between, Angola, United Arab Emirates and VietnamA
# Replace Null values with 0
# countries = countries.fillna(0)

performance = countries[["World", "Angola", "United Arab Emirates", "Vietnam"]]
# Yearly comparison for the selected countries with the world
performance.groupby(by='World', group_keys=True, dropna=True).mean()


# In[51]:


pd.pivot_table(
    performance,
    values = None,
    index = 'World',
    columns = ["World", "Angola", "United Arab Emirates", "Vietnam"], 
    aggfunc = {
       'World':  np.mean,
       'Angola': np.mean,
       "United Arab Emirates": np.mean,
       "Vietnam": np.mean
    }, 
    fill_value = None, 
    margins = False, 
    dropna = True, 
    margins_name = 'All', 
    observed = False,
    sort = True
)


# In[52]:


performance.describe()


# In[53]:


ts = performance.iloc[2:performance.shape[0]-1, :]
fig, ((ax1, ax2), (ax3, ax4))= plt.subplots(ncols=2,nrows=2, figsize=(15, 10))
ax1.plot(ts.index, ts["World"])
ax1.set_title("$CO_2$ Emission for the whole World")
x1_ticks = ax1.get_xticklabels()
plt.setp(x1_ticks, rotation=70)

ax2.plot(ts.index, ts["Angola"])
x2_ticks = ax2.get_xticklabels()
plt.setp(x2_ticks, rotation=70)
ax2.set_title("$CO_2$ Emission for Angola")

ax3.plot(ts.index, ts["United Arab Emirates"])
x3_ticks = ax3.get_xticklabels()
plt.setp(x3_ticks, rotation=70)
ax3.set_title("$CO_2$ Emission for United Arab Emirates")

ax4.plot(ts.index, ts["Vietnam"])
x_ticks = ax4.get_xticklabels()
plt.setp(x_ticks, rotation=70)
ax4.set_title("$CO_2$ Emission for Vietnam")

plt.tight_layout()
plt.show()


# In[ ]:

