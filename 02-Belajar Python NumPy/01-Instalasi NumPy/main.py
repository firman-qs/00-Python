import numpy as np

array_numpy = np.array([1, 2, 3, 4, 5])
array_biasa = [1, 2, 3, 4, 5]

print(f"array numpy : {array_numpy}") # without comma saparator
print(f"array biasa : {array_biasa}") # with comma saparator

# whats the difference? let see
array_numpy += 1 # add 1 for each component in array
# array_biasa += 1 # will error

print(f"array numpy : {array_numpy}") 
# print(f"array biasa : {array_biasa}") 

