from preprocess import get_df, get_rc, get_trn_val_tst, get_trn_scaled, WINDOW_SIZE, get_windows

import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

def train_model(X_trn, y_trn):
    model = Sequential()
    model.add(LSTM(units = 50, return_sequences = True, input_shape = (X_trn.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units = 50, return_sequences = True))
    model.add(Dropout(0.2))
    model.add(LSTM(units = 50, return_sequences = True))
    model.add(Dropout(0.2))
    model.add(LSTM(units = 50))
    model.add(Dropout(0.2))
    model.add(Dense(units = 1))
    model.compile(optimizer = 'adam', loss = 'mean_squared_error')
    
    model.fit(X_trn, y_trn, epochs = 100, batch_size = 32)

    return model

def main():
    df = get_df('data/raw.csv')
    rc = get_rc(df)
    trn_set, val_set, tst_set = get_trn_val_tst(rc, (0.7, 0.2, 0.1))
    trn_set_scaled, sc = get_trn_scaled(trn_set)
    X_trn, y_trn = get_windows(trn_set_scaled, WINDOW_SIZE)
    X_trn = np.reshape(X_trn, (X_trn.shape[0], X_trn.shape[1], 1))
    model = train_model(X_trn, y_trn)
    model.save('saved_models/model')

if __name__ == "__main__":
    main()