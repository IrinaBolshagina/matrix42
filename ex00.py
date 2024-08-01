from vector import Vector
from matrix import Matrix


if __name__ == '__main__':

    v1 = Vector([2, 3])
    v2 = Vector([5, 7])

    print("\nAddition and subtraction of vectors:\n")
    print("v1 = ")
    print(v1, '\n')
    print("v2 = ")
    print(v2, '\n')

    print("v1 + v2 = ")
    print(v1 + v2, '\n')

    print("v1 - v2 = ")
    print(v1 - v2, '\n')
    
    
    print("Multiplication of vector by scalar: \n")
    print("v1 * 2 = ")
    print(v1 * 2, '\n')

    print("Addition and subtraction of matrices: \n")
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[7, 4], [-2, 2]])

    print ("m1 = ")
    print(m1, '\n')
    print ("m2 = ")
    print(m2, '\n')
    
    print("m1 + m2 = ")
    print(m1 + m2, '\n')
    
    print("m1 - m2 = ")
    print(m1 - m2, '\n')

    print("Multiplication of matrix by scalar: \n")
    print("2 * m1  = ")
    print(2 * m1, '\n')

    print("------------bonus------------\n")
    
    print("Operations for complex numbers: \n")
    v1 = Vector([1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j])
    v2 = Vector([2.0 + 1.0j, 3.0 + 2.6j, 4.7 + 3.2j])
    
    print("v1 = ")
    print(v1, '\n')
    print("v2 = ")
    print(v2, '\n')

    print("v1 + v2 = ")
    print(v1 + v2, '\n')

    print("v1 - v2 = ")
    print(v1 - v2, '\n')

    print("v1 * (2.0 + 3.0j) = ")
    print(v1 * (2.0 + 3.0j), '\n')