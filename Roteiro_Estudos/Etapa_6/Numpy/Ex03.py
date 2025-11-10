import numpy as np

# print(np.__version__)  # mostra a version do numpy

# array = np.array([1, 2, 3, 4, 5])
# array *= 2
# print(array)
# print(type(array))

# array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
#                   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
#                   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', 'S']]])

# palavra = array[0,1,1] + array[0,0,2] + array[1,1,2] + array[0,0,0] # ECOA com matriz

# print(palavra)


array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#array[start:end:step]

print(array[2:, 2:])


 







