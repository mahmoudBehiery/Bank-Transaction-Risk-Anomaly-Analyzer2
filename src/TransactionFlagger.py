import numpy as np

class TransactionFlagger:
    def __init__(self, df):
        self.df = df.copy()

    def flag_transactions(self):
        risk = self.df['risk_score'] >= 80
    
        amount = self.df['amount'] > 500000
    
        type = self.df['type'].isin(['TRANSFER', 'CASH_OUT'])

        self.df['is_suspicious'] = (risk | (amount & type))
    
        self.df['risk_band'] = 'Low'
        self.df.loc[self.df['risk_score'] >= 30, 'risk_band'] = 'Medium'
        self.df.loc[self.df['risk_score'] >= 60, 'risk_band'] = 'High'
        self.df.loc[self.df['amount'] > 500000, 'risk_band'] = 'Critical' 

        
        print("Transactions flagged successfully")
        
        return self.df