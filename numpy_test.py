import numpy as np

x = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print(x.shape)
print(x)

y = np.array([1, 2, 3, 4])
print(y)

z = np.array([0, 0, 0, 1])
print(y)

print(y + z)
print(np.add(y,z))

m = np.matrix([[1, 2], [3, 4]])
print(m)