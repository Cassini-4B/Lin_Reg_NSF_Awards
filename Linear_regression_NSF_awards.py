import os
import glob
from collections import Counter
import re
import pickle
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Ridge, Lasso
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns
% matplotlib inline

import parse_xml.py 
import data_clean.py
import linear_regression.py 
import regression_metrics.py
import log_transformation.py



# 1) After downloading xml files: parse data

for folder in directory:
	parse_xml.parse_xml(folder)

#2) Separate big list of data (1 row, N^N columns) into individual rows per xml file
parse_xml.separate_records(listofdata)

#3) Clean data
data_clean.py

#4) Run Linear Regression model on data
linear_regression.regression_model(datafile)

#5) Run model diagnostics
regression_metrics.calc_variance_inflation_factor(datafile)

#6) Plot residuals vs actuals
regression_metrics.ols_fit(data[x], data[y])
regression_metrics.residuals_vs_actuals_plot(datafile)

#7) Transform y variable into ln(y)
log_transformation.log_transform_response_variable(datafile)


