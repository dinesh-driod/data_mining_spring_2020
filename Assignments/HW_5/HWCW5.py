import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

chipotle = pd.read_csv('Data2.txt', sep='\t')
print(chipotle[:6])
print("6th Observation: ", list(chipotle.iloc[6]))
# iv. Clean the item price column and change it in a float data type then reassign the
# column with the cleaned prices.
chipotle['item_price'] = chipotle['item_price'].str.replace('$', '')
chipotle['item_price'] = chipotle['item_price'].astype(float)
print(chipotle.item_price)
# v. Remove the duplicates in item name and quantity.
chipotle = chipotle.drop_duplicates(['item_name', 'quantity'])
# # vi. Find only the products with quantity equals to 1 and find item price that greater that 10.
print(chipotle[(chipotle.quantity == 1) & (chipotle.item_price > 10)])
# # vii. Find the price of each item.
print(chipotle.reindex(columns=['item_name', 'item_price']))
# # viii. Sort by the name of the item.
print(chipotle.sort_values('item_name'))
# # ix. find the most expensive item ordered.
print(chipotle.sort_values('item_price', ascending=False).head(1))
# # x. Find the frequency of times were a Veggie Salad Bowl ordered.
print(len(chipotle[chipotle.item_name == 'Veggie Salad Bowl']))
# # xi. How many times people ordered more than one Canned Soda?
print(len(chipotle[(chipotle.item_name == 'Canned Soda') & (chipotle.quantity > 1)]))

Food = pd.read_csv('Food.tsv', sep='\t', low_memory=False)
# iii. Print the size of the data frame and the 6 observation of it.
print("Size of Dataframe: ", Food.size)
print("First 6 Observations: ", Food[:6])
print("6th Observation: ", list(Food.iloc[6]))
# iv. How many columns this dataset has and print the name of all the columns. v. What is
# the name and data type of 105th column?
print("Number of columns in Food Dataset: ", len(Food.columns))
print("Name of columns in Food Dataset: ", list(Food.columns))
print("Column 105 Name: ", Food.columns[105])
print("Data Type of Column Number 105: ", Food.dtypes[Food.columns[105]])
# vi. What are the indices of this dataset. How they are shaped and ordered.
print(Food.index)
# vii. What is the name of product of 100th observation.
print("Name of Product of 100th Observation: ", Food.product_name[100])

users = pd.read_table('data.txt', sep='|')
print("First 6 Observations: " '\n', users[:6])
print("6th Observation: ", list(users.iloc[6]))

# iv. Find what is the mean age for occupation.
print("Mean Age per Occupation: " "\n", users.groupby('occupation').age.mean())

# v. Find the male ratio for occupation and sort it from the most to the least.

ratio = users.pivot_table(index='occupation', columns='gender', aggfunc='size', fill_value=0)
calc = ratio[['F', 'M']].sum(axis=1)
ratio['MR'] = ratio['M'] / calc

print(ratio['MR'].sort_values(ascending=False))

# vi. For each occupation, calculate the minimum and maximum ages.
print(users.groupby('occupation').age.agg(['min', 'max']))
# vii. For each combination of occupation and gender, calculate the mean age.
print(users.groupby(['occupation', 'gender']).age.mean())
# viii. Per occupation present the percentage of women and men.
gender = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})
count = users.groupby(['occupation']).count()
genderpercent = (gender/count) * 100
print(genderpercent['gender'])

# =================================================================
# Class_Ex1:
# From the data table above, create an index to return all rows for
# which the phylum name ends in "bacteria" and the value is greater than 1000.
# ----------------------------------------------------------------

data = pd.DataFrame({'value': [632, 1638, 569, 115, 433, 1130, 754, 555],
                     'patient': [1, 1, 1, 1, 2, 2, 2, 2],
                     'phylum': ['Firmicutes', 'Proteobacteria', 'Actinobacteria',
                                'Bacteroidetes', 'Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes']})

print(20 * "-" + "Q1" + 20 * "-")
print(data[(data.phylum.str.endswith('bacteria')) & (data.value > 1000)])
# =================================================================
# Class_Ex2:
# Create a treatment column and add it to DataFrame that has 6 entries
# which the first 4 are zero and the 5 and 6 element are 1 the rest are NAN
# ----------------------------------------------------------------

print(20 * "-" + "Q2" + 20 * "-")
treatment = pd.Series([0]*4 + [1]*2)
data['treatment'] = treatment
print(data)

# =================================================================
# Class_Ex3:
# Create a month column and add it to DataFrame. Just for month Jan.
# ----------------------------------------------------------------
print(20 * "-" + "Q3" + 20 * "-")
data['month']='Jan'
print(data)

# =================================================================
# Class_Ex4:
# Drop the month column.
# ----------------------------------------------------------------
print(20 * "-" + "Q4" + 20 * "-")
data= data.drop('month' , 1)
print(data)

# =================================================================
# Class_Ex5:
# Create a numpy array that has all the values of DataFrame.
# ----------------------------------------------------------------
print(20 * "-" + "Q5" + 20 * "-")
look = np.array(list(data['value']))
print(look)

# =================================================================
# Class_Ex6:
# Read baseball data into a DataFrame and check the first and last
# 10 rows
# ----------------------------------------------------------------
print(20 * "-" + "Q6" + 20 * "-")
Baseball = pd.read_csv('baseball.csv')
print(Baseball[:10])
print(Baseball[-10:])


# =================================================================
# Class_Ex7:
# Create  a unique index by specifying the id column as the index
# Check the new df and verify it is unique
# ----------------------------------------------------------------
print(20 * "-" + "Q7 " + 20 * "-")
print(Baseball['id'].unique())
Baseball = Baseball.set_index('id')


# =================================================================
# Class_Ex8:
# Notice that the id index is not sequential. Say we wanted to populate
# the table with every id value.
# Hint: We could specify and index that is a sequence from the first
# to the last id numbers in the database, and Pandas would fill in the
#  missing data with NaN values:
# ----------------------------------------------------------------
print(20 * "-" + "Q8" + 20 * "-")

Seq = range(Baseball.index.values.min(), Baseball.index.values.max())
new_baseball = Baseball.reindex(Seq)
print(new_baseball.head())


# =================================================================
# Class_Ex9:
# Fill the missing values
# ----------------------------------------------------------------
print(20 * "-" + "Q9" + 20 * "-")
print(new_baseball.fillna(0, inplace = True))
print(new_baseball.head())

# =================================================================
# Class_Ex10:
# Find the shape of the new df
# ----------------------------------------------------------------
print(20 * "-" + "Q10" + 20 * "-")
print(new_baseball.shape)


# =================================================================
# Class_Ex11:
# Drop row 89525 and 89526
# ----------------------------------------------------------------
print(20 * "-" + "Q11" + 20 * "-")
Baseball1 = new_baseball.drop(89526, axis = 0)
Baseball2 = Baseball1.drop(89525, axis = 0)
print(Baseball2[-10:])


# =================================================================
# Class_Ex12:
# Sor the df ascending and not ascending
# ----------------------------------------------------------------
print(20 * "-" + "Q12" + 20 * "-")
print("Ascending")
print(Baseball2.sort_values(['id'], ascending=True))
print("Descending")
print(Baseball2.sort_values(['id'], ascending=False))
print(20* "-" + "Ex12" + 20* "-")
