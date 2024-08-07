from matrix import Matrix

if __name__ == '__main__':
    m1 = Matrix([[ 1., -1.],
                 [-1., 1.]])
    print("Matrix:")
    print(m1,  '\n')
    print("Determinant:")
    print(m1.det(), '\n')

    m2 = Matrix([[2., 0., 0.],
                 [0., 2., 0.],
                 [0., 0., 2.]])
    print("Matrix:")
    print(m2,  '\n')
    print("Determinant:")
    print(m2.det(), '\n')

    m3 = Matrix([[8., 5., -2.],
                 [4., 7., 20.],
                 [7., 6., 1.]])
    print("Matrix:")
    print(m3,  '\n')
    print("Determinant:")
    print(m3.det(), '\n')

    m4 = Matrix([[ 8., 5., -2., 4.],
                 [ 4., 2.5, 20., 4.],
                 [ 8., 5., 1., 4.],
                 [28., -4., 17., 1.]])
    print("Matrix:")
    print(m4,  '\n')
    print("Determinant:")
    print(m4.det(), '\n')\
    
    m5 = Matrix([[ 1, 2, 3],
                 [ 4, 5, 6],
                 [ 7, 8, 9]])
    print("Matrix:")
    print(m5,  '\n')
    print("Determinant:")
    print(m5.det(), '\n')

    print("------------bonus------------\n")
    print("Operations for complex numbers: \n")

    m6 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j],
                 [3.0 + 4.0j, 4.0 + 5.0j]])
    print("Matrix:")
    print(m6,  '\n')
    print("Determinant:")
    print(m6.det(), '\n')



    