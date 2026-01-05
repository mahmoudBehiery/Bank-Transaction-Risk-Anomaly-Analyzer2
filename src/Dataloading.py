import pandas as pd

class DataManager:
    def __init__(self,df=None):
        self.df = df

    def load_data(self):
        while True: 
            try:
                path = input("enter the path of the dataset: ")
                self.df = pd.read_csv(path)
                print("Dataset loaded successfully")
                return self.df
            
            except FileNotFoundError:
                print("this path is invalid, please try again")
                
        


    