# %% 1-Download the 2018_cen zip file from Blackboard. unzip the zip file by using zipfile package.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q1" + 20* "-")
import zipfile
import os
import pandas as pd

# %% 2- Use os package of python and create a data directory and extract all the files from zip file to the data directory.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q2" + 20* "-")
print(os.getcwd())
try:
    os.mkdir(os.getcwd() +'/'+ 'data')
except:
    print('direcory is created.')

with zipfile.ZipFile("2018_cen.zip","w") as zip_ref:
    zip_ref.extractall(os.getcwd() +'/'+ 'data')

# %% 3- Read all the csv files and search for the csv file which has "Sex" as coloumn header.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q3" + 20* "-")
list_that_has_sex_as_columns, error_list_sex = [], []
os.chdir(os.getcwd() + '/' + 'data' + '/')

for x in [i for i in os.listdir() if i[-4:]==".csv"]:
    try:
        df = pd.read_csv( x)
        if "Sex" in df.keys():
            list_that_has_sex_as_columns.append(x)
    except:
        error_list_sex.append(x)
# %% 4- Find about all Male population counts in  part 3.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q4" + 20* "-")
print(list_that_has_sex_as_columns)
print(error_list_sex)

df1 = pd.read_csv(list_that_has_sex_as_columns[0])
print(df1.head())
print(df1.iloc[0,:])

# %% 5- Read all the csv files and search for the csv file which has "Occupation" as coloumn header.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q5" + 20* "-")

list_that_has_Occupationas_columns, error_list_Occupation = [], []
for x in [i for i in os.listdir() if i[-4:]==".csv"]:
    try:
        df = pd.read_csv( x)
        if "Occupation" in df.keys():
            list_that_has_Occupationas_columns.append(x)
    except:
        error_list_Occupation.append(x)

print(list_that_has_Occupationas_columns)
print(error_list_Occupation)

# %% 6- Find all Occupations and list it in  part 5.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q6" + 20* "-")
df2 = pd.read_csv(list_that_has_Occupationas_columns[0])
print(df2['Occupation'].values)



