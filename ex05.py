from vector import Vector
from vector import angle_cos


if __name__ == '__main__':
    v1 = Vector([1, 0])
    v2 = Vector([1, 0])
    print("angle_cos([1, 0], [1, 0]) = ")
    print(angle_cos(v1, v2), '\n')
    
    v3 = Vector([1, 0])
    v4 = Vector([0, 1])
    print("angle_cos([1, 0], [0, 10]) = ")
    print(angle_cos(v3, v4), '\n')
    
    v5 = Vector([-1, 1])
    v6 = Vector([1, -1])
    print("angle_cos([-1, 1], [1, -1]) = ")
    print(angle_cos(v5, v6), '\n')
    
    v7 = Vector([2, 1])
    v8 = Vector([4, 2])
    print("angle_cos([2, 1], [4, 2]) = ")
    print(angle_cos(v7, v8), '\n')
    
    v9 = Vector([1, 2, 3])
    v10 = Vector([4, 5, 6])
    print("angle_cos([1, 2, 3], [4, 5, 6]) = ")
    print(angle_cos(v9, v10), '\n')

    print("------------- bonus -------------\n")
    v11 = Vector([1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j])
    v12 = Vector([2.0 + 1.0j, 3.0 + 2.6j, 4.7 + 3.2j])
    print("angle_cos([1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j], [2 + 1j, 3 + 2j, 4 + 3j]) = ")
    print(angle_cos(v11, v12), '\n')
    