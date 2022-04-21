#!/usr/bin/env python
# coding: utf-8

# # An automatically-updating DataWrapper graph using Python and Yahoo finance wrapper

# ## If necessary, we install the necessary libraries

# In[1]:


#pip install datawrapper
#pip install yfinance
#pip install yahoofinancials


# ## We import them
# 

# In[2]:


from datawrapper import Datawrapper
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials


# ## Now we pass our Datawrapper API key to the Datawrapper instance

# In[3]:


dw = Datawrapper(access_token = "IVOkJfFZxTzEi6YyIJTGZDcqw0f4zKT2KT4W36jSPcDqOWcvqTfqrVw28yrQpMO8")
dw.account_info()


# ## Import the dataset we are interested in. In this case, the stokes of gas natural have been chosen

# In[4]:


gas_df = yf.download('NG=F', 
                      start='2021-12-06', 
                      end='2022-04-20', 
                      progress=False,
)
gas_df.head()


# In[5]:


gas_df.tail()


# ## Let's check the price of gas before the Russian invasion

# In[6]:


gas_df.loc["2022-02-24"]


# In[7]:


gas_df.loc["2022-04-19"]


# ## Since the beginning of the conflict, the cost of natural gas has risen by more than 60%.

# In[27]:


ticker = yf.Ticker('NG=F')
gas_df = ticker.history(period="3mo")
gas_df['Close'].plot(title="Natural Gas' stock price")


# ## We create a subset that includes only the closing stocks price

# In[28]:


naturalgas_df=gas_df[["Close"]]
naturalgas_df=naturalgas_df.reset_index(level=0)
naturalgas_df.rename(columns = {'Close':'Stock price'}, inplace = True)
naturalgas_df.head()


# In[29]:


naturalgas_df.tail()


# ## We create our graph using the DataWrapper library.

# In[31]:


gas_chart = dw.create_chart(title = "Natural Gas' stocks", 
chart_type = 'd3-lines', data = naturalgas_df)


# ## The outcome is:

# In[32]:


dw.publish_chart(gas_chart['id'])


# ## We personalise it by inserting the sources and the author's name.

# In[35]:


dw.update_description(
  gas_chart['id'],
  source_name = 'Yahoo Finance',
  source_url = 'https://finance.yahoo.com/quote/NG%3DF/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAMmzAm-FUjfUKdHkrPPFv5lV0BUyskMi6mn7hbK3zUOyfm61si1B_9nnqbLq1AKkTRGWSwIzzqr8WBsqjpt9-T2nUV3dPr1S8H9aLGmwH-fq4SAG1miRGA6zoat0nG1HgBKOTQQomPYQqeE4Ky5Lis0VJwQ5Cnnk_otxJq-tydRt',
  byline = 'Jacopo Cirica',
    intro= 'Since the Russian invasion of Ukraine, the price of gas has risen by more than 60%.',
)


# In[36]:


dw.publish_chart(gas_chart['id'])


# ## Let's change the title

# In[40]:


dw.update_chart(
    gas_chart['id'],
    title='Natural gas stocks skyrocket',
)


# ## We complete the last details and notes in the DataWrapper dashboard.

# In[ ]:




