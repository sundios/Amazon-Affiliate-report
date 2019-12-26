#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:29:30 2019

@author: konradburchardt
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Importing data set
df = pd.read_excel('Fee-Earnings.xlsx',index_col=False)

#Making row 0 the index. (Data sets come with one row above the header)
df.columns = df.iloc[0]

#dropping row 0 from the list
df = df.drop(df.index[0])

#Selecting Category, Date shipped & Ad Fees 
df = df.iloc[:,[0,5,10]]

#Transforming 'Date Shipped' to YYYY-MM-DD
df['Date Shipped'] = pd.to_datetime(df['Date Shipped']).dt.strftime('%Y/%m/%d')

#Groupping them by Category to see best category
Category = df.groupby(pd.Grouper('Category')).sum()

#reseting index
cat = Category.reset_index()

#plotting Category vs Ad Fees to see what is our best perfoming category for the time frame
plt.bar(cat['Category'], cat['Ad Fees($)'])
plt.xticks(rotation=90)

# Grouping by Dates
dates = df.groupby(pd.Grouper('Date Shipped')).sum()

#reseting index
dates = dates.reset_index()

#dates['Date Shipped'].sort(key=lambda date: datetime.strptime(date, "%d-%b-%y")

plt.plot(dates['Date Shipped'], dates['Ad Fees($)'] ,label="Ad Fees $")
plt.xticks(rotation=45)
plt.xlabel('Dates')
plt.ylabel('Ad Fees $')
plt.title('Ad Fees For December 2019')
plt.legend(loc="upper left")
plt.show()





