from datetime import date, datetime, time
import pandas as pd

class HistoryReader:
    def __init__(self, path:str):
        self.path = path
        self.df = pd.DataFrame()
        
    def OpenExcel(self, header=0):
        
        df = pd.read_excel(self.path, header=header)
        
        return df
    
    def CalculateDatetime(self, df, date_name:str, time_name:str):
        
        series = df[[date_name, time_name]].apply(lambda data:  datetime.combine(data[0].date(), data[1]), axis=1)
        
        return series