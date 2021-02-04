#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[5]:


#1. Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10.

arr1 = np.arange(100, 200, 10)
arr1 = arr1.reshape(5,2)
print (arr1)


# In[6]:


#2. Write a NumPy program to create a 3x3x3 array filled with arbitrary values and find the minimum and maximum values.

arr2 = np.random.randint(0,50, size = (3,3))
print("3*3*3 array\n",arr2)
print("The minimum value is",np.min(arr2))
print("The maximum value is",np.max(arr2))


# In[9]:


#3. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.

arr3=np.diag([1,2,3,4,5])
print("5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5\n",arr3)


# In[10]:


#4. Given an array arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
#i) Extract all odd numbers from arr 
#ii) Replace all odd numbers in arr with -1

arr4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("The Odd numbers are")
for i in arr4:
    if i%2!=0:
        print(i)
        arr4[i]=-1
print("Replacing all odd number with -1",arr4)


# In[11]:


#5.Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1,the rest are 0.

arr5=np.identity(3,dtype=int)
print("3x3 identity matrix\n",arr5)


# In[18]:


#6. Write a NumPy program to convert an array to a float type.

arr6=([1,2,3,4,5])
print("Before Converting to float\n",arr6)
arr6_float=np.asfarray(arr6)
print("After Converting to float\n",arr6_float)


# In[17]:


#7. Write a NumPy program to generate five random numbers from the normal distribution.

arr_normal=np.random.normal(size=5)
print("five random numbers from the normal distribution\n",arr_normal)


# In[19]:


#8. Following is the input NumPy array delete column two and insert following new column in its place.
#sampleArray=numpy.array([[34,43,73],[82,22,12],[53,94,66]])
#newColumn = numpy.array([[10,10,10]])

samplearray=np.array([[34,43,73],[82,22,12],[53,94,66]])
newcolumn = np.array([[10,10,10]])
print("Before Removing column 2\n",samplearray)
samplearray[:,2]=newcolumn
print("After Removing column 2 and inserting new column in its place\n",samplearray)


# In[21]:


#9. Write a NumPy program to compute the multiplication of two given matrices.

arr_mult1=([1,2],[3,4])
arr_mult2=([2,4],[6,8])
arr_mult3=np.multiply(arr_mult1,arr_mult2)
print("After Multiplication\n",arr_mult3)


# In[22]:


#10. Write a NumPy program to create a random vector of size 10 and sort it.

arr_ran=np.random.random(10)
print("Before Sorting\n",arr_ran)
arr_ran_sort=np.sort(arr_ran)
print("After sorting\n",arr_ran_sort)


# In[23]:


#11. Write a NumPy program to compute the covariance matrix of two arrays.

arr_cov1=np.random.random(10)
arr_cov2=np.random.random(10)
print("1st array\n",arr_cov1)
print("2nd array\n",arr_cov2)
arr_cov=np.cov(arr_cov1,arr_cov2)
print("Covariance Matrix\n",arr_cov)


# In[24]:


#12.Create a 4X2 integer array and Prints its
#i)The shape of an array.
#ii) Array dimensions.
#iii) The Length of each element of the array in bytes

array4X2 = np.empty([4,2])
print("4X2 array",array4X2)
print("Shape of Array",np.shape(array4X2))
print("Dimension of Array",np.ndim(array4X2))
print("The Length of each element of the array in bytes",array4X2.itemsize)                  


# In[25]:


#13. Write a NumPy program to concatenate element-wise two arrays of string.

arr_str1=np.array(['Yogesh','Prasad'])
arr_str2=np.array(['Yo','Pra'])
print("Before concatenate\n",arr_str1,"\n",arr_str2)
arr_str3=np.char.add(arr_str1,arr_str2)
print("After concatenate element-wise\n",arr_str3)


# In[26]:


#14. Write a NumPy program to capitalize the first letter, lowercase, uppercase, swapcase, title-case of all the 
#elements of a given array.

arr_strp=np.array(['Yogesh','Prasad','Aditya','Rohan'])
print("original array\n",arr_strp)
print("Capitalize the first letter\n",np.char.capitalize(arr_strp))
print("Lowercase\n",np.char.lower(arr_strp))
print("Uppercase\n",np.char.upper(arr_strp))
print("Swapcase\n",np.char.swapcase(arr_strp))
print("Title Case\n",np.char.title(arr_strp))


# In[27]:


#15. Write a NumPy program to convert a given array into a list.

print("Array before converting to list\n",arr_strp)
list_arr_strp=list(arr_strp)
print("After converting to list\n",list_arr_strp)
print(type(list_arr_strp))


# In[28]:


#16. Write a NumPy program to compute the sum of all elements, sum of each column and sum of each row of a given array.

print("Array\n",arr2)
print("sum of all elements",np.sum(arr2))
print("Sum of 1st column",np.sum(arr2[:,0]))
print("Sum of 2nd column",np.sum(arr2[:,1]))
print("Sum of 3rd column",np.sum(arr2[:,2]))
print("Sum of 1st row",np.sum(arr2[0,:]))
print("Sum of 2nd row",np.sum(arr2[1,:]))
print("Sum of 3rd row",np.sum(arr2[2,:]))


# In[31]:


#17. Write a NumPy program to create a random 10x4 array and extract the first five rows of the array and store 
#them into a variable.

arr10X4=np.random.rand(10,4)
print("10X4 array\n",arr10X4)
storeval=arr10X4[:5]
print("extract the first five rows of the array and store them into a variable\n",storeval)


# In[32]:


#18. Write a NumPy program to get the unique elements of a 1D and 2D array.

arr1d=np.array([1,2,3,4,6,5,4,3,1])
print("Original 1D Array\n",arr1d)
print("Unique Elements in 1D Array\n",np.unique(arr1d))
arr2d=np.array([[1,2],[2,3],[3,4],[5,6]])
print("Original 2D Array\n",arr2d)
print("Unique Elements in 2D Array\n",np.unique(arr2d))


# In[33]:


#19. Write a NumPy program to get the unique elements of an array.
#arr= [ -10 12.12 -0.2]

arr1 = np.array([-10, 12,.12,-0.2,12,-10])
print(arr1)
np.unique(arr1)


# In[34]:


#20. Write a NumPy program to save a given array to a text file and load it. You have to save and load files using numpy library.

arr_txt=np.arange(9).reshape(3, 3)
print("Before Loading into Text File\n",arr_txt)
np.savetxt("text.txt",arr_txt)
arr_ret=np.loadtxt("text.txt")
print("After Pulling from Text File\n",arr_ret)


# In[ ]:





# In[ ]:




