import pandas as pd
import numpy as np
import pickle 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns
% matplotlib inline


def log_transform_response_variable(dataframe):
	"""
		This function adds one to every element in y (to avoid divide by zero errors) and 
	takes the log of every element.

	"""

	dataframe[y_1]=dataframe[y].apply(lambda x: x+1)
	dataframe[y_log]=dataframe[y_1].apply(lambda x:np.log(x))

	return (dataframe[y_log])

