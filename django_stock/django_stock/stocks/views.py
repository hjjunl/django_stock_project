from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *
import FinanceDataReader as fdr
import yfinance as yf
import pandas as pd
import numpy as np
from IPython.display import display
import datetime
import schedule
import time
from sqlalchemy import create_engine
import pymysql
# pymysql db설정
db = pymysql.connect(
    host="127.0.0.1",  # DATABASE_HOST
    port=3306,
    user="root",  # DATABASE_USERNAME
    passwd="2000",  # DATABASE_PASSWORD
    db="stock_db",  # DATABASE_NAME
    charset='utf8'
)

# 메인 dashboard
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")


# search를 하면 자동으로 DB에 찾아본 종목이 저장
# def search_site(request, stock_cd):
#     # stock info 데이터 받아오고
#     stk_cd = get_object_or_404(StockInfo, pk=stock_cd)
#     try:
#         search_stock = stk_cd.choice_set.get(pk=request.POST) 
#     if stk_cd in 
#     ticker = yf.Ticker(stk_cd)

#     return render(request, )

# 매일 한국 주식데이터 업데이트 kospi, kosdaq
def update_kor_stock():
    engine = create_engine("mysql+pymysql://root:"+"2000"+"@127.0.0.1" + "/stock_db")
    conn = engine.connect()
    # 한국 주식 전체 정보 -> 매달 1번씩 저장
    stock_info = fdr.StockListing('KRX')[['Code', 'Name', 'Market']] # 코스피, 코스닥, 코넥스 전체
    stock_info = stock_info[stock_info['Market']!="KONEX"]
    # DB format에 맞게 조절
    stock_info.rename(columns={"Code": "stk_cd", "Name" : "stk_name", "Market" : "stk_market"}, inplace=True)
    kor_stock_id = []
    stock_info = stock_info.reset_index(drop=True)
    for i in range(len(stock_info)):
        if stock_info['stk_market'].loc[i]=='KOSPI':
            kor_stock_id.append(stock_info['stk_cd'].loc[i] + '.KS')
        if 'KOSDAQ' in stock_info['stk_market'].loc[i]:
            kor_stock_id.append(stock_info['stk_cd'].loc[i] + '.KQ')
    stock_info['stk_id'] = kor_stock_id
    stock_info.to_sql(name='kor_stock', con=engine, if_exists='replace', index=False)
    conn.close()

# 매일 10:30 에 실행
schedule.every().day.at("10:30").do(update_kor_stock)
while True:
    schedule.run_pending()
    time.sleep(1)