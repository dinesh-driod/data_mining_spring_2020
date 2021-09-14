
# %%------------------------------------------------------------------------------
# Question 1:
# Hangman is a classic word game in which you must guess as many secret words as you can before time runs out! Challenge yourself.
# https://hangmanwordgame.com/?fca=1&success=0#/
# Write a computer program that simulate the following game.
# NOTE:  Write your own program.
# Your program should be as follows:
# your search word is DATAMINING.
# -- you will have 10 chances to predict the word. After that you should print a Game Over.
# -- The code should ask Enter the character you guess:
# -- Your guess is: ______ if it is not the character that you wanted.
# -- Your guess is: _A_A______ if you choose A.
# -- If you predict all the characters correctly then You win.

# %%--------------------------------Answer----------------------------------------------

import random

words = ['DATA MINING']
word = random.choice(words)
print("Enter the characters You Guess")
guesses = ''
turns = 10
while turns > 0:
        failed = 0
        for char in word:
                if char in guesses:
                        print(char)
                else:
                        print("_")
                        failed += 1

        if failed == 0:
                print("You Win")
                print("The word is: ", word)
                break

        guess = input("guess a character:")
        guesses += guess
        if guess not in word:

                turns -= 1
                print("Wrong")
                print("You have", + turns, 'more guesses')
                if turns == 0:
                        print("You Loose")
                print("GAME OVER")



                # %%-----------------------------------End-------------------------------------------
# %%----------------------------------------------------------------------------------
# Question 2:
# Guess The Number
# Write a computer program that simulate the Guessing the Number.
# NOTE:  Write your own program.
# Your program should be as follows:
# -- First it should ask  the number you want to try to guess
# -- It should generate a random number between the two numbers that users will input
# Example:
# Enter the number you want to start:0
# Enter the number you want to end:25
# -- Then it should guide the user by stating the value is high or low to find the number.
# %%---------------------------------Answer---------------------------------------------
import random
import time

def guess_number():
    min_value = 0
    max_value = 25
    guess_number = "yes"
    while guess_number == "yes" or guess_number == "Yes" or guess_number == "Y" or guess_number == "y" or guess_number == "YES":
        if guess_number == 0:
                print ("Low Value")
        elif max_value >25:
                print("High Value")
        else:
                print("Guesssing.....")
                print("The values are...")
                time.sleep(1)
                print(random.randint(min_value, max_value))
                print(random.randint(min_value, max_value))
                guess_number = input("Do you want to guess again ")

guess_number()

# %%-----------------------------------End-------------------------------------------
# Question 3:
# Graphs are networks that have nodes connected by edges or arcs.
# In directed graphs, the relationship between nodes have a direction,
# and are called arcs, in not directed graphs, the connections have no
# direction and are names edges. Assume we have the following graph.
# A -> B
# A -> C
# B -> C
# B -> D
# C -> D
# D -> C
# E -> F
# F -> C
# 1- Assign the following graph to a meaningful python variable and explain why that is the best.
# 2- Write a function to find a path between two nodes.
# It takes a graph (variable in 1) and the start and end as input. It will return a list of nodes
# 3- Change question number 2 code to find all the paths between a given start and end.
# 4- Change question number 3 and finds the closest or shortest path between two given start and end node.
# %%------------------------------------------------------------------------------
# Assigning to a meaningful python variable called graph. Dictonary creates 1-1 relationship between keys and values
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
#function to find a path between nodes
def navigate_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = navigate_path(graph, node, end, path)
                if newpath: return newpath
        return None
        navigate_path(graph, 'A', 'D')
        print(graph)


# %%-----------------------------------End-------------------------------------------
# Question 4:
# Consider the following Python dictionary data and Python list labels, Answer the following questions
# 1- Create a DataFrame df from this dictionary data which has the index labels.
# 2- Display a summary of the basic information about this DataFrame and its data.
# 3- Return the first 3 rows of the DataFrame df.
# 4- Select just the 'animal' and 'age' columns from the DataFrame df
# 5- Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
# 6- Select only the rows where the number of visits is greater than 3.
# 7- Select the rows where the age is missing, i.e. is NaN.
# 8- Select the rows where the animal is a cat and the age is less than 3.
# 9- Select the rows the age is between 2 and 4 (inclusive).
# 10- Change the age in row 'f' to 1.5.
# 11- Calculate the sum of all visits (the total number of visits).
# 12- Calculate the mean age for each different animal in df.
# 13- Append a new row 'k' to df with your choice of values for each column. Then delete that row to return the original DataFrame.
# 14- Count the number of each type of animal in df.
# 15- Sort df first by the values in the 'age' in decending order, then by the value in the 'visit' column in ascending order.
# 16- The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes'
# should be True and 'no' should be False.
# 17- In the 'animal' column, change the 'snake' entries to 'python'.
# 18- For each animal type and each number of visits, find the mean age. In other words, each row is an animal, each column
# is a number of visits and the values are the mean ages (hint: use a pivot table).

# %%------------------------------------------------------------------------------

import pandas as pd
import numpy as np

# creating Dataframe
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 1- Create a DataFrame df from this dictionary data which has the index labels.
df = pd.DataFrame(data,labels)
# 2- Display a summary of the basic information about this DataFrame and its data.
print(df.info())
# 3- Return the first 3 rows of the DataFrame df.
print(df.head(3))
# 4- Select just the 'animal' and 'age' columns from the DataFrame df
# 5- Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
# 6- Select only the rows where the number of visits is greater than 3.
# 7- Select the rows where the age is missing, i.e. is NaN.
# 8- Select the rows where the animal is a cat and the age is less than 3.
# 9- Select the rows the age is between 2 and 4 (inclusive).
# 10- Change the age in row 'f' to 1.5.
# 11- Calculate the sum of all visits (the total number of visits).
# 12- Calculate the mean age for each different animal in df.
# 13- Append a new row 'k' to df with your choice of values for each column. Then delete that row to return the original DataFrame.
# 14- Count the number of each type of animal in df.
# 15- Sort df first by the values in the 'age' in decending order, then by the value in the 'visit' column in ascending order.
# 16- The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes'
# should be True and 'no' should be False.
# 17- In the 'animal' column, change the 'snake' entries to 'python'.
# 18- For each animal type and each number of visits, find the mean age. In other words, each row is an animal, each column
# is a number of visits and the values are the mean ages (hint: use a pivot table).



