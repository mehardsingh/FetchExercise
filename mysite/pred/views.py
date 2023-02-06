from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import json
from django.contrib.auth.models import User #####
from django.http import JsonResponse , HttpResponse ####

# import tensorflow as tf
# from tensorflow import keras 
from keras.models import load_model

from pred.pred_helpers.preprocess import *
from pred.pred_helpers.prediction import predict

from datetime import date, timedelta, datetime
# from matplotlib import pyplot as plt

# with open('model_architecture.json', 'r') as json_file:
#     model = model_from_json(json_file.read())

# from wiki.summarize import summarize as sm

model = None

df = get_df('../../FetchExercise/data/raw.csv')
rc = get_rc(df)
trn_set, val_set, tst_set = get_trn_val_tst(rc, (0.7, 0.2, 0.1))
trn_set_scaled, sc = get_trn_scaled(trn_set)

def index(request):
    return HttpResponse("Hello, world. You're at the pred index.")


# https://pypi.org/project/wikipedia/#description
def get_pred(request, model=model, rc=rc, sc=sc):
    date_input = request.GET.get('date', None)
    date_input = datetime.strptime(date_input, '%Y-%m-%d').date()

    if model == None:
        model = load_model('pred/saved_models/model1')

    # print(model.summary())
    
    print(date_input)
    rc_new = predict(model, date_input, rc, sc)
    print(rc_new)
    prediction = rc_new[-1]
    print("pred",  prediction)
    print("rc_new shape",  rc_new.shape)
    # plt.plot(rc, np.arange(0, len(rc)))
    # plt.title("Predicted Receipt Count")
    # plt.xlabel("Days since 1-1-2021")
    # plt.xlabel("Receipt Count")
    # plt.savefig('fig.png')

    # print("here")
    # print(prediction.shape, rc.shape)
    rc_new = rc_new.tolist()
    data = {'pred': str(prediction), 'all': rc_new}

    return JsonResponse(data, safe=False)