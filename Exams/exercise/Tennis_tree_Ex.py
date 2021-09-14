# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# Deepak Agarwal------>Email:deepakagarwal@gwmail.gwu.edu
# %%%%%%%%%%%%% Date:
# V1 June - 05 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Decision Tree  %%%%%%%%%%%%%%%%%%%%%%%%%%
#%%-----------------------------------------------------------------------
#%%-----------------------------------------------------------------------
# Exercise
#%%-----------------------------------------------------------------------
# 1:
# Build the simple tennis table we just reviewed, in python as a dataframe. Label the columns.
# We are going to calculate entropy manually, but in python.
# Make sure to enter all variables as binary vs. the actual categorical names
# Name the dataframe tennis_ex.
#%%-----------------------------------------------------------------------
import pandas as pd
import numpy as np
import pydotplus
import collections
from math import log, e
from sklearn import tree
from sklearn.model_selection import train_test_split

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# NOTE: QUESTION ASK WAS TO BUILD DATAFRAME, HENCE CREATED DATAFRAME THAN USING pd.read CSV
tennis_ex = pd.DataFrame()
tennis_ex['outlook'] = ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy',
                     'overcast', 'sunny', 'sunny', 'rainy', 'sunny', 'overcast',
                     'overcast', 'rainy']

tennis_ex['temp'] = ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool',
                         'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild']

tennis_ex['humidity'] = ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal',
                      'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high']

tennis_ex['windy'] = ['false', 'true', 'false', 'false', 'false', 'true', 'true',
                   'false', 'false', 'false', 'true', 'true', 'false', 'true']

tennis_ex['play'] = ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes',
                  'yes', 'yes', 'no']

print("Tennis Dataframe: ",'\n', tennis_ex)
print('\n\n')

#df_no_indices = tennis_ex.to_string(index= False)
#print("Tennis Dataframe without index", '\n',df_no_indices)

features = pd.get_dummies(tennis_ex[ ['outlook', 'temp', 'humidity', 'windy'] ])
print(features)
target = tennis_ex['play']

#%%-----------------------------------------------------------------------
# 2:
# Build a function that will calculate entropy. Calculate entropy for the table we just went over
# in the example, but in python
# This is for the first split.
#%%-----------------------------------------------------------------------
new_tennis_data=pd.concat([features, target], axis=1)

def entropy(value_input):
    elements, counts = np.unique(value_input, return_counts = True)
    entropy = np.sum([(-counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
    return entropy

for col_names in features.columns:
    print("\nEntropy for ", col_names, ": ", end='')
    if(new_tennis_data[col_names].dtype=="uint8"):
        test=new_tennis_data[new_tennis_data[col_names]==1]
    if (new_tennis_data[col_names].dtype == "uint8"):
        test = new_tennis_data[new_tennis_data[col_names] == True]
    print(entropy(test["play"]))

#%%-----------------------------------------------------------------------
# 3:
# Run the decision tree algorithm and find out the best feature and graph it.
#%%-----------------------------------------------------------------------
# Importing the required packages
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import tree
#%%-----------------------------------------------------------------------
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
#%%-----------------------------------------------------------------------

# Libraries to display decision tree
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
import webbrowser
#%%--------------------------------Save Console----------------------------

# old_stdout = sys.stdout
# log_file = open("console.txt", "w")
# sys.stdout = log_file

#%%-----------------------------------------------------------------------
train_features, test_features, train_labels, test_labels = train_test_split(features,
                                                                            target,
                                                                            test_size=0.2,
                                                                            random_state=21)
clf = tree.DecisionTreeClassifier()
clf_train = clf.fit(features, target)
print(tree.export_graphviz(clf_train, None))


dot_data = tree.export_graphviz(clf_train,
                                out_file= None,
                                feature_names=list(features.columns.values),
                                class_names=['Not_Play', 'Play'],
                                rounded=True,
                                filled=True)
graph = pydotplus.graph_from_dot_data(dot_data)

graph.write_png('Tennis_tree.png')
graph.write_svg('Tennis_tree.svg')





