from matrix import Matrix

if __name__ == '__main__':

    print("Transpose of matrix: \n")
    m1 = Matrix([[1, 0], 
                 [0, 1]])
    print("Matrix:")
    print(m1,  '\n')
    print("Transpose:")
    print(m1.transpose(), '\n')

    m2 = Matrix([[2, -5, 0],    
                [4, 3, 7],
                [-2, 3, 4]])
    print("Matrix:")
    print(m2,  '\n')
    print("Transpose:")
    print(m2.transpose(), '\n')

    m3 = Matrix([[0, 1, 2],
                [3, 4, 5]])
    print("Matrix:")
    print(m3,  '\n')
    print("Transpose:")
    print(m3.transpose(), '\n')

    print("------------bonus------------\n")
    print("Conjugate transpose of matrix of complex numbers: \n")
    m4 = Matrix([[1.0 + 2.2j, 5],
                [0.0, 4.0 - 5.0j]])
    print("Matrix:")
    print(m4,  '\n')
    print("Conjugate transpose:")
    print(m4.transpose(), '\n')
