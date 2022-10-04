import pandas as pd
import time
import numpy as np
import mxnet as mx
from mxnet import nd, autograd, gluon
from mxnet.gluon import nn, rnn

import datetime
import seaborn as sns

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

import math

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

import xgboost as xgb
from sklearn.metrics import accuracy_score

context = mx.cpu(); model_ctx=mx.cpu()
mx.random.seed(1719)

dataset_ex_df = pd.read_csv("AmazonStockPriceDataset.csv", header=0, parse_dates=[0], date_parser=parser)

dataset_ex_df[['Date','Open','Close']].head(5)

number_of_days = (dataset_ex_df.shape[0])
year = int(number_of_days / 365)
month = (number_of_days - year *365) % 30
week = int((number_of_days % 365) % 7)
days = (number_of_days % 365) % 7
     
print(f'There are {number_of_days} number of days in the dataset equivalent to {week} weeks ')
print(f'or {year} year/s {month}, months and {days} days ')     