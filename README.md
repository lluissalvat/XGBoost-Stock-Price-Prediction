# XGBoost-Stock-Price-Prediction

## Introduction

This script loads desired stock price training data, trains an XGBoost Regressor for Time Series Forecasting (allowing fine-tuning) and downloads the model to be used for prediction tasks. Specifically, it attempts to predict the following day's adjusted close price based on former days' adjusted close prices.

## XGBoost


XGBoost is a scalable end to-end tree boosting system, which is a highly effective and widely used machine learning method [1]. It is a system that outperforms deep learning models (and also requires much less tuning) on classification and regression problems for tabular data across multiple 
datasets [4]. It is for this reason that it is often employed by participants in Kaggle-style data science and machine learning competitions [2]. XGBoost has been frequently used in the literature to forecast financial time series, such as [5], [6] and [7], in which stock prices, stock market volatility and crude oil prices are predicted, respectively.

As an ensemble technique, gradient boosting combines the results of several weak learners, referred to as
base learners, to build a model that performs generally better than the conventional single machine learning models.
Typically, gradient boosting utilizes decision trees as base learners. Like other boosting methods, the core idea of
gradient boosting is that during the learning procedure new models are build and fitted consecutively and not independently, to provide better predictions of the output variable. New base learners are constructed aiming to minimize a loss function, associated with the whole
ensemble. Instances that are not predicted correctly in previous steps and score higher errors are correlated with
larger weight values, so the model can focus on them, and learn from its mistakes [3]. 


## Data Transformation

Most of the data transformation is included as step by step comments in the script. Nevertheless, I shall expand on my feature generation rationale. It is 
widely acknowledged that there exist a miriad of variables that may correlate with or directly influence the price movements of the stock market indices in general and of individual stocks in particular. Most of these variables tend to be of macroeconomical nature, such as inflation (CPI) reports, interest rate hikes, GDP drops, corporate governance changes, lawsuits, quarterly earnings and more. These stimuli drive retail and institutional investors to make decisions regarding their capital deployment strategy, in essence buying, holding or selling a given security; ultimately resulting in price movements.

While other variables are often employed to predict stock prices, I wanted to follow an alternative approach and observe if past prices could be useful features to perform said predictions, and that's what I have done in this script. I wanted to train a model to predict the next day's closing price so that the user or an automated algorithm could wake up, compute the prediction and, if it is higher that the open price minus slippage, open a long position on the security at hand and sell before close. Obviously, this strategy would have to be thoroughly backtested to ensure it has a positive expectancy (see Further Steps). Regarding the dataset, the label is the next day's adjusted close price, while the features are the given day's adjusted close price and the adjusted close of 2, 3, 5 and 10 days before that (the last two in an attempt to capture some weekly periodicity).

## Model Training

The model training is straightforward. I started by performing a train-test split of the dataset, the percentages of which are easily modifiable and I then split them again into dependent (X) and independent (y) variable subsets. The interesting part is when I declare the model by setting `model=XGBRegressor(n_estimators, learning_rate)`. I omitted the rest of hyperparameters since the default ones already provide decent performance. The number of estimators, `n_estimators`, is the number of trees to fit. I then proceeded to fit the model to the training data, using both the training and the testing set as the evaluation sets and the root mean squared error (RMSE) as the default loss function, which was trivially lower in the training set. Finally, I save the trained model in a JSON format.

## Further Steps

This is a really interesting project upon which I plan to expand, given that it combines a lot of the topics I'm interested in and that it is central in my career aspirations as a Quantitative Researcher. As far as ways to expand on the project, there's a very clear pipeline, namely using the `load_model` function to use the model to generate some predictions and some data visualisation of the actual and predicted values, and designing the logic of the aforementioned trading strategy (and try to improve upon it) in order to backtest it and evaluate its feasibility for different parameters (Part 4 of 'Active Portfolio Management' by Grinold and Kahn may be a good resource). Finally, assuming the backtesting and parameter optimization process yields satisfactory results, the last step would be to deploy it in an automated fashion employing the Interactive Brokers Trader Workstation API.

## References


[1] Chen, Tianqi, and Carlos Guestrin. "Xgboost: A scalable tree boosting system." Proceedings of the 22nd acm sigkdd international conference on knowledge discovery and data mining. 2016.

[2] Januschowski, Tim, et al. "Forecasting with trees." International Journal of Forecasting (2021).

[3] Paliari, Iliana, Aikaterini Karanikola, and Sotiris Kotsiantis. "A comparison of the optimized LSTM, XGBOOST and ARIMA in Time Series forecasting." 2021 12th International Conference on Information, Intelligence, Systems & Applications (IISA). IEEE, 2021.

[4] Shwartz-Ziv, Ravid, and Amitai Armon. "Tabular data: Deep learning is not all you need." Information Fusion 81 (2022): 84-90.

[5] Vuong, Pham Hoang, et al. "Stock-price forecasting based on XGBoost and LSTM." Computer Systems Science and Engineering 40.1 (2022): 237-246.

[6] Wang, Yan, and Yuankai Guo. "Forecasting method of stock market volatility in time series data based on mixed model of ARIMA and XGBoost." China Communications 17.3 (2020): 205-221.

[7] Zhou, Yingrui, et al. "A CEEMDAN and XGBOOST-based approach to forecast crude oil prices." Complexity 2019 (2019).

## Disclaimer

This material has been prepared for informational purposes only, and is not intended to provide, and should not be relied on for, financial tax, legal or accounting advice. You should consult your own financial, tax, legal and accounting advisors before engaging in any transaction.
