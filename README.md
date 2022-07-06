# XGBoost-Stock-Price-Prediction

## Introduction

This script loads desired stock price training data, trains an XGBoost Regressor for Time Series Forecasting (allowing fine-tuning) and downloads the model to be used for prediction tasks. Specifically, it attempts to predict the following day's adjusted close price based on former days' adjusted close prices.

## XGBoost


XGBoost is a scalable end to-end tree boosting system, which is a highly effective and widely used machine learning method [1]. It is a system that outperforms deep learning models (and also requires much less tuning) on classification and regression problems for tabular data across multiple 
datasets [4]. It is for this reason that it is often employed by participants in Kaggle-style data science and machine learning competitions [2].

As an ensemble technique, gradient boosting combines the results of several weak learners, referred to as
base learners, to build a model that performs generally better than the conventional single machine learning models.
Typically, gradient boosting utilizes decision trees as base learners. Like other boosting methods, the core idea of
gradient boosting is that during the learning procedure new models are build and fitted consecutively and not independently, to provide better predictions of the output variable. New base learners are constructed aiming to minimize a loss function, associated with the whole
ensemble. Instances that are not predicted correctly in previous steps and score higher errors are correlated with
larger weight values, so the model can focus on them, and learn from its mistakes [3]. 


## Data Transformation

Most of the data transformation is included as step by step comments in the script. Nevertheless, I shall expand on my feature generation rationale. It is 
widely acknowledge that there exist a miriad of variables that may correlate with or directly influence the price movements of the stock market indices in general and of individual stocks in particular. Some of these variables tend to be of macroeconomical nature, such as inflation (CPI) reports, interest rate hikes, GDP drops, corporate governance changes, lawsuits, quarterly earnings report and more. These stimuli drive retail and institutional investors to make decisions regarding their capital deployment strategy, in essence buying, holding or selling a given security.

## Model Training

## Further Steps


## References


[1] Chen, Tianqi, and Carlos Guestrin. "Xgboost: A scalable tree boosting system." Proceedings of the 22nd acm sigkdd international conference on knowledge discovery and data mining. 2016.

[2] Januschowski, Tim, et al. "Forecasting with trees." International Journal of Forecasting (2021).

[3] Paliari, Iliana, Aikaterini Karanikola, and Sotiris Kotsiantis. "A comparison of the optimized LSTM, XGBOOST and ARIMA in Time Series forecasting." 2021 12th International Conference on Information, Intelligence, Systems & Applications (IISA). IEEE, 2021.

[4] Shwartz-Ziv, Ravid, and Amitai Armon. "Tabular data: Deep learning is not all you need." Information Fusion 81 (2022): 84-90.

## Disclaimer

This material has been prepared for informational purposes only, and is not intended to provide, and should not be relied on for, financial tax, legal or accounting advice. You should consult your own financial, tax, legal and accounting advisors before engaging in any transaction.
