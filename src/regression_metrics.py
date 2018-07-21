import pandas as pd
import numpy as np

import pickle 

import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import metrics
from statsmodels.stats.outliers_influence import variance_inflation_factor



def calc_variance_inflation_factor(datafile):
	"""
		This function calculates variance inflation factor (VIF) to determine if there
		is multicollinearity in the data (where one variable can be linearly predicted
		from another, which prevents you from being able to find unique Beta coeffs).
	"""
	
	X = datafile[x]

	vif = pd.DataFrame()
	vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
	vif['features'] = X.columns

	return(vif.round(1))




def residuals_vs_actuals_plot(datafile):
	"""
		This function plots the residuals vs actuals to look at whether the variance
		of the error is constant.  If not, the model might not be linear, or may need
		to be transformed, or may need additional features to determine the 
		relationship between the dependent and independent variables.
	"""
	
	residual = datafile[y] - (ols_fit(datafile[x], datafile[y])
	plt.scatter(datafile[x], residual)	
	return(plt.show)




def ols_fit(X,y):
	"""
		Fit data to Ordinary Least Squares model, generate results
	"""

	results = smf.OLS(y, X).fit()
	y_pred = results.predict(X)

	return y_pred
