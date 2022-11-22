from enum import Enum
from datetime import datetime, date
from datetime import timedelta
import csv
import openpyxl

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from history_reader import HistoryReader
from payment import Payment

    
class HyundaiCardParam:
    def __init__(self):
        self.header_index = 2
        self.last_row = -2
        
class HyundaiHistoryReader(HistoryReader):
    def __init__(self, path:str, param):
        super().__init__(path)
        
        self.df = super().OpenExcel(header=param.header_index)
        
        self.df = self.df.iloc[:param.last_row, :]
        
        self.df['승인시간'] = super().CalculateDatetime(self.df, '승인일', '승인시각')
        
        print(self.df.keys())
        self.df = self.df[['승인시간', '가맹점명', '승인금액']]
        self.df['카드종류'] = Payment.Hyundai
        
        
        
        
if __name__ == "__main__":
    HYUNDAI_CARD_PATH = "data/hyundaicard/"
    
    hyundai_reader = HyundaiHistoryReader(HYUNDAI_CARD_PATH + "/hyundaicard_20221122.xlsx", HyundaiCardParam())
    
    print(hyundai_reader.df.shape)
    print(hyundai_reader.df.keys())
    print(hyundai_reader.df.head())
    print(hyundai_reader.df.tail())