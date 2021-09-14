# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# Deepak Agarwal------>Email:deepakagarwal@gwmail.gwu.edu
# %%%%%%%%%%%%% Date:
# V1 June - 05 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Decision Tree  %%%%%%%%%%%%%%%%%%%%%%%%%%


import os

# %%-----------------------------------------------------------------------
# Exercise
# %%-----------------------------------------------------------------------
# Specify what are your features and targets. Why this is a classification
# 1- Use the bank banknote dataset.
# 2- Specify what are your features and targets.
# 3- Why this is a classification problem.
# 4- Run the decision tree algorithm.
# 5- Explain your findings and write down a paragraph to explain all the results.
# %%-----------------------------------------------------------------------
import pandas as pd
import numpy as np
import pydotplus
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


# 1- Use the bank banknote dataset.
banknote_datadset = pd.read_csv("data_banknote_authentication.csv")
print('\n\n')

#%%-----------------------------------------------------------------------
# 2- Specify what are your features and targets.
print(banknote_datadset.info())
print('\n')
banknote_datadset.columns = ['Feature_1','Feature_2','Feature_3','Feature_4','Target']
print(banknote_datadset.columns)
print('\n')
dataset_features = banknote_datadset.iloc[:, 0:4].values
dataset_target = banknote_datadset.iloc[:, 4].values
print("Features: ",'\n',dataset_features)
print("Target:",'\n',dataset_target)
#%%-----------------------------------------------------------------------
# 3- Why this is a classification problem.
'''
The variable to be predicted is binary, hence this is a classification problem.
Here we are given some input data and we have to classify the input into one of the several predefined categories. 
'''
#%%-----------------------------------------------------------------------
# 4- Run the decision tree algorithm.
print('\n\n')
train_features, test_features, train_labels, test_labels = train_test_split(dataset_features,
                                                                            dataset_target,
                                                                            test_size=0.2,
                                                                            random_state=21)
print("train_features shape: {}".format(train_features.shape))
print("test_features shape: {}".format(test_features.shape))
print("train_labels shape: {}".format(train_labels.shape))
print("test_labels shape: {}".format(test_labels.shape))
print('\n\n')
clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
clf_train = clf.fit(train_features, train_labels)
from sklearn import tree
print(tree.export_graphviz(clf_train,None))
#%%-----------------------------------------------------------------------
# 5- Explain your findings and write down a paragraph to explain all the results.
#FINDINGS
'''
The dataset contains 1372 records.
It is evident from the output that our dataset has four features: 
feature_1,feature_2,feature_3, feature_4
While the target refers to binary.
'''
#RESULTS
'''
To see the statistical details of the data, the “describe()” function is used, 
which returns the mean, count, standard deviation, quartile information and maximum values for each column.
The best performance is 1 with normalize == True and the F1 score can be interpreted as a weighted average of the 
precision and recall, here F1 score reaches its best value at 1. hence this can be considered as best model
'''
#Staistics
print(banknote_datadset.head)
print(banknote_datadset.describe())
print('\n\n')
# instantiate
dtc = DecisionTreeClassifier()
# fit
dtc.fit(dataset_features, dataset_target)
# predict
target_pred = dtc.predict(test_features)
from sklearn.metrics import  classification_report
from sklearn.metrics import confusion_matrix
print("Classification Report: ",'\n', classification_report(target_pred, test_labels))
print("Confusion Matrix: ", '\n', confusion_matrix(target_pred, test_labels))
