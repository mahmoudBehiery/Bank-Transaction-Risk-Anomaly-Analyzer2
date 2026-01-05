import numpy as np

class RiskScorer:
    def __init__(self, df):
        self.df = df.copy()

    def compute_scores(self):

        group_stats = self.df.groupby('nameOrig')['amount']
        mean = group_stats.transform('mean')
        std = group_stats.transform('std')
        self.df['z_score_personal'] = ((self.df['amount'] - mean) / std).fillna(0)

        global_mean = self.df['amount'].mean()
        global_std = self.df['amount'].std()
        self.df['z_score_global'] = (self.df['amount'] - global_mean) / global_std


        self.df['risk_score'] = (np.maximum(self.df['z_score_personal'].abs(), 
                                            self.df['z_score_global'].abs()) * 20).clip(0, 100)
    
    

        print("Risk scores computed successfully")
        return self.df