import pandas as pd
from pathlib import Path
import datetime

class DF_Processor:
    """
    @TODO Add Description
    """
    
    # Constructor
    def __init__(self):
        # Save titles
        # List of non-regional csv titles
        self.non_regional_titles = ['National','Energy','Food', 'National-Less-Food-Energy']
        # List of regional csv titles
        self.regional_titles = ['Midwest', 'Northeast', 'South', 'West']

    # Method to get dataframes
    def get_dfs(self, is_regional):
        # Empty list to hold DataFrames
        dataframes = []
        
        titles = self.regional_titles if is_regional else self.non_regional_titles
        
        # Looping over csv titles list
        for title in titles:
            # Columns to drop
            columns_to_drop = ['HALF1','HALF2']
            
            # If the regional set is 
            if is_regional:
                # Add the Annual column
                columns_to_drop.append('Annual')

            # Saving the csv (by title) as DataFrame, making Year the index column and dropping the HALF1 and HALF2 columns
            df = pd.read_csv(Path(f'./Data/{title}.csv')).drop(columns=columns_to_drop).melt(id_vars=['Year'], var_name='Month', value_name='Price')

            # Appending dataframe to dataframes list
            dataframes.append(df)
        
        # Returning all dataframes
        return dataframes

    # Method to data pre-process dataframes
    def process_dfs(self, is_regional):
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
            df = df.dropna(is_regional)

            # Adding dataframe to processed_dataframes list
            processed_dataframes.append(df)
        return processed_dataframes
    
    # Method to return the processed dataframes
    def get_regional_data(self):
        # Return the processed dataframes
        return self.process_dfs(True)
    
    # Method to return the processed dataframes
    def get_non_regional_data(self):
        # Return the processed dataframes
        return self.process_dfs(False)
