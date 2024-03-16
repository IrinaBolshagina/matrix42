from vector import Vector
from matrix_from_vector import Matrix


if __name__ == '__main__':

    print('\n------------ vectors ------------\n')

    v1 = Vector([1,2,0,0])
    v2 = Vector([2,3,0,1])
    v1 = v2

    print('vector1=')
    v1.print()
    print()

    print('vector2=')
    v2.print()
    print()

    print('\n------- vectors addidtion -------\n')

    print('vector1+vector2=')
    print(v1+v2,'\n')

    # print('vector1-vector2=')
    # print(v1-v2, '\n')

    # print('vector1*2=')
    # print(2*v1, '\n')

    print('\n------------ matrix ------------\n')

    m1 = Matrix([[1,2,0,1], [0,0,0,2]])
    m2 = Matrix([[1,2,0,1], [0,0,0,0]])
    print(m1)
    m2.print()
    print(m1.shape())

    print('\n------- matrix addidtion -------\n')
    print("matrix1 + matrix2 = ")
    m = m1+m2
    print(m)