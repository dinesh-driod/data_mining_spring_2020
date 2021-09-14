import numpy as np
import matplotlib.pyplot as plt

# %% 1- Load the image.npy using numpy package and print the data type.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q1" + 20* "-")
image = np.load('image.npy')
print(type(image))

# %% 2- Plot the image and explain the features of the figure (color or black and white, size of the image, resolution)
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q2" + 20* "-")
plt.figure(1)
plt.imshow(image)


print('The image is gray scale since there is no channel {}'.format(image.shape))
print('The size image is {}'.format(image.shape))
print('Image is low resolution since there is no channel and the size is small')

# %% 3- Flip the image 90, 180, 270 degree by using numpy.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q3" + 20* "-")
image1 = np.rot90(image)
image2 = np.rot90(image,2)
image3 = np.rot90(image,3)
plt.figure(2)
plt.imshow(image1)

plt.figure(3)
plt.imshow(image2)

plt.figure(4)
plt.imshow(image3)

# %% 4- Remove the background and try to find the camera man in the picture (set the background to white or black)
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q4" + 20* "-")
image4 = np.ravel(image)
index = np.where(image4 >30)
image4[index] = 255
image4= image4.reshape(512,512)

plt.figure(5)
plt.imshow(image4,cmap='gray')


# %% 5- Keep the background and try color the cameraman by white colors.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q5" + 20* "-")
image = np.load('image.npy')
mask = image < 30
image[mask] = 255
plt.figure(6)
plt.imshow(image, cmap='gray')
plt.show()