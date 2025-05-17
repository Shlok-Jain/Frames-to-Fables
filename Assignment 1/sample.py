import numpy as np
import pandas as pd
import math

# Python list to initialize a one dimensional NumPy array of numbers 1 to 5 and then print it
#py_list = [1,2,3,4,5]
#arr = np.array(py_list)
#print(arr)



# Python list to initialize a two dimensional NumPy array of shape [3,3] and then print it
#list = [[1,2,3],
#        [9,4,7],
#       [3,9,4]]
#arr = np.array(list)
#print(arr)



# Write a NumPy function to create an array with random values of shape [3,4]
# def create_random_array():
#     return np.random.rand(3, 4)

# random_array = create_random_array()
# print(random_array)



# Write a NumPy function to create an array with all elements initialized as zero of shape [3,4]

# def create_zeros_array():
#     return np.zeros((3, 4))

# zeros_array = create_zeros_array()
# print(zeros_array)




# Write a NumPy function to create an array with all elements initialized as ones of shape [3,4]
# def create_ones_array():
#     return np.ones((3, 4))

# ones_array = create_ones_array()
# print(ones_array)





# Write a NumPy function to create an array containing a range of evenly spaced intervals
#arr1=np.linspace(start,stop,no. of elements)
#arr2=np.arange(start,stop,gap b/w two consecutive elements)





#a = np.array([[-4,6,8], [9, 3, 1], [1, 8, 5]])
#b = np.array([[11,16,18], [90, 37, 81], [61, 48, 75]])




# Write a NumPy function to sort the array 'a'

# Write a NumPy function to sort the array 'a' along axis=0

# Write a NumPy function to sort the array 'a' along axis=1

# Write a NumPy function to sort the array 'a' in descending order along axis=0


#def sort_array_flat(a):
#    return np.sort(a, axis=None)
#def sort_array_axis0(a):
#    return np.sort(a, axis=0)
#def sort_array_axis1(a):
#    return np.sort(a, axis=1)
#def sort_array_axis0_descending(a):
#    return -np.sort(-a, axis=0)
#print("\nSorted (Flattened):\n", sort_array_flat(a))
#print("\nSorted along axis=0:\n", sort_array_axis0(a))
#print("\nSorted along axis=1:\n", sort_array_axis1(a))
#print("\nSorted along axis=0 (Descending):\n", sort_array_axis0_descending(a))





# Write a NumPy function to argsort the array along axis=0

# Write a NumPy function to argsort the array along axis=1

# def argsort_axis0(a):
#     return np.argsort(a, axis=0)

# def argsort_axis1(a):
#     return np.argsort(a, axis=1)

# print("Original Array:\n", a)
# print("\nArgsort along axis=0:\n", argsort_axis0(a))
# print("\nArgsort along axis=1:\n", argsort_axis1(a))





# Write a NumPy function to concatenate the arrays 'a' and 'b'

# Write a NumPy function to concatenate the arrays 'a' and 'b' along axis = 0

#def concatenate_flat(a, b):
#     return np.concatenate((a.flatten(), b.flatten()))

# def concatenate_axis0(a, b):
#     return np.concatenate((a, b), axis=0)

# print("Concatenate Flattened:\n", concatenate_flat(a, b))
# print("\nConcatenate along axis=0:\n", concatenate_axis0(a, b))







# Write a NumPy function to get the Number of dimensions

# Write a NumPy function to get the Shape of the array

# Write a NumPy function to get the Size of the array


# def get_num_dimensions(array):
#     return array.ndim

# def get_shape(array):
#     return array.shape

# def get_size(array):
#     return array.size

# print("Number of Dimensions:", get_num_dimensions(a))
# print("Shape of the Array:", get_shape(a))
# print("Size of the Array:", get_size(a))







# Write a NumPy function to Reshape the array 'a' to the dimension (1,9)

# def reshape_to_1x9(array):
#     return array.reshape(1, 9)

# reshaped = reshape_to_1x9(a)
# print("Reshaped Array (1, 9):\n", reshaped)






# Write a NumPy function to add a new axis to the array 'a'
# def add_new_axis(array):
#     return array[np.newaxis, :, :]  
# expanded = add_new_axis(a)
# print("Array with New Axis:\n", expanded)
# print("New Shape:", expanded.shape)






#a = np.array([[4,6,0], [0, 3, 1], [1, 8, 5]])



# Write a NumPy function to index and slice NumPy arrays similar to Python lists
# Show all three - indexing by a integer, indexing by a tuple, using range


# def demonstrate_indexing_slicing(array):
    
#     row_0 = array[0]
    
#     element_1_2 = array[1, 2]
    
#     slice_rows_cols = array[0:2, 0:2]

#     return row_0, element_1_2, slice_rows_cols

# row, element, subarray = demonstrate_indexing_slicing(a)

# print("Integer Indexing (row 0):\n", row)
# print("\nTuple Indexing (element at [1,2]):", element)
# print("\nRange-based Slicing ([0:2, 0:2]):\n", subarray)






# Write a NumPy function to select values satisfying a specific condition like Values greater than 4

# Write a NumPy function to select values satisfying mulitple conditions like Values greater than 4 and divisible by 2

# def select_greater_than_4(array):
#     return array[array > 4]

# print("Values > 4:\n", select_greater_than_4(a))
# Select values > 4 and divisible by 2
# def select_greater_than_4_and_even(array):
#     return array[(array > 4) & (array % 2 == 0)]
# print("Values > 4 and divisible by 2:\n", select_greater_than_4_and_even(a))






# Write a NumPy function to copy the array 'a' and finally print an array where all elements are increased by 1

# def copy_and_increment(array):
#     copied = array.copy()
#     incremented = copied + 1
#     return incremented
# result = copy_and_increment(a)
# print("Copied and Incremented Array:\n", result)






#url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])




# Write a Pandas function to drop rows that contain a missing value.


# df = pd.DataFrame(iris_2d, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

# def drop_missing_rows(dataframe):
#     return dataframe.dropna()

# clean_df = drop_missing_rows(df)

# print("Original shape:", df.shape)
# print("Shape after dropping missing rows:", clean_df.shape)







# Write a Pandas function to find the correlation between the first two columns.

# df = pd.DataFrame(iris_2d, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

# def find_correlation_between_first_two(df):
#     return df.iloc[:, :2].corr()

# correlation = find_correlation_between_first_two(df)
# print("Correlation between the first two columns:\n", correlation)






# Write a Pandas function to find the mean, median and standard deviation of column 3.

# df = pd.DataFrame(iris_2d, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

# def column_stats(df):
#     col = df.columns[2]  
#     stats = {
#         'mean': df[col].mean(),
#         'median': df[col].median(),
#         'std_dev': df[col].std()
#     }
#     return stats
# stats_result = column_stats(df)
# print("Column 3 Statistics (Petal Length):\n", stats_result)







# Write a Pandas function to create a new column for volume in iris_2d, where volume is (pi x petallength x sepal_length^2)/3

# df = pd.DataFrame(iris_2d, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

# def add_volume_column(df):
#     df['volume'] = (math.pi * df['petal_length'] * (df['sepal_length'] ** 2)) / 3
#     return df

# df_with_volume = add_volume_column(df)
# print(df_with_volume.head())








#Let x = np.arange(4, dtype=np.int64). Create an array of ones with the same shape and type as X.

# x = np.arange(4, dtype=np.int64)
# ones_array = np.ones_like(x)

# print(ones_array)
# print(ones_array.dtype)








#Let x be an array [1, 2, 3, ..., 9]. Split x into 3 arrays, each of which has 4, 2, and 3 elements in the original order.

# x = np.arange(1, 10)  
# split_indices = [4, 6]

# arrays = np.split(x, split_indices)

# for arr in arrays:
#     print(arr)






#Initiate x as a 2x5 array with random values from 0 to 10(not inclusive).Get the maximum and minimum values and their indices of x along the second axis.

# x = np.random.randint(0, 10, size=(2, 5))
# print("x:\n", x)

# max_values = np.max(x, axis=1)
# max_indices = np.argmax(x, axis=1)

# min_values = np.min(x, axis=1)
# min_indices = np.argmin(x, axis=1)

# print("\nMax values along axis 1:", max_values)
# print("Indices of max values along axis 1:", max_indices)

# print("\nMin values along axis 1:", min_values)
# print("Indices of min values along axis 1:", min_indices)








# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris = np.genfromtxt(url, delimiter=',', dtype='object')
# names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')






#Write a Pandas function to bin the petal length (3rd) column of iris_2d to form a text array, such that if petal length is:
#Less than 3 –> ‘small’
#3-5 –> ‘medium’
#greater than equal to 5 –> ‘large’

# iris_df = pd.DataFrame(iris, columns=names)

# iris_df['petallength'] = pd.to_numeric(iris_df['petallength'], errors='coerce')

# def petal_length_bin(pl):
#     if pl < 3:
#         return 'small'
#     elif 3 <= pl < 5:
#         return 'medium'
#     else:
#         return 'large'

# iris_df['petal_length_bin'] = iris_df['petallength'].apply(petal_length_bin)

# print(iris_df[['petallength', 'petal_length_bin']].head(10))








#Write a Pandas function to find the most frequent value of petal length (3rd column) in iris dataset


# iris_df = pd.DataFrame(iris, columns=names)

# iris_df['petallength'] = pd.to_numeric(iris_df['petallength'], errors='coerce')

# iris_df = iris_df.dropna(subset=['petallength'])

# most_frequent = iris_df['petallength'].mode().iloc[0]

# print("Most frequent petal length:", most_frequent)

