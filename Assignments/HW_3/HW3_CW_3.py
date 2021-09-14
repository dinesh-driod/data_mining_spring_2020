print("==================== DINESH - ASSIGNMENT 3 =============================================")
print("==================== HomeWork-3 Programs=================================================")
# E.1:
# Write a script to find duplicates from an array (define an array with some duplicates on it).
# If you use built in function in python explain the methods and how this methods are working.

# Initialize array
def Repeat(x):
    arr_size = len(x)
    repeated = []
    for i in range(arr_size):
        k = i + 1
        for j in range(k, arr_size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print(Repeat(list1))
print()
print("==================== END OF EX 1========================================================")
# E.2:
#Write a script that finds all such numbers which are divisible by 2 and 5, less than 1000.
# If you use built in function in python explain the methods and how this methods are working.

for i in range(1001):
    if ((i % 2 == 0) and (i % 5 == 0)):
        print(i, "Divisible by 2 and 5")
    else:
        pass
print()
print("==================== END OF EX 2========================================================")
# E.3:
# Write a Python class to convert a roman numeral to an integer. Hint: (Use the following symbols
# and numerals Wiki )
class solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

print(solution().roman_to_int('MMXX'))
print(solution().roman_to_int('XL'))
print(solution().roman_to_int('LX'))

print()
print("==================== END OF EX 3========================================================")
# E.4:
# Write a Python class to find sum the three elements of the given array to zero.
# Given: [-20, -10, -6, -4, 3, 4, 7, 10]
# Output : [[-10, 3, 7], [-6, -4, 10]]

class solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(solution().threeSum([-20, -10, -6, -4, 3, 4, 7, 10]))

print()
print("==================== END OF EX 4=========================================================")
print()
print("==================== END OF HomeWork Examples============================================")
print()
print("==================== ClassWork-3-Programs================================================")
# Class_Ex1:
# Writes a python script (use class) to simulate a Stopwatch .
# push a button to start the clock (call the start method), push a button
# to stop the clock (call the stop method), and then read the elapsed time
# (use the result of the elapsed method).
# ----------------------------------------------------------------
import time

input("Press Enter to start")
startT = time.time()

input("Press Enter to end")
endT = time.time()

class Stopwatch:
    def __init__(self, startT, endT):
        self.lapsedT = -startT + endT
        self.startT = startT
        self.endT = endT

    def lapasedT(self):
        return endT - startT

    def lapasedformatT(self):
        sec = self.lapsedT
        mins = sec // 60.
        sec = sec % 60.
        hours = mins // 60.

        mins = mins % 60.
        return print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))

obj = Stopwatch(startT, endT)
#print(obj.startT)
#print(obj.endT)
print("Elapsed Time:", obj.lapasedT())
print("The Formatted Result(H:M:S) is displayed below")
print(obj.lapasedformatT())
print("==================== END OF CW 1=========================================================")


# Class_Ex2:
# Write a python script (use class)to implement pow(x, n).
# ----------------------------------------------------------------
class py_solution:
    def pow(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x

        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.pow(x, -n)
        val = self.pow(x, n // 2)
        if n % 2 == 0:
            return val * val
        return val * val * x


print(py_solution().pow(3, -4));
print(py_solution().pow(2, 5));
print(py_solution().pow(10, 0));

print()
print("==================== END OF CW 2=========================================================")


# Class_Ex3:
# Write a python class to calculate the area of rectangle by length
# and width and a method which will compute the area of a rectangle.
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width


newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())
print()
print("==================== END OF CW 3=========================================================")
# Class_Ex4:
# Write a python class and name it Circle to calculate the area of circle
# by a radius and two methods which will compute the area and the perimeter
# of a circle.
import math


class circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


r = int(input("Enter radius of circle: "))
obj = circle(r)
print("Area of circle:", round(obj.area(), 2))
print("Perimeter of circle:", round(obj.perimeter(), 2))
print()
print("==================== END OF ClassWork Programs============================================")
