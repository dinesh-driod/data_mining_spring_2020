# -------------------------Q:1------------------
def pattern(n): 
    for i in n: 
        print("|", end = "") 
        print("*" * int(i))       
n = "41325"
pattern(n)
print(40*'=')
# -------------------------Q:2------------------
def squaresum(n) : 
    sm = 0
    for i in range(1, n+1) : 
        sm = sm + (i * i) 
      
    return sm 
n = 4
print(squaresum(n))
print(40*'=')
# -------------------------Q:3------------------
num = 11
if num > 1: 
   for i in range(2, num//2):       
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number")
print(40*'=')
# -------------------------Q:4------------------
start = 11
end = 25
  
for val in range(start, end + 1):   
   # If num is divisible by any number   
   # between 2 and val, it is not prime  
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val)
print(40*'=')
# -------------------------Q:5------------------
