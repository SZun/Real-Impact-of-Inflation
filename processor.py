import pandas as pd
from pathlib import Path
import datetime

class DF_Processor:
    """
    @TODO Add Description
    """
    
    # Constructor
    def __init__(self,titles,is_regional=False):
        # Save titles
        self.titles = titles
        # Save is_regional
        self.is_regional = is_regional
        
        # Set empty list for processed DataFrames
        self.processed_dataframes = []
        
        # Run dataframe processing method
        self.process_dfs()

    # Method to get dataframes
    def get_dfs(self):
        # Empty list to hold DataFrames
        dataframes = []
        
        # Looping over csv titles list
        for title in self.titles:
            # Columns to drop
            columns_to_drop = ['HALF1','HALF2']
            
            # If the regional set is 
            if self.is_regional:
                # Add the Annual column
                columns_to_drop.append('Annual')

            # Saving the csv (by title) as DataFrame, making Year the index column and dropping the HALF1 and HALF2 columns
            df = pd.read_csv(Path(f'./Data/{title}.csv')).drop(columns=columns_to_drop).melt(id_vars=['Year'], var_name='Month', value_name='Price')

            # Appending dataframe to dataframes list
            dataframes.append(df)
        
        # Returning all dataframes
        return dataframes

    # Method to data pre-process dataframes
    def process_dfs(self):
        # Dictionary of months and thier numeric values
        months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        # Get and loop over DataFrames
        for df in self.get_dfs():
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

            # Adding dataframe to processed_dataframes list
            self.processed_dataframes.append(df)
    
    # Method to return the processed dataframes
    def get_processed_dataframes(self):
        # Return the processed dataframes
        return self.processed_dataframes
