import pandas as pd

class TransactionCleaner:
    def __init__(self,df):
        self.df = df

    def clean_data(self):
        self.df = self.df.dropna()  
        self.df = self.df.drop_duplicates()
        self.df = self.df[self.df['amount'] > 0]

        if 'step' in self.df.columns:
            self.df['timetransaction'] = pd.to_datetime(self.df['step'], unit='h', origin='2020-01-01')

        
        print("Data cleaned successfully")
        return self.df