import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# %%============================================================================================================
# Q1: Read the data of the weather. What are the features in this data set.
# %%------------------------------------------------------------------------------------------------------------
from sklearn.tree import DecisionTreeClassifier

weather_data = pd.read_csv("weather.csv")
print('\n\n')
print(weather_data.columns)

# Q2: Check is there any null values in the dataset or not? Print samples of them
# %%------------------------------------------------------------------------------------------------------------
print('\n\n')
print(weather_data.isnull().any().any())
print('\n')
print(weather_data.isnull().sum())
# Q3: Please do any cleaning you think is needed for this dataset.
# This is up to you which method to use and what kind of method you choose.
# Make sure you clean this set in a way that you can use the clean set for modeling purposes.
# %%------------------------------------------------------------------------------------------------------------

print(weather_data[weather_data.isnull().any(axis = 1)])
del weather_data['number']
print(weather_data.columns)

before_rows = weather_data.shape[0]
print(before_rows)
weather_data = weather_data.dropna()
after_rows = weather_data.shape[0]
print(after_rows)
print("Dropped Rows: ")
print(before_rows - after_rows)

# Q4: Filter the values which contains more than 24.99 relative humidity at 3pm.
# Create a high_humidity_label column that contains 0 and 1.
# anything greater than 24.99 consider as 1 else 0
# %%------------------------------------------------------------------------------------------------------------
pre_processed = weather_data.copy()
pre_processed['high_humidity_label'] = (pre_processed['relative_humidity_3pm'] > 24.99) * 1
print(pre_processed['high_humidity_label'])
pre_processed['relative_humidity_3pm'].head()


# Q5: Store all the Morning features other than Humidity at 3 pm in the morning feature
# Use 9am Sensor Signals as Features to Predict Humidity at 3pm
# %%------------------------------------------------------------------------------------------------------------
morning_features=[ 'air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am',
       'avg_wind_speed_9am', 'max_wind_direction_9am', 'max_wind_speed_9am',
       'rain_accumulation_9am', 'rain_duration_9am', 'relative_humidity_9am']

time = '9am'
features = list(pre_processed.columns[pre_processed.columns.str.contains(time)])
features.remove('relative_humidity_9am')
print(features)


# Q6: Copying the values from the clean_data dataset to new dataset x which only consist of the Morning Feature Data
# Hint: use a copy command in pandas
# %%------------------------------------------------------------------------------------------------------------

X = pre_processed[features].copy()
y = pre_processed[['high_humidity_label']].copy()


# Q7: Perform Test and Train split . USe 20 percent for test set and use random state of 1
# %%------------------------------------------------------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

# Q8: USe SVM to train the data.
# Use different SVM classifier and use can use different hyper parameters.
# %%------------------------------------------------------------------------------------------------------------

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
#Linear SVM
from sklearn.svm import SVC
classifier = SVC(kernel='linear', random_state = 0)
classifier.fit(X_train, y_train.values.ravel())
#Non-Linear SVM
classifier = SVC(kernel='rbf', random_state = 0)
classifier.fit(X_train, y_train.values.ravel())


# Q9: Validate your model on the test data.
# %%------------------------------------------------------------------------------------------------------------

DT = DecisionTreeClassifier(max_leaf_nodes = 10, random_state = 0)
DT.fit(X_train, y_train)
predictions = DT.predict(X_test)

# Q10: Calculate the accuracy, f1 score and confusion matrix.
# Please explain yur results carefully (what is accuracy, and f1 score means) interpret that results into words.
# Is this model performing well? Hint: Can we trust this model to predict the labels.
# Can you improve the results by using different pre processing methods. If yes, how? Change it and show the results.
#

# %%------------------------------------------------------------------------------------------------------------
accuracy_score(y_true=y_test,y_pred = predictions)
print("Classification Report: ",'\n', classification_report(y_test, predictions))
print("Confusion Matrix: ", '\n', confusion_matrix(y_test, predictions))
#Staistics
print(weather_data.head)
print(weather_data.describe())
print('\n\n')
'''
To see the statistical details of the data, the “describe()” function is used, 
which returns the mean, count, standard deviation, quartile information and maximum values for each column.
The best performance is 1 with normalize == True and the F1 score can be interpreted as a weighted average of the 
precision and recall, here F1 score reaches its best value at .80. hence this can be considered as good model with an  
accuracy of 81 % and 19 % loss.
'''


