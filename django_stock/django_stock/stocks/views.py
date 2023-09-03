from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *
import FinanceDataReader as fdr
import yfinance as yf
import pandas as pd
import numpy as np
from IPython.display import display
import datetime

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

