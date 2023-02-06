import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

WINDOW_SIZE = 30

def get_df(fp):
  df = pd.read_csv(fp)
  df = df.drop(['Date'], axis=1)
  df['Receipt_Count'] = df['Receipt_Count'].astype(float)
  return df

def get_rc(df):
  return np.array([[z] for z in df['Receipt_Count']])

def get_windows(data):
  N = len(data)
  X = []
  y = []

  for i in range(N):
    j = i + WINDOW_SIZE
    if j >= N:
      break

    x_i = data[i:j]
    y_i = data[j]
    X.append(x_i)
    y.append(y_i)

  return np.array(X), np.array(y)

def get_trn_val_tst(data, splits):
  N = len(data)
  trn_idx = np.arange(0, int(N * splits[0]))
  val_idx = np.arange(trn_idx[-1] + 1, trn_idx[-1] + 1 + int(N * splits[1]))
  tst_idx = np.arange(val_idx[-1] + 1, val_idx[-1] + 1 + int(N * splits[2]))

  return data[trn_idx], data[val_idx], data[tst_idx]

def get_trn_scaled(trn_set):
    sc = MinMaxScaler(feature_range = (0, 1))
    trn_set_scaled = sc.fit_transform(trn_set)
    return trn_set_scaled, sc

def get_windows(data, window):
  N = len(data)
  X = []
  y = []

  for i in range(N):
    j = i + window
    if j >= N:
      break

    x_i = [z for z in data[i:j]]
    y_i = data[j]
    X.append(x_i)
    y.append(y_i)

  return np.array(X), np.array(y)