from datetime import date, timedelta
import numpy as np

WINDOW_SIZE = 15

def predict(model, pred_date, rc, sc):
  first_date = date(2021, 1, 1)
  end_date = date(2021, 12, 31)

  end_idx = len(rc)
  pred_idx = (pred_date - first_date).days

  while not (pred_idx == end_idx):
    X = rc[end_idx-WINDOW_SIZE:end_idx]
    print("end_idx", end_idx)
    print(X)
    print()
    X = np.reshape(X, (1, X.shape[0], 1))

    prediction = model.predict(X)
    prediction = sc.inverse_transform(prediction)
    rc = np.append(rc, prediction)

    end_idx += 1

  return rc