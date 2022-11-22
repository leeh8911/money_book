from datetime import date, datetime, time
import pandas as pd

from history_reader import HistoryReader
from payment import Payment

class KBHistoryReader(HistoryReader):
    def __init__(self, path:str):
        super().__init__(path)
        
        self.df = super().OpenExcel(header=6)
        
        self.df['이용일'] = pd.to_datetime(self.df['이용일'])
        self.df['이용\n시간'] = pd.to_datetime(self.df['이용\n시간']).apply(lambda t: t.to_pydatetime().time())

        self.df['승인시각'] = super().CalculateDatetime(self.df, '이용일', '이용\n시간')
        self.df.dropna(axis=1, inplace=True)
        
        self.df['이용금액'] = self.df['국내이용금액\n(원)'] + self.df['해외이용금액\n($)'] - self.df['할인금액']
        
        self.df = self.df[['승인시각', '이용하신곳', '이용금액']]
        self.df['Payment'] = Payment.KB
        
if __name__ == "__main__":
    KB_CARD_PATH = "data/kbcard/"
    
    kb_reader = KBHistoryReader(KB_CARD_PATH + "카드이용내역_20221001_20221031.xls")
    
    print(kb_reader.df.shape)
    print(kb_reader.df.keys())
    print(kb_reader.df.head())
    print(kb_reader.df.tail())