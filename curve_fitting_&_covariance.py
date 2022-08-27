# -*- coding: utf-8 -*-
"""Curve_fitting_&_covariance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JN74kL52phNWu8VeAPq3cSF-k4rio2sw
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

#data points 
x_data = np.array([0.        , 0.15789474, 0.31578947, 0.47368421, 0.63157895,
       0.78947368, 0.94736842, 1.10526316, 1.26315789, 1.42105263,
       1.57894737, 1.73684211, 1.89473684, 2.05263158, 2.21052632,
       2.36842105, 2.52631579, 2.68421053, 2.84210526, 3.        ])
y_data = np.array([  2.95258285,   2.49719803,  -2.1984975 ,  -4.88744346,
        -7.41326345,  -8.44574157, -10.01878504, -13.83743553,
       -12.91548145, -15.41149046, -14.93516299, -13.42514157,
       -14.12110495, -17.6412464 , -16.1275509 , -16.11533771,
       -15.66076021, -13.48938865, -11.33918701, -11.70467566])

plt.scatter(x_data,y_data)
plt.show()

#model to be fit with the experimental data
def model_f(x, a, b, c):
    return a*(x-b)**2 + c

popt, pcov = curve_fit(model_f, x_data, y_data, p0=[3,2,-16]) #

popt # which gives the optimal parameters for the model_f given the data

pcov  #the covariance matrix, which gives an estimate of the "error" of the parameters

plt.imshow(np.log(np.abs(pcov)))
plt.colorbar()
plt.show()

a_opt, b_opt, c_opt = popt
x_model = np.linspace(min(x_data), max(x_data), 100)
y_model = model_f(x_model, a_opt, b_opt, c_opt)

plt.scatter(x_data,y_data)
plt.plot(x_model,y_model, color='r')
plt.show()

def fit_f(x, a, b, c, d):
    return a*(x-b)**2 + c + d*0.1*np.cos(x)

popt, pcov = curve_fit(fit_f, x_data, y_data, p0=[1,2,-16,1])

popt

pcov

plt.imshow(np.log(np.abs(pcov)))
plt.colorbar()
plt.show()

a_opt, b_opt, c_opt, d_opt = popt
x_model1 = np.linspace(min(x_data), max(x_data), 1000)
y_model1 = fit_f(x_model, a_opt, b_opt, c_opt, d_opt)

plt.scatter(x_data,y_data)
plt.plot(x_model1,y_model1, color='b')
plt.show()