class ReportGenerator:
    def __init__(self, df):
        self.df = df        

    def generate_reports(self):
       
        flagged_df = self.df[self.df['is_suspicious'] == True]
        flagged_df.to_csv('flagged_transactions.csv', index=False)
        print("flagged_transactions.csv is created successfully")

        
        customer_summary = self.df.groupby('nameOrig').agg({
            'risk_score': 'max',
            'amount': 'sum',
            'trans_count': 'max'
        }).reset_index()

        idx = self.df.groupby('nameOrig')['risk_score'].idxmax()
        bands = self.df.loc[idx, ['nameOrig', 'risk_band']]
        
        customer_summary = customer_summary.merge(bands, on='nameOrig', how='left')
        
        customer_summary.columns = ['Customer_ID', 'Max_Risk_Score', 'Total_amount', 'Transaction_Count', 'Primary_Risk_Band']
        customer_summary.to_csv('customer_risk_summary.csv', index=False)
        print("customer_risk_summary.csv is created successfully")



        self._write_txt_report(flagged_df, customer_summary)
        print("report.txt is created successfully")

    def _write_txt_report(self, flagged_df, customer_summary):
        top_risky = customer_summary.sort_values(by='Max_Risk_Score', ascending=False).head(10)
        
        with open('report.txt', 'w') as f:
            f.write("==========================================\n")
            f.write("      BANK TRANSACTION RISK REPORT        \n")
            f.write("==========================================\n\n")
            
            f.write(f"1. OVERALL STATISTICS:\n")
            f.write(f"- Total Transactions Scanned: {len(self.df)}\n")
            f.write(f"- Suspicious Transactions Found: {len(flagged_df)}\n\n")
            
            f.write(f"2. RISK BAND DISTRIBUTION:\n")
            f.write(self.df['risk_band'].value_counts().to_string())
            f.write("\n\n")
            
            f.write(f"3. TOP 10 RISKY CUSTOMERS:\n")
            f.write(top_risky.to_string(index=False))
            