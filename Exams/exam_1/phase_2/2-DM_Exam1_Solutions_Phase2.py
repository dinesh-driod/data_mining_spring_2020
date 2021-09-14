# %%------------------------------------------------------------------------------
# Question 1:
# Run the following code.
# 1- What is aa function do?.
# 2- What is bb function do?.
# 3- Are they solving the same problem? If yes exaplin?If no Exaplin?
# 4- The following codes represent and algorithm. Write down the logic of each algorithm .
# 5- If both function does some tasks, which one is faster and can you force one function produce the same results faster.
# %%--------------------------------Answer----------------------------------------------
def aa(xs, target):
    for (i, v) in enumerate(xs):
       if v == target:
           return i
    return -1
test_case = ["Amir", "Joe", "Mat", "Angelina"]
print(aa(test_case, "Amir"))

def bb(x, target):
    LB = 0
    UP = len(x)
    while True:
        if LB == UP:
           return -1
        m_ind = (LB + UP) // 2
        item_m= x[m_ind]
        if item_m == target:
            return m_ind
        if item_m < target:
            LB = m_ind + 1
        else:
            UP = m_ind
test_case = ["Amir", "Joe", "Mat", "Angelina"]
print(bb(test_case, "Amir"))

# Run the following code.
# 1- Linear search
# 2- Binary Search
# 3- Linear search is very slow compare to binary search
# 4-Linear search is incremental however binary search is finding a middle point
# and the search left and right is faster.
# 5-in this case since choose the test case like as example.
# %%-----------------------------------End-------------------------------------------
# %%----------------------------------------------------------------------------------
# Question 2:
# Answer the following questions in order.
# 1- Import the numpy package as np
# 2- Find which version of numpy is installed on your computer
# 3- Create a zero numpy array of size 208.
# 4- Find the memory size part 3
# 5- How to find the examples and syntax of the np.add without searching over the net?
# 6- Create a zero 2 dim array of size 10. Assign the fifth value of this vector 1.
# 7- Create an array with values started from 0 end to 10
# 8- Reverse the array you created at part 7.
# 9- Make a 3x3 matrix that values are ranging from 0 to 8 vertically and horizontally.
# 10- Find the indices that has non zero element for the following array [1,2,0,0,4,0]
# 11- Make a 2 dim array that has 1's on the edges and 0's inside for a matrix of 10 by 10 all ones in it.
# 12- Make a 2 dim array that has 0's on the edges and 1's inside for a matrix of 5 by 5 all ones in it.
# 13- Make a 5 by 5 matrix which all diagonal elements are 1,2,3,4
# 14- Create a two arrays and have some common values in it. Find common values between these two.
# 15- Make a random vector that has the shape of (100,2). Assume these are the coordinates. Find the point by point distances from each other.
# 16- Make a 2 different arrays. Add 1 to the second vector which is indexed by first vector?
# 17-  Make a one-dimensional array. Create a 2 dimensional array that the first row is the same az array  and other rows are shifted by 1?
# 18-Create a 10 by 3 numpy matrix. Store the rows which has unequal values into variable U.

# %%---------------------------------Answer---------------------------------------------
import numpy as np
print(np.__version__)
Z = np.zeros(10)
print(Z)
Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))
help(np.add)
Z = np.zeros(10)
Z[4] = 1
print(Z)
Z = np.arange(10,50)
print(Z)
Z = Z[::-1]
print(Z)
Z = np.arange(9).reshape(3,3)
print(Z)
print(Z.T)
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)
Z = np.diag(1+np.arange(4),k=-1)
print(Z)
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))
Z = np.random.random((10,2))
X,Y = np.atleast_2d(Z[:,0], Z[:,1])
D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
print(D)
Z = np.ones(10)
I = np.random.randint(0,len(Z),20)
Z += np.bincount(I, minlength=len(Z))
print(Z)
np.add.at(Z, I, 1)
print(Z)
from numpy.lib import stride_tricks

def rolling(a, window):
    shape = (a.size - window + 1, window)
    strides = (a.itemsize, a.itemsize)
    return stride_tricks.as_strided(a, shape=shape, strides=strides)
Z = rolling(np.arange(10), 3)
print(Z)
Z = np.random.randint(0,5,(10,3))
print(Z)
E = np.all(Z[:,1:] == Z[:,:-1], axis=1)
U = Z[~E]
print(U)
U = Z[Z.max(axis=1) != Z.min(axis=1),:]
print(U)
# %%-----------------------------------End-------------------------------------------
# %%----------------------------------------------------------------------------------
# Question 3:
# Answer the following questions in order.
# 1- Import the pandas package as pd
# 2- Read food data as data frame.
# 3- Pint the first 3 rows.
# 4- Visualize the top 3 items people bought
# 5- Visualize the number of items orderered  vs price.

# %%---------------------------------Answer---------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

chipo = pd.read_csv('food.tsv', sep = '\t')
x = chipo.item_name
letter_counts = Counter(x)
df = pd.DataFrame.from_dict(letter_counts, orient='index')
df = df[0].sort_values(ascending = True)[47:50]
df.plot(kind='bar')
plt.xlabel('Items')
plt.ylabel('Price')
plt.title('Most ordered Chipotle\'s Items')
plt.show()

chipo.item_price = [float(value[1:-1]) for value in chipo.item_price] # strip the dollar sign and trailing space
orders = chipo.groupby('order_id').sum()
plt.scatter(x = orders.item_price, y = orders.quantity, s = 50, c = 'green')
plt.xlabel('Order Price')
plt.ylabel('Items ordered')
plt.title('Number of items ordered per order price')
plt.ylim(0)
plt.show()
# %%-----------------------------------End-------------------------------------------
# %%----------------------------------------------------------------------------------
# Question 4:
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of
# congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# https://www.practicepython.org/solution/2014/04/02/08-rock-paper-scissors-solutions.html

# %%---------------------------------Answer---------------------------------------------
import sys
user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))