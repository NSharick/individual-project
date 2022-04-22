##Acquire, clean, and prep functions for individual project##

#imports
import pandas as pd


#acquire function
def get_online_retail():
    df = pd.read_excel('Online Retail.xlsx')
    return df

#clean function
def clean_online_retail(df):
    df = df[pd.notnull(df['CustomerID'])]
    df = df[df['Quantity'] > 0]
    return df

#prep function
#def prep_online_retail(df):
    