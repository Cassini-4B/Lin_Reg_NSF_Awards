import pandas as pd
import numpy as np
from sklearn.cross_validation import cross_val_score

import pickle 
import statsmodels.api as sm
import statsmodels.formula.api as smf

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Ridge, Lasso
from sklearn import metrics

from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler


import matplotlib.pyplot as plt
import seaborn as sns
% matplotlib inline

def regression_model(pickledfile):
	"""
		This function splits the data into a training and test set, fits data to 
		a linear regression model to a pickled data file and returns 
		RMS error and r-squared score.
	"""
	X = pickledfile[X]
	y = pickeldfile[response_variable]
	
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

	lr = LinearRegression()
	lr.fit(X_train, y_train)
	y_pred_train = lr.predict(X_train)

	y_pred = lr.predict(X_test)

	return ("Training set RMSE:",np.sqrt(metrics.mean_squared_error(y_train, y_pred_train)))
	return ("Training set R2 Score:", metrics.r2_score(y_train, y_pred_train))

	return ("Test set RMSE:",np.sqrt(metrics.mean_squared_error(y_test, yfit)))
	return ("Test set R2 Score:", metrics.r2_score(y_test, yfit))



