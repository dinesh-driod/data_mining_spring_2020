print("==================== DINESH - ASSIGNMENT 1 =============================================")
# ====================================================================================
# Class_Ex1:
# Write python program that converts seconds to
# (x Hour, x min, x seconds)
# ----------------------------------------------------------------
time = float(input("Input time in seconds: "))
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("hour:minutes:seconds-> %d:%d:%d" % (hour, minutes, seconds))
print("==================== END OF EX 1=============================================")
# ====================================================================================
# Class_Ex2:
# Write a python program to print all the different arrangements of the
# letters A, B, and C. Each string printed is a permutation of ABC.
# ----------------------------------------------------------------
#Functions creating iterators for efficient looping.
s = input ("Enter 3 letter string (say ABC) to display all the permutation: ")
for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            if i!=k and k!=j and i!=j:
                print(s[i] + s[j] + s[k])
print("==================== END OF EX 2=============================================")
# ====================================================================================
# Class_Ex3:
# Write a python program to print all the different arrangements of the
# letters A, B, C and D. Each string printed is a permutation of ABCD.
# ----------------------------------------------------------------
s = input ("Enter 4 letter string (say ABCD) to display all the permutation: ")
for k in range(0, 4):
    for l in range(0, 4):
        for m in range(0, 4):
            for n in range(0, 4):
                 if k!=l and k!=m and l!=m and l!=n and m!=n and n!=k:
                     print(s[k] + s[l] + s[m] + s[n])
print("====================END OF EX 3=============================================")

# ====================================================================================
# Class_Ex4:
# Suppose we wish to draw a triangular tree, and its height is provided
# by the user.
# ----------------------------------------------------------------
n = int(input("Enter the height of Triangle: "))
for i in range(0, n):
    for j in range (0,n-i-1):
            print(end=" ")

        # inner loop to handle number of columns
        # values changing acc. to outer loop
    for j in range(0, i + 1):
            # printing stars
        print("* ", end="")

            # ending line after each row
    print("\r")
print("==================== END OF EX 4 =============================================")
# ====================================================================================
# Class_Ex5:
# Write python program to print prime numbers up to a specified values.
# ----------------------------------------------------------------
print("Display prime numbers from a range")
l = int(input("Enter lower range: "))
u = int(input("Enter upper range: "))
for n in range(l, u+1):
    if n>1:
        for i in range(2, n):
            if (n % i) == 0:
                #print(n, "is not a prime number")
                break
        else:
         # loop fell through without finding a factor
             print(n)
            #print(n, 'is a prime number')
print("====================END OF EX 5=============================================")