##Acquire, clean, and prep functions for individual project##

#imports
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#acquire function
def get_online_retail():
    '''
    This function reads the dataset from a locally saved .xlsx file into jupyter notebooks as a 
    pandas dataframe for further wrangling.
    '''
    df = pd.read_excel('Online Retail.xlsx')
    return df

#clean function
def clean_online_retail(df):
    '''
    This function takes in the customer orders dataset and removes any observations without a customer id (target variable)
    and removes any observations where the order quantity is zero or less than zero.
    '''
    #keep only rows with a customer id that is not null
    df = df[pd.notnull(df['CustomerID'])]
    #keep only rows where the order quantity is greater than zero
    df = df[df['Quantity'] > 0]
    return df

#prep function
def feat_eng_online_retail(df):
    '''
    This function takes in the customer order dataset and uses the available data to engineer the features that will be 
    used with the clustering machine learning model. 
    '''
    #use the datetime stamp in the dataset to identify the date of the most recent purchase
    df['last_purchase'] = df['CustomerID'].apply(lambda x: df[df['CustomerID'] == x].InvoiceDate.max())
    #set the variable of 'today' as the most recent entry in the overall dataset for calculating recency
    today = pd.to_datetime('2011-12-10')
    #calculate recency for each customer by subtracting the date of the most recent purchase from the 'today' date
    df['recency'] = df['last_purchase'].apply(lambda x: (today - x).days)
    #calculate the frequency of the customers orders
    df['frequency'] = df['CustomerID'].apply(lambda x: df[df['CustomerID'] == x].size)
    #calculate the sales total by multiplying the item quantity by the item price
    df['sales_total'] = df['Quantity'] * df['UnitPrice']
    #calculate the total monetary value of the cuatomer's orders
    df['monetary'] = df['CustomerID'].apply(lambda x: df[df['CustomerID'] == x].sales_total.sum())
    #calcualte the average order value by customer
    df['average_order_value'] = df['CustomerID'].apply(lambda x: df[df['CustomerID'] == x].sales_total.mean())
    #calculate the average number of items ordered by customer
    df['avg_items_ordered'] = df['CustomerID'].apply(lambda x: df[df['CustomerID'] == x].Quantity.mean())
    #calculate the total number of unique items ordered by customer
    df['unique_items_count'] = df['CustomerID'].apply(lambda x: df[df['CustomerID'] == x].Description.nunique())
    #calculate a distance rating by ranking the customer country's distance from the company country (between 0 and 36)
    df['dist_rating'] = df.Country.map({'United Kingdom': 0, 'EIRE': 1, 'Channel Islands': 2, 'France': 3, 'Belgium': 4,
                                   'Netherlands': 5, 'Germany': 6, 'Switzerland': 7, 'Austria': 8,
                                    'Czech Republic': 9, 'Denmark': 10, 'Italy': 11, 'Spain': 12, 'Norway': 13, 
                                   'Portugal': 14, 'Sweden': 15, 'Poland': 16, 'Lithuania': 17, 'Greece': 18,
                                   'Malta': 19, 'Iceland': 20, 'Finland': 21, 'Cyprus': 22, 'Israel': 23, 
                                    'Lebanon': 24, 'Saudi Arabia': 25, 'Bahrain': 26, 'United Arab Emirates': 27,
                                   'Brazil': 28, 'USA': 29, 'Canada': 30, 'RSA': 31, 'Singapore': 32, 'Japan': 33,
                                   'Australia': 34, 'European Community': 35, 'Unspecified': 36})
    return df

#preparation function for customer grouping
def prep_online_retail(df):
    '''
    This function drops the original columns used to create the engineered columns and then groups the resulting
    dataframe by customer id so each row represents an individual customer.
    '''
    #drop original columns not needed for modeling
    df = df.drop(columns=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'Country',
                          'last_purchase', 'sales_total'])
    #group the dataframe by customer id
    df = df.groupby('CustomerID').max()
    return df
    
#scaling function - prep for clustering
def scale_online_retail(df):
    '''
    This function takes in the prepared dataframe and scales the values with a min-max scaler so that all features
    have equal weight when being used with the clustering model
    '''
    #create the scaler object
    scaler = MinMaxScaler()
    #fit the object with the dataframe
    scaler.fit(df)
    #transform the dataframe with the scaler
    scaled_df = scaler.transform(df)
    #return the dataframe with scaled values
    df = pd.DataFrame(scaled_df, columns=df.columns, index=df.index)
    return df

