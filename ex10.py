from matrix import Matrix

if __name__ == '__main__':

    print("Row-echeleon form of matrix: \n")
    m1 = Matrix([[1., 0., 0.],
                 [0., 1., 0.],
                 [0., 0., 1.]])
    print("Matrix:")
    print(m1,  '\n')
    print("Row-echeleon form:")
    print(m1.row_echelon(), '\n')

    m2 = Matrix([[1., 2.],
                 [3., 4.]])
    print("Matrix:")
    print(m2,  '\n')
    print("Row-echeleon form:")
    print(m2.row_echelon(), '\n')

    m3 = Matrix([[1., 2.],
                 [2., 4.]])
    print("Matrix:")
    print(m3,  '\n')
    print("Row-echeleon form:")
    print(m3.row_echelon(), '\n')

    m4 = Matrix([[8., 5., -2., 4., 28.],
                 [4., 2.5, 20., 4., -4.],
                 [8., 5., 1., 4., 17.]])
    print("Matrix:")
    print(m4,  '\n')
    print("Row-echeleon form:")
    print(m4.row_echelon(), '\n')

    print("------------bonus------------\n")
    print("Operations for complex numbers: \n")

    m5 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j],
                 [3.0 + 4.0j, 4.0 + 5.0j]])
    print("Matrix:")
    print(m5,  '\n')
    print("Row-echeleon form:")
    print(m5.row_echelon(), '\n')

