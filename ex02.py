from vector import Vector, lerp
from matrix_from_vector import Matrix #, lerp


if __name__ == '__main__':
    print("linear_interpolation(0.0, 1.0, 1.0) = ")
    print(lerp(0.0, 1.0, 1.0), '\n')

    v1 = Vector([1.0, 1.0])
    v2 = Vector([7.0, 5.0])
    t = 0.5
    print("linear_interpolation([2.0, 1.0],[4.0, 2.0], 0.3) = ")
    print(lerp(v1,v2,t), '\n')

    # m1 = Matrix([[1,2,0,1], [1,2,1,0]])
    # m2 = Matrix([[2,2,5,0], [6,0,0,1]])
    # t = 0.3
    # print(lerp(m1,m2,t))




