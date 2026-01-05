from Dataloading import DataManager
from Datacleaning import TransactionCleaner
from preparefeatures import FeatureBuilder
from risk_scores import RiskScorer
from TransactionFlagger import TransactionFlagger
from Reports import ReportGenerator


df = None
cleaned_df = None
features_df = None
scored_df = None
final_df = None



while True:
    print("\n=====Bank Transaction=====")
    print ("1. Load dataset")
    print ("2. Clean data")
    print ("3. Build features")
    print ("4. Score customers")
    print ("5. Flag suspicious transactions")
    print ("6. Export reports")
    print ("7. Display summary in console")
    print ("0. Exit application")


    try:

        choice = int(input("\nEnter your choice: "))
       

        if choice == 1:
            data_manager = DataManager()
            df = data_manager.load_data()


        elif choice == 2:
            if df is None:
                print("Please load a dataset first")
                continue

            cleaner = TransactionCleaner(df)
            cleaned_df = cleaner.clean_data()
           

        elif choice == 3:
            if cleaned_df is None:
                print("Please clean the data first")
                continue
            feature_builder = FeatureBuilder(cleaned_df)
            features_df = feature_builder.build_features()


        elif choice == 4:
            if features_df is None:
                print("please build features first")
                continue
            scorer = RiskScorer(features_df)
            scored_df = scorer.compute_scores()


        elif choice == 5:
            if scored_df is None:
                print("Compute risk scores first")
                continue
            flagger = TransactionFlagger(scored_df)
            final_df = flagger.flag_transactions()
    

        elif choice == 6:
            if final_df is None:
                print("Please complete steps 1-5 first")
                continue
            
            reporter = ReportGenerator(final_df)
            reporter.generate_reports()

        elif choice == 7:
            if final_df is None:
                print("No data processed yet")
                continue
                
            print("\n   QUICK SYSTEM SUMMARY \n")
            print(f"Total Transactions : {len(final_df)}")
            print(f"Suspicious Flags   : {final_df['is_suspicious'].sum()}")
            print("-" * 30)
            print("Risk Distribution:")
            print(final_df['risk_band'].value_counts())
            

        

        elif choice == 0:
            print("Exiting the application")
            break
        
    except ValueError :
        print("Invalid choice. Please try again")
        

    
