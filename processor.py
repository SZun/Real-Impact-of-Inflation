# Importing dependencies
import pandas as pd
import datetime
from pathlib import Path

class DF_Processor:
    """
    This class reads, processes and returns both regional and non-regional CSVs as DataFrames from the Data directory.
    The __init__ (constructor) method sets both the regional and non-regional CSV titles as class variables.
    The get_dfs method takes in the is_regional boolean flag and outputs a list of all of the requested DataFrames.
    The process_dfs method takes care of all the necessary DataFrame processing we need to get our data in the right form.
    The get_regional_data method returns a list of the regional DataFrames.
    And the get_non_regional_data returns a list of the non-regional DataFrames.
    """
    
    # Constructor
    def __init__(self):
        # List of non-regional csv titles
        self.non_regional_titles = ['National','Energy','Food', 'National-Less-Food-Energy']
        # List of regional csv titles
        self.regional_titles = ['Midwest', 'Northeast', 'South', 'West']

    # Method to get dataframes
    def get_dfs(self, is_regional):
        # Empty list to hold DataFrames
        dataframes = []
        
        # Setting titles list
        titles = self.regional_titles if is_regional else self.non_regional_titles
        
        # Looping over csv titles list
        for title in titles:
            # Columns to drop
            columns_to_drop = ['HALF1','HALF2']
            
            # If the regional flag is set 
            if is_regional:
                # Append the Annual column
                columns_to_drop.append('Annual')

            # Saving the csv (by title) as DataFrame, dropping un-needed comments, and reshaping using melt
            df = pd.read_csv(Path(f'./Data/{title}.csv')).drop(columns=columns_to_drop).melt(id_vars=['Year'], var_name='Month', value_name='Price')

            # Appending dataframe to dataframes list
            dataframes.append(df)
        
        # Returning all dataframes
        return dataframes

    # Method to data pre-process dataframes
    def process_dfs(self, is_regional):
        # Empty list to hold processed DataFrames
        processed_dataframes = []
        # Dictionary of months and thier numeric values
        months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        # Get and loop over DataFrames
        for df in self.get_dfs(is_regional):
            # Creating Day column and setting values to 1
            df['Day']=1
            # Mapping month from string to int
            df['Month'] = df['Month'].map(months)

            # Creating date column
            df['Date']=pd.to_datetime(dict(year=df.Year, month=df.Month, day=df.Day))
            # Sorting Date values
            df = df.sort_values('Date')
            # Making index Date
            df.index = df['Date']

            # Dropping Year, Month, Day, Date columns
            df = df.drop(columns=['Year','Month','Day','Date'])
            # Dropping NaN values
            df = df.dropna()

            # Adding current DataFrame to processed_dataframes list
            processed_dataframes.append(df)
        #Returning all of the processed dataframes
        return processed_dataframes
    
    # Method to get regional DataFrames
    def get_regional_data(self):
        # Return the processed regional DataFrames
        return self.process_dfs(True)
    
    # Method to get non-regional DataFrames
    def get_non_regional_data(self):
        # Return the processed non-regional DataFrames
        return self.process_dfs(False)
