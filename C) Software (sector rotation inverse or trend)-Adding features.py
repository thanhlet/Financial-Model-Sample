#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to calculate trend or reverse 
def calculate(df,window=1):
    print(window)
    df['buy_hold'] = 100*(df['Close']/df['Close'].shift(1)-1)
    df['reverse'] = (-1)*np.sign(df['buy_hold'].shift(int(window)))*df['buy_hold'] 
    df['trend'] = np.sign(df['buy_hold'].shift(int(window)))*df['buy_hold']
    return df


# In[ ]:


# Cleaning up the method


import tkinter as tk
from tkinter import *

# pip install pillow
from PIL import Image, ImageTk
import yfinance as yf
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
    
root = tk.Tk()
root.wm_title("Tkinter window")

sector_df = pd.read_csv('csv/sector_etf.csv',index_col = 0,encoding = 'latin')
string = ''
for i in sector_df.index[:-1]:
    string+=' '+i+','
string+=' '+sector_df.index[-1]

def plot(df):
    fig = plt.figure(figsize  = (10,5))
    ax = fig.add_subplot(111,label = e1.get())
    ax.plot(df['buy_hold'].cumsum())
    ax.plot(df['reverse'].cumsum(),label = 'reverse',color = 'orange')
    ax.plot(df['trend'].cumsum(),label = 'trend',color = 'green')
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    fig.tight_layout()
    plt.legend(loc = 'upper_left')
    plt.savefig('png/temp.png')
  



def runProgram():
    if time.get().replace(' ','')!='':
        
        df = calculate(yf.download(tickers = e1.get(),start = time.get(),end = datetime.today())[['Close']],window.get())

        plot(df)
        # Loading image
        load = Image.open('png/temp.png')
        render  = ImageTk.PhotoImage(load)
        img = Label(root, image =render)
        img.image = render
        img.grid(row= 0,rowspan = 2,column =  2,sticky = tk.W+tk.E+tk.N+tk.S)
    else:
        df = calculate(yf.download(tickers = e1.get(),start = '2015-01-01',end = datetime.today())[['Close']],window.get())
        plot(df)
        # Loading image
        load = Image.open("png/temp.png")
        render  = ImageTk.PhotoImage(load)
        img = Label(root, image =render)
        img.image = render
        img.grid(row= 0,rowspan = 2,column =  2,sticky = tk.W+tk.E+tk.N+tk.S)
        
def showList():
    root2 = tk.Tk()
    for i in range(len(sector_df)):
        text = tk.Label(root2, text = sector_df.index[i]).grid(row = i,column = 0,sticky = tk.W)
        text = tk.Label(root2, text = sector_df['Name'][sector_df.index[i]]).grid(row = i, column = 1,sticky = tk.W)

    
text = tk.Label(root,text = 'Enter series').grid(row = 0,column= 0)
text = tk.Label(root,text = 'Enter time').grid(row = 1,column = 0)
text = tk.Label(root,text = 'Enter window (int)').grid(row = 2,column = 0)

e1 = tk.Entry(root)

e1.grid(row =0 ,column = 1)  

time = tk.Entry(root)

time.grid(row=1,column = 1)

window = tk.Entry(root)
window.grid(row = 2,column =1)


tk.Button(root, text= 'Run', command  = runProgram,relief = 'raised').grid(row = 5, column  = 1, sticky = tk.W,pady = 4)
tk.Button(root, text= 'Show',command  = showList).grid(row = 5, column  = 0, sticky = tk.W,pady = 4)
tk.mainloop()


# In[ ]:




