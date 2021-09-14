print("==================== DINESH - ASSIGNMENT 2 =============================================")
print("==================== HomeWork-2 Programs=================================================")
#E.1:
#Search algorthim for array:
def search(array, targetvalue):
    min  = 0
    max = len(array) - 1
    found = False
    while (min <= max and not found):
        guess = (min + max) // 2
        if array[guess] == targetvalue:
            found = True
        else:
            if targetvalue < array[guess]:
                max = guess - 1
            else:
                min = guess + 1
    return found

print(search([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 61))
print(search([1, 2, 3, 5, 8, 9, 10, 11, 13, 16, 89], 90))
print()
print("==================== END OF EX 1========================================================")
#E.2:
#Work on a script to count the number of characters or (frequency) in a string.

string = input("Enter a string: ")
a = len(string)
print("Length of the string:", string, '=',a)
print()
print("==================== END OF EX 2========================================================")
#E.3:
#Write a function that takes a list of words and returns the length of the longest one.

def longest_words_inlist(list_of_words):
    longest_word = list_of_words[0]
    for word in list_of_words:
        if len(longest_word) < len(word):
            longest_word = word
    print(f'The longest word is: {longest_word}')
    return longest_word

longest_words_inlist(['MSI', 'lambda', 'Aser', "dell", "Radioactive"])
print()
print("==================== END OF EX 3========================================================")
#E.4:
#Make up your own list and work on a program to get the smallest number from the list.
# list of numbers
list1 = [100, 20, 48, 45, 99]

# printing the smallest element
print("Smallest element is:", min(list1))
print()
print("==================== END OF EX 4=========================================================")
#E.5:
#Work on a function that takes two lists and returns same (or True) if they have at least one common element.

def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

    return result

a = [1, 2, 3, 4, 5]
b = [10, 6, 7, 8, 9]
print(common_data(a, b))

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_data(a, b))
print()
print("==================== END OF EX 5=========================================================")
#E.6:
#Work on a script to merge or join two dictionaries

first_Dict = {1: 'mac', 2: 'iphone', 3: 'ipad'}
second_Dict = {4: 'iwatch', 5: 'ipods'}
print("First Dictionary: ", first_Dict)
print("Second Dictionary: ", second_Dict)

first_Dict.update(second_Dict)

print("\nAfter merging two Dictionaries : ")
print(first_Dict)
print()
print("==================== END OF EX 6=========================================================")
#E.7:
#Work on a script or a program to map two lists into a dictionary

test_keys = ["iphone", "lambda", "ipods"]
test_values = [1, 2, 5]
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))
res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break
print("Resultant dictionary is : " + str(res))
print()
print("==================== END OF EX 7=========================================================")
print("==================== END OF HomeWork Examples=========================================================")
print()
print("==================== ClassWork-2-Programs=============================================================")
# Class_Ex1:
# Write a program that simulates the rolling of a die.
import random
total_dice = int(input('How many dice? '))
dice_val = int(input("How many sides? "))

rolls = []
high_roll = 0
low_roll = 0

for i in range(total_dice):
    roll = random.randint(1, dice_val)
    rolls.append(roll)

nums = len(rolls)

print("")
print("Roll #\tRoll")
print("------------------")
for i in range(nums):
    print("#" + str(i + 1) + ":\t" + str(rolls[i]))
print("==================== END OF CW 1=========================================================")
# Class_Ex2:
# Answer  Ex1 by using functions.
import random
import time

def rolling_dice():
    min_value = 1
    max_value = 6
    roll_again = "yes"
    while roll_again == "yes" or roll_again == "Yes" or roll_again == "Y" or roll_again == "y" or roll_again == "YES":
        print("Rolling dices...")
        print("The values are...")
        time.sleep(1)
        print(random.randint(min_value, max_value))
        print(random.randint(min_value, max_value))
        roll_again = input("Roll the dices again? ")

rolling_dice()
print()
print("==================== END OF CW 2=========================================================")
# Class_Ex3:
# Randomly Permuting a List

import random
test_list = [1, 4, 5, 6, 3]
print("The original list is : " + str(test_list))

# to shuffle a list
for i in range(len(test_list) - 1, 0, -1):

    # Pick a random index from 0 to i
    j = random.randint(0, i + 1)

    # Swap arr[i] with the element at random index
    test_list[i], test_list[j] = test_list[j], test_list[i]

# Printing shuffled list
print("The shuffled list is : " + str(test_list))
print()
print("==================== END OF CW 3=========================================================")
# Class_Ex4:
# Write a program to convert a tuple to a string.

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)
print()
print("==================== END OF CW 4=========================================================")
# Class_Ex5:
# Write a program to get the 3th element and 3th element from last of a tuple.

#Get an item of the tuple
tuplex = ("M", "A", "L", "A", "Y", "A", "L", "A", "M")
print(tuplex)
#Get item (3th element)of the tuple by index
item = tuplex[2]
print(item)
#Get item (3th element from last)by index negative
item1 = tuplex[-3]
print(item1)
print()
print("==================== END OF CW 5=========================================================")
# Class_Ex6:
# Write a program to check if an element exists in a tuple or not.
tuplex = ("M", "A", "L", "A", "Y", "A", "L", "A", "M")
print("M" in tuplex)
print(5 in tuplex)
print()
print("==================== END OF CW 6=========================================================")
# Class_Ex7:
# Write a  program to check a list is empty or not.

def Enquiry(lis1):
    if len(lis1) == 0:
        return 0
    else:
        return 1

lis1 = ['l', 'a', 'm', 'd', 'a' ]
if Enquiry(lis1):
    print("The list is not empty: \n lis1 = ",lis1)
else:
    print("The list is Empty: \n lis1 = ", lis1)
print()
print("==================== END OF CW 7=========================================================")
# Class_Ex8:
# Write a program to generate a 4*5*3 3D array that each element is O.
array_3d = [[['0' for col in range(4)] for col in range(5)] for row in range(3)]
print(array_3d)
print()
print("==================== END OF ClassWork Programs=========================================================")
