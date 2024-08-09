from vector import Vector
from matrix import Matrix

if __name__ == '__main__':
    print('\n Bonus: all the exersises ex00-ex13 for complex numbers')

    print("\nVector operations: \n")
    v1 = Vector([1.0 + 2.2j, 2.0 + 3.9j])
    v2 = Vector([3.0 + 4.0j, 4.0 + 5.0j])
    print("Vectors:")
    print(v1)
    print(v2)
    print("Addition:")
    print(v1 + v2)
    print("Subtraction:")
    print(v1 - v2)
    print("Multiplication:")
    print(v1 * v2)
    print("Dot product:")
    print(v1.dot(v2))
    print("Cross product:")
    print(v1.cross(v2))
    print("Norm:")
    print(v1.norm())
    

