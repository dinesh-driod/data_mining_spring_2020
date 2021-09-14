import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Tumor_data = pd.read_csv("Tumor.csv")
print("Shape: ", '\n', Tumor_data.shape)

print("Statistics: ", '\n', Tumor_data.describe())

print("Headers: ",'\n', Tumor_data.head())

def find_coefficients(x_val,y_val):
    slope = np.sum((x_val-np.average(x_val))*(y_val-np.average(y_val)))/np.sum(np.square((x_val-np.average(x_val))))
    intercept=np.average(y_val)-(slope*np.average(x_val))
    return slope,intercept

d_slope,d_intercept=find_coefficients(Tumor_data["Tumor Size(cm^3)"],Tumor_data[" Weight(grams)"])

print("\nEquation of line: Y = ",d_slope," * X + ",d_intercept)
print("\nSlope: ",d_slope,"\nIntercept: ",d_intercept)
x_actual = Tumor_data["Tumor Size(cm^3)"]
x=np.linspace(np.min(x_actual)-100,np.max(x_actual)+100,1000)
y_pred = d_slope*x + d_intercept
y_actual = Tumor_data[" Weight(grams)"]

plt.plot(x, y_pred, '-g',label="Regression Line")
plt.scatter(Tumor_data["Tumor Size(cm^3)"],Tumor_data[" Weight(grams)"],c="red",marker=".",label="Scatter Plot")
plt.title('Graph')
plt.xlabel("Tumor Sizer"r"$(cm^3)$")
plt.ylabel("Weight(grams)")
plt.legend()
plt.show()