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

print(y*z)

v1 = np.array([1,2,1])
v2 = np.array([0,0,1])
m1 = np.array([v1,v2])

print(v1)
print(v2)
print(m1)
print("dot")
print(v1*v2)
print("scale")
print(v1*2)