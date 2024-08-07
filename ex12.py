from matrix import Matrix

if __name__ == '__main__':
    print("\nInverse matrix: \n")
    m1 = Matrix([[1., 0., 0.],
                 [0., 1., 0.],
                 [0., 0., 1.]])
    print("Matrix:")
    print(m1,  '\n')
    print("Inverse matrix:")
    print(m1.inverse(), '\n')

    m2 = Matrix([[2., 0., 0.],
                 [0., 2., 0.],
                 [0., 0., 2.]])
    print("Matrix:")
    print(m2,  '\n')
    print("Inverse matrix:")
    print(m2.inverse(), '\n')

    m3 = Matrix([[8., 5., -2.],
                 [4., 7., 20.],
                 [7., 6., 1.]])
    print("Matrix:")
    print(m3,  '\n')
    print("Inverse matrix:")
    print(m3.inverse(), '\n')
    
    # error case with singular matrix
    '''
    m4 = Matrix([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
    print("Matrix:")
    print(m4,  '\n')
    print("Inverse matrix:")
    print(m4.inverse(), '\n')
    '''

    print("------------bonus------------\n")
    print("Operations for complex numbers: \n")

    m5 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j],
                 [3.0 + 4.0j, 4.0 + 5.0j]])
    print("Matrix:")
    print(m5,  '\n')
    print("Inverse matrix:")
    print(m5.inverse(), '\n')
