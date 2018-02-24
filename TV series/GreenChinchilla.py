# -*- coding: utf-8 -*-
"""
Spirit Animal User ID: GreenChinchilla
Date the file was last edited: Feb 8, 2018
Challenge Number: 2

Source for converting values to log Paul
"""
#importing all required libraries
from __future__ import division
from collections import defaultdict
import matplotlib.pyplot as mplot
import pandas as pd
import numpy as np 
import re

#creating required variables
import os
global valuesdict
valuesdict={}

#importing data in dataframe
names = pd.read_csv('sentiment_lex_header.csv',header=None)
df = pd.read_csv('sentiment_lex.csv',header=None)
df.columns = names.iloc[0].tolist()

#creating dictionary of lexicons
values = df.values.tolist()
mydict = dict(values)



#file read function adding count values to the value dictionary 
def fileread(files):

    data=open(files, "r")
    data=data.read()
    data =  data.strip()
    data=re.sub(r'\W+', " ", data)
    data=data.split(" ")
    for word in data:
        if word in data:
    
            try:
                valuesdict[word]+=1
             
            except:
                valuesdict[word]=1       
                
# calculate plot function plot log base 10 values
def calculateplot():
    logvalues = [0,0,0,0,0]
    for word,value in valuesdict.items():
        if word in mydict:
            if mydict[word]>=-1.0 and mydict[word]<-0.6:
                logvalues[0] += value
            elif mydict[word]>=-0.6 and mydict[word]<-0.2:
                logvalues[1] += value
            elif mydict[word]>=-0.2 and mydict[word]<=0.2:
                logvalues[2] += value
            elif mydict[word]>0.2 and mydict[word]<=0.6:
                logvalues[3] += value
            elif mydict[word]>0.6 and mydict[word]<=1.0:
                logvalues[4] += value
    logvalues =  np.log10(logvalues)
    return logvalues

#original code for checking the difference
#scaning folder for series files
y = raw_input("Please enter the series you want to watch if a or b?")
for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith('.txt') and file.startswith("a") and y=='a':
            fileread(file)
        elif file.endswith('.txt') and file.startswith("b") and y=='b':
            fileread(file)            

#plotting values                
logvalues = calculateplot()
xtixs = ['Neg','WNeg','Neutral','WPos','Pos']
yvalues = np.arange(len(xtixs))
mplot.bar(yvalues, logvalues)
mplot.xticks(yvalues,xtixs)
#    mplot.xticks(range(0, len(keys)), keys)
mplot.xlabel("Sentiment")
mplot.ylabel("Log word count")
mplot.title("Sentiment analysis of asked series")
mplot.show()
