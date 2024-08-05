from vector import Vector
from matrix import Matrix

if __name__ == '__main__':

    m1 = Matrix([[1, 0], [0, 1]])
    v1 = Vector([4, 2])

    print("\nMultiplication of matrix by vector: \n")
    print("Matrix:")
    print(m1,  '\n')
    print("Vector:")
    print(v1,  '\n')
    print("Result:")
    print(m1.mul_vec(v1), '\n')

    m2 = Matrix([[2, 0], [0, 2]])
    v2 = Vector([4, 2])

    print("Matrix:")
    print(m2,  '\n')
    print("Vector:")
    print(v2,  '\n')
    print("Result:")
    print(m2.mul_vec(v2), '\n')

    m3 = Matrix([[2, -2], [-2, 2]])
    v3 = Vector([4, 2])

    print("Matrix:")
    print(m3,  '\n')
    print("Vector:")
    print(v3,  '\n')
    print("Result:")
    print(m3.mul_vec(v3), '\n')

    m4 = Matrix([[1, 0], [0, 1]])
    m5 = Matrix([[1, 0], [0, 1]])

    print("Matrix:")
    print(m4,  '\n')
    print("Matrix:")
    print(m5,  '\n')
    print("Result:")
    print(m4.mul_mat(m5), '\n')

    m6 = Matrix([[1, 0], [0, 1]])
    m7 = Matrix([[2, 1], [4, 2]])

    print("Matrix:")
    print(m6,  '\n')
    print("Matrix:")
    print(m7,  '\n')
    print("Result:")
    print(m6.mul_mat(m7), '\n')

    m8 = Matrix([[3, -5], [6, 8]])
    m9 = Matrix([[2, 1], [4, 2]])

    print("Matrix:")
    print(m8,  '\n')
    print("Matrix:")
    print(m9,  '\n')
    print("Result:")
    print(m8.mul_mat(m9), '\n')


    print("------------bonus------------\n")
    print("Operations for complex numbers: \n")

    m10 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j], [3.0 + 4.0j, 4.0 + 5.0j]])
    v4 = Vector([1.0 + 2.2j, 2.0 + 3.9j])

    print("Matrix:")
    print(m10,  '\n')
    print("Vector:")
    print(v4,  '\n')
    print("Result:")
    print(m10.mul_vec(v4), '\n')
    
