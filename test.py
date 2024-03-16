from vector_from_matrix import Vector
from matrix import Matrix


if __name__ == '__main__':

    print('\n------------ vectors ------------\n')

    v1 = Vector([1,2,0,0])
    v2 = Vector([2,3,0,1])

    print('vector1=')
    v1.print()
    print()

    print('vector2=')
    v2.print()
    print()

    print('\n------- vectors addidtion -------\n')

    # print('vector1+vector2=')
    # print(v1+v2,'\n')

    # print('vector1-vector2=')
    # print(v1-v2, '\n')

    # print('vector1*2=')
    # print(2*v1, '\n')

    m1 = Matrix([1,2,0,1])
    m2 = Matrix([[1,2,0,1], [0,0,0,0]])
    print(m1)
    m2.print()
    print(m1.shape())