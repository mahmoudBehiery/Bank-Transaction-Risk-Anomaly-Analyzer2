from src.Dataloading import DataManager
from src.Datacleaning import TransactionCleaner
from src.preparefeatures import FeatureBuilder
from src.risk_scores import RiskScorer
from src.TransactionFlagger import TransactionFlagger
from Reports.generate_report import ReportGenerator


class ConsoleApp:
    def __init__(self):
        self.df = None
        self.cleaned_df = None
        self.features_df = None
        self.scored_df = None
        self.final_df = None


    def run(self):

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
                    self.df = data_manager.load_data()

                elif choice == 2:
                    if self.df is None:
                        print("Please load a dataset first")
                        continue
                    cleaner = TransactionCleaner(self.df)
                    self.cleaned_df = cleaner.clean_data()

                elif choice == 3:
                    if self.cleaned_df is None:
                        print("Please clean the data first")
                        continue
                    feature_builder = FeatureBuilder(self.cleaned_df)
                    self.features_df = feature_builder.build_features()
                
                elif choice == 4:
                    if self.features_df is None:
                        print("please build features first")
                        continue
                    scorer = RiskScorer(self.features_df)
                    self.scored_df = scorer.compute_scores()
                
                elif choice == 5:
                    if self.scored_df is None:
                        print("Compute risk scores first")
                        continue
                    flagger = TransactionFlagger(self.scored_df)
                    self.final_df = flagger.flag_transactions()
        
                elif choice == 6:
                    if self.final_df is None:
                        print("Please complete steps 1-5 first")
                        continue
                    reporter = ReportGenerator(self.final_df)
                    reporter.generate_reports()

                elif choice == 7:
                    if self.final_df is None:
                        print("No data processed yet")
                        continue
                    
                    print("\n    QUICK SYSTEM SUMMARY \n")
                    print(f"Total Transactions : {len(self.final_df)}")
                    print(f"Suspicious Flags   : {self.final_df['is_suspicious'].sum()}")
                    print("-" * 30)
                    print("Risk Distribution:")
                    print(self.final_df['risk_band'].value_counts())

                elif choice == 0:
                    print("Exiting the application")
                    break
                
                else:
                    print("Invalid choice. Please try again")

            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = ConsoleApp()
    app.run()