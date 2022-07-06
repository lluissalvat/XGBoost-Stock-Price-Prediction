# We import the relevant modules
import pandas as pd
import pandas_datareader.data 
import sklearn
import xgboost
from xgboost import XGBRegressor

# We define the 'Dataset' function, which will output a DataFrame and the list of features which will be used to train the model
def Dataset(ticker, start, end, days_list):
  
  # We use the DataReader function to obtain price data from Yahoo Finance of stock 'ticker' from 'start' to 'end'
  df = pandas_datareader.data.DataReader(ticker, 'yahoo', start, end)
  # We eliminate all columns but 'Adj Close', which is the only one we will use
  df = df.drop(['High','Low','Open','Close','Volume'], axis=1)
  
  # We change the name of the column, from 'Adj Close' to 'adjclose'
  df = df.rename(columns={'Adj Close':'adjclose'})
  
  # We initialize the 'features' list, which will contain 'adjclose' and the other independent variables
  features = ['adjclose']
  
  # We iterate over the elements of 'days_list'
  for day in days_list:
    # We create columns named according to and whose values are obtained by shifting the elements of 'days_list'
    df['adjclose_'+str(day)+'d']=df.adjclose.shift(day)
    # We add the name of the new column to 'features'
    features.append('adjclose_'+str(day)+'d')

  # We ensure that there are no indexes with missing values due to the shift to obtain features
  df = df[df['adjclose_'+str(max(days_list))+'d'].notna()]
  # We shift the 'adjclose' value, so that the 'target' of each day is the following day's 'adjclose'
  df['target'] = df.adjclose.shift(-1)
  # We ensure that there are no indexes with missing values due to the shift to obtain the label
  df = df[df['target'].notna()]

  # We output both the dataset and the list of features
  return df, features

# We obtain the dataset and the list of features for some given input variables, feel free to modify them
df, features = Dataset(ticker='AAPL', start='01-01-2000', end='06-07-2022', days_list=[1,2,3,7,14])

# We define the 'XGBoostTimeSeriesForecastingModel', which will save the trained model
def XGBoostTimeSeriesForecastingModel(df, features, label, perc, n_estimators, learning_rate):

  # We define the number threshold to split the 'train' and 'test' subsets
  n = int(len(df)*(1-perc))
  
  # We split the DataFrame into the 'train' subset
  train = df[:n]
  # We split the DataFrame into the 'test' subset
  test = df[n:]

  # We define the training set into the dependent and independent variable
  X_train, y_train = train[features], train[label]
  # We define the testing set into the dependent and independent variable
  X_test, y_test = test[features], test[label]

  # We declare the model we will be employing and set its hyperparameters
  model = XGBRegressor(n_estimators=n_estimators, learning_rate=learning_rate)

  # We fit our model to our training data and define the evaluation set as the training and testing subsets 
  model.fit(X_train, y_train, eval_set=[(X_train, y_train), (X_test, y_test)])
  
  # We save the trained model in a JSON format
  trained_model = model.save_model('XGBoostTimeSeriesForecastingModel.json')
  
  # We download the trained model
  return trained_model

# We call the main function for some values for the hyperparameters, feel free to modify them
XGBoostTimeSeriesForecastingModel(df, features, 'target', perc=0.2, n_estimators=2000, learning_rate=0.1)
