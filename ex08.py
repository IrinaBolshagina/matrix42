from matrix import Matrix

if __name__ == '__main__':

    m1 = Matrix([[1, 0], [0, 1]])

    print("\nTrace of matrix: \n")
    print("Matrix:")
    print(m1,  '\n')
    print("Trace:")
    print(m1.trace(), '\n')

    m2 = Matrix([[2, -5, 0],
                 [4, 3, 7],
                 [-2, 3, 4]])
    
    print("Matrix:")
    print(m2,  '\n')
    print("Trace:")
    print(m2.trace(), '\n')

    m3 = Matrix([[-2., -8., 4.],
                 [1., -23., 4.],
                 [0., 6., 4.]])
    
    print("Matrix:")
    print(m3,  '\n')
    print("Trace:")
    print(m3.trace(), '\n')

    print("------------bonus------------\n")
    print("Operations for complex numbers: \n")

    m4 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j],
                [3.0 + 4.0j, 4.0 + 5.0j]])
    print("Matrix:")
    print(m4,  '\n')
    print("Trace:")
    print(m4.trace(), '\n')


