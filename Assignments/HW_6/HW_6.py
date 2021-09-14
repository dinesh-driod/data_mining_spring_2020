# =================================================================
# Class_Ex1:
# We will do some  manipulations on numpy arrays by importing some
# images of a racoon.
# scipy provides a 2D array of this image
# Plot the grey scale image of the racoon by using matplotlib
# ----------------------------------------------------------------
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
face = misc.face(gray=True) ## Modify the face function
plt.imshow(face)
plt.title("Image")
plt.show()
print('#',50*"-")
# =================================================================
# Class_Ex2:
# If still the face is gray choose the color map function and make it
# gray
# ----------------------------------------------------------------


plt.imshow(face,cmap='gray')
plt.title("Image with color map set to gray")
plt.show()

print('#',50*"-")
# =================================================================
# Class_Ex3:
# Crop the image (an array of the image) with a narrower centering
# Plot the crop image again.
# ----------------------------------------------------------------

cropped_image = face[150:-150, 150:-150]
plt.imshow(cropped_image,cmap='gray')
plt.title("Cropped Image (Removed 150 pixels from all borders)")
plt.show()


print('#',50*"-")
# =================================================================
# Class_Ex4:
# Take the racoon face out and mask everything with black color.
# ----------------------------------------------------------------

new_face=face.copy()
new_face[:,:]=0
new_face[230:490,450:800]=face[230:490,450:800]
plt.imshow(new_face,cmap='gray')
plt.title("Only racoon face")
plt.show()


print('#',50*"-")
# =================================================================
# Class_Ex5:
# For linear equation systems on the matrix form Ax=b where A is
# a matrix and x,b are vectors use scipy to solve the for x.
# Create any matrix A and B (Size matters)
# ----------------------------------------------------------------

import numpy as np
from scipy.linalg import solve

A = np.array([[5, 25, 17], [21, 3, 15], [2, 5, 6]])
B = np.array([12, 9, 5])
print("\nMatrix A:\n",A)
print("\n\nMatrix B:\n",B)
x=solve(A,B)
print("\n\nSolutions:\n",x)

print('#',50*"-")
# =================================================================
# Class_Ex6:
# Calculate eigenvalue of matrix A. (create any matrix and check your
# results.)
# ----------------------------------------------------------------

import scipy

A=np.random.randint(1,20,9).reshape(3,3)
print("\nMatrix A:\n",A)
print("\n\nEigenvalue of matrix A:\n",scipy.linalg.eigvals(A))


print('#',50*"-")
# =================================================================
# Class_Ex7:
# Sparse matrices are often useful in numerical simulations dealing
# with large datasets
# Convert sparse matrix to dense and vice versa
# ----------------------------------------------------------------


import numpy as np
from scipy.sparse import csr_matrix

A=np.random.randint(1,20,15).reshape(3,5)
print("\nDense matrix representation:\n", A)
A_sparse = csr_matrix(A)
print("\n\nSparse matrix:\n",A_sparse)
A_dense = A_sparse.todense()
print("\n\nDense matrix:\n", A_dense)

print('#',50*"-")

# =================================================================
# Class_Ex8:
# Create any polynomial to order of 3 and write python function for it
# then use scipy to minimize the function (use Scipy)
# ----------------------------------------------------------------


from scipy.optimize import minimize_scalar
print("\nUsing Python Function - Polynominal of Order 3")
def polynomial_func(x):
    return x**3 + 2*x**2 - 3*x + 4

for x in [2, -3, 6]:
    print("\nValue of x: ",x,"\nResult: ", polynomial_func(x))

print("\n\nUsing Scipy Function - Polynominal of Order 3")
result = minimize_scalar(polynomial_func)
for x in [2, -3, 6]:
    print("\nValue of x: ",x,"\nResult: ", result.x)


print('#',50*"-")
# =================================================================
# Class_Ex9:
# use the brent or fminbound functions for optimization and try again.
# (use Scipy)
# ----------------------------------------------------------------

from scipy import optimize

def polynomial_func2(x):
    return x ** 2

minimum = optimize.fminbound(polynomial_func2, -4, 1)
print("\n\nMinimum of the function in range(-4,1): ",minimum)
minimum = optimize.fminbound(polynomial_func2, 1, 5)
print("\nMinimum of the function in range(1,5): ",minimum)

print('#',50*"-")
# =================================================================
# Class_Ex10:
# Find a solution to a function. f(x)=0 use the fsolve (use Scipy)
# ----------------------------------------------------------------

from scipy.optimize import fsolve
import numpy as np

def my_function(x):
    return x + 4 * np.cos(x)

result = fsolve(my_function, 0.5)
print("\n\nSolution to the function: ",result)


print('#',50*"-")
# =================================================================
# Class_Ex11:
# Create a sine or cosine function with a big step size. Use scipy to
# interpolate between each data points. Use different interpolations.
# plot the results (use Scipy)
# ----------------------------------------------------------------

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 11)
y = np.sin(-x**2/9.0)
p1 = interp1d(x, y, kind='nearest')
p2 = interp1d(x, y, kind='previous')
p3 = interp1d(x, y, kind='next')

x_new = np.linspace(0, 20, 1001)

plt.plot(x, y, 'o')
plt.plot(x_new, p1(x_new), '-', x_new, p2(x_new), '--', x_new, p3(x_new), ':')
plt.legend(['data', 'nearest', 'previous', 'next'], loc='best')
plt.title("Sine Function of Different Interpolations")
plt.show()

print('#',50*"-")
# =================================================================
# Class_Ex12:
# Use scipy statistics methods on randomly created array (use Scipy)
# PDF, CDF (CUMsum), Mean, Std, Histogram
# ----------------------------------------------------------------


from scipy import stats
import scipy
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0,100,20)
print("\nRandom Array:", x)
print("\n\nMean:", stats.tmean(x))
print("\n\nStd:", stats.tstd(x))
print("\n\nPDF:", stats.norm.pdf(x))
print("\n\nCDF:", stats.norm.cdf(x))
print("\n\nCUMsum:", np.cumsum(x))

hist, bin_edges = scipy.histogram(x, bins=range(20))
print("\n\nNo. of points in each bin : ", hist)
print("\n\nSize of the bins          : ", bin_edges)
plt.bar(bin_edges[:-1], hist, width=1)
plt.xlim(min(bin_edges), max(bin_edges))
plt.show()

print('#',50*"-")
# =================================================================
# Class_Ex13:
# USe hypothesise testing  if two datasets of (independent) random varibales
# comes from the same distribution (use Scipy)
# Calculate p values.
# ----------------------------------------------------------------

from scipy.stats import ttest_ind
import numpy as np

sample_1 = np.random.randint(0,100,20)
sample_2 = np.random.randint(0,100,20)
print("\nSample 1:\n")
print(sample_1)
print("\n\nSample 2:\n")
print(sample_2)
print("\n\nSample 1 Mean:", np.mean(sample_1))
print("\nSample 2 Mean:", np.mean(sample_2))
print("\n\nSample 1 Standard Deviation:", np.std(sample_1))
print("\nSample 2 Standard Deviation:", np.std(sample_2))

print("\n\nOur null hypothesis is that two independent samples (Sample 1 and Sample 2) have identical mean values.")
ttest,pval = ttest_ind(sample_1,sample_2)
print("\np-value:",pval)

if pval <0.05:
  print("\nSince p-value < 0.05, hence we reject null hypothesis.")
else:
  print("\nSince p-value > 0.05, hence we fail to reject the null hypothesis.")

print('#',50*"-")
# ----------------------------------------------------------------