# %% -------------------------Q:1------------------
print(20 * "-" + "Q1" + 20 * "-")
a=[1,2,3,4,5,6,7,8,9]
try:
    a[::2]=10,20,30,40,50,60
except ValueError as e:
    z = e
print(z)
# %% -------------------------Q:2------------------
print(20 * "-" + "Q2" + 20 * "-")
def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])
# %% -------------------------Q:3------------------
print(20 * "-" + "Q3" + 20 * "-")
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v
print(fun(data[0]))
# %% -------------------------Q:4------------------
print(20 * "-" + "Q4" + 20 * "-")
arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())
# %% -------------------------Q:5------------------
print(20 * "-" + "Q5" + 20 * "-")
def f(i, values = []):
    values.append(i)
    print (values)
    return values
f(1)
f(2)
f(3)
# %% -------------------------Q:6------------------
print(20 * "-" + "Q6" + 20 * "-")

init_tuple = ()
print (init_tuple.__len__())
# %% -------------------------Q:7------------------
print(20 * "-" + "Q7" + 20 * "-")
l = [1, 2, 3]

init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
print(init_tuple)

# %% -------------------------Q:8------------------
print(20 * "-" + "Q8" + 20 * "-")
init_tuple = (1,) * 3
try:
    init_tuple[0] = 2
except:
   print('‘tuple’ object does not support item assignment')
# %% -------------------------Q:9------------------
print(20 * "-" + "Q9" + 20 * "-")
arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1

sum = 0
for k in arr:
    sum += arr[k]

print (sum)
# %% -------------------------Q:10------------------
print(20 * "-" + "Q10" + 20 * "-")

dict = {'c': 97, 'a': 96, 'b': 98}

for _ in sorted(dict):
    print (dict[_])