
import FinanceDataReader as fdr
import yfinance as yf
import pandas as pd
import numpy as np
from IPython.display import display
import datetime

# 한국 주식 전체 정보 -> 매달 1번씩 저장
stocks = fdr.StockListing('KRX') # 코스피, 코스닥, 코넥스 전체
stock_info = stocks[['Code', 'Name', 'Market']]

class financial_report:
    def __init__(self, start_date, end_date, code) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.code = code
    
    # stock_info 데이터 DB에 있음
    def stock_info(self,start_date, end_date, code):
        # if DB에 코드가 없닫면
        ticker = yf.Ticker(code)
 
        stock_df = ticker.history(
               interval='1d',
               start=start_date,
               end=end_date, 
               actions=True,
               auto_adjust=True).reset_index()[["Date", "Open", "High", "Low", "Close", "Volume"]]
        
        stk_finance = ticker.financials
        stk_cashflow = ticker.cash_flow
        stk_info = ticker.info
        # stock_df db에 저장 기
        # elif DB에 코드가 있다면 신규 날짜에 맞춰 업로드
        
        return stock_df, stk_info, stk_finance, stk_cashflow