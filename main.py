from vector import Vector, Matrix


if __name__ == '__main__':

    v = Vector([1,2])
    m = Matrix([[1,2,3,2], [3,4,5,0], [0,0,0,0]])

    # m1 = Matrix([1,2])

    v.print()
    print(v.size())
    m.print()
    print(m.shape())
    v1 = m.reshape()
    v1.print()
    # m1 = v.reshape()
    # m1.print()