class FeatureBuilder:
    def __init__(self, df):
        self.df = df.copy()

    def build_features(self):

        customer_stats = self.df.groupby('nameOrig')['amount'].agg([('trans_count', 'count'),
            ('total_amount', 'sum'),
            ('avg_amount', 'mean'),
            ('max_amount', 'max')]).reset_index()
        
        self.df = self.df.merge(customer_stats, on='nameOrig', how='left')

        self.df['date'] = self.df['timetransaction'].dt.normalize()
        self.df['daily_velocity'] =self.df.groupby(['nameOrig', 'date'])['amount'].transform('sum')


        print("features built successfully")
        

        return self.df