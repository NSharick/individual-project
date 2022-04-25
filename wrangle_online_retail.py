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
def prep_online_retail(df):
    df['last_purchase'] = df['CustomerID'].apply(lambda x: df[df['CustomerID'] == x].InvoiceDate.max())
    today = pd.to_datetime('2011-12-10')
    df['recency'] = df['last_purchase'].apply(lambda x: (today - x).days)
    df['frequency'] = df['CustomerID'].apply(lambda x: df[df['CustomerID'] == x].size)
    df['sales_total'] = df['Quantity'] * df['UnitPrice']
    df['monetary'] = df['CustomerID'].apply(lambda x: df[df['CustomerID'] == x].sales_total.sum())
    df['average_order_value'] = df['CustomerID'].apply(lambda x: df[df['CustomerID'] == x].sales_total.mean())
    df['avg_items_ordered'] = df['CustomerID'].apply(lambda x: df[df['CustomerID'] == x].Quantity.mean())
    df['unique_items_count'] = df['CustomerID'].apply(lambda x: df[df['CustomerID'] == x].Description.nunique())
    df['dist_rating'] = df.Country.map({'United Kingdom': 0, 'EIRE': 1, 'Channel Islands': 2, 'France': 3, 'Belgium': 4,
                                   'Netherlands': 5, 'Germany': 6, 'Switzerland': 7, 'Austria': 8,
                                    'Czech Republic': 9, 'Denmark': 10, 'Italy': 11, 'Spain': 12, 'Norway': 13, 
                                   'Portugal': 14, 'Sweden': 15, 'Poland': 16, 'Lithuania': 17, 'Greece': 18,
                                   'Malta': 19, 'Iceland': 20, 'Finland': 21, 'Cyprus': 22, 'Israel': 23, 
                                    'Lebanon': 24, 'Saudi Arabia': 25, 'Bahrain': 26, 'United Arab Emirates': 27,
                                   'Brazil': 28, 'USA': 29, 'Canada': 30, 'RSA': 31, 'Singapore': 32, 'Japan': 33,
                                   'Australia': 34, 'European Community': 35, 'Unspecified': 36})
    return df
