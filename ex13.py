from matrix import Matrix

if __name__ == '__main__':
    print("\nRank of matrix: \n")
    m1 = Matrix([[1., 0., 0.],
                 [0., 1., 0.],
                 [0., 0., 1.]])
    print("Matrix:")
    print(m1,  '\n')
    print("Rank:")
    print(m1.rank(), '\n')

    m2 = Matrix([[ 1., 2., 0., 0.],
                 [ 2., 4., 0., 0.],
                 [-1., 2., 1., 1.]])
    print("Matrix:")
    print(m2,  '\n')
    print("Rank:")
    print(m2.rank(), '\n')

    m3 = Matrix([[ 8., 5., -2.],
                 [ 4., 7., 20.],
                 [ 7., 6., 1.],
                 [21., 18., 7.]])
    print("Matrix:")
    print(m3,  '\n')
    print("Rank:")
    print(m3.rank(), '\n')

    m4 = Matrix([[4, 2],
                    [2, 1]])
    print("Matrix:")
    print(m4,  '\n')
    print("Rank:")
    print(m4.rank(), '\n')

    print("------------bonus------------\n")
    print("Operations for complex numbers: \n")

    m5 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j],
                 [3.0 + 4.0j, 4.0 + 5.0j]])
    print("Matrix:")
    print(m5,  '\n')
    