# FetchExercise

## Run Server

Go into the mysite directory and run the command

`python manage.py runserver`

## Chrome Extension

Go onto your Chrome browser and go to the extension management page.

Click "Load Unpacked" and select the `extension` folder

## Get Predictions

Simply click on the Chrome extension, add a date, and a prediction for the ReceiptCount should appear as a notification!

# Backend

The predictions work by using an LSTM-based time-series predictor. Tensorflow and Keras are some tools that were used.
