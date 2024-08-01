from vector import Vector, lerp
from matrix import Matrix


if __name__ == '__main__':
    print("\nLinear_interpolation for real numbers 0.0, 1.0, 1.0")
    print(lerp(0.0, 1.0, 1.0), '\n')

    v1 = Vector([1.0, 1.0])
    v2 = Vector([7.0, 5.0])
    t = 0.5
    print("Linear_interpolation for vectors [2.0, 1.0],[4.0, 2.0] and scalar 0.3 ")
    print(lerp(v1,v2,t), '\n')

    m1 = Matrix([[1,2,0,1], [1,2,1,0]])
    m2 = Matrix([[2,2,5,0], [6,0,0,1]])
    t = 0.3
    print(lerp(m1,m2,t))

    print("\n------------bonus------------")
    print("Operations for complex numbers: \n")

    v1 = Vector([1.0 + 2.2j, 2.0 + 3.9j])
    v2 = Vector([2.0 + 1.0j, 3.0 + 2.6j])
    t = 0.3
    print("Linear_interpolation([1.0 + 2.2j, 2.0 + 3.9j], [2.0 + 1.0j, 3.0 + 2.6j], 0.3) = ")
    print(lerp(v1,v2,t), '\n')




