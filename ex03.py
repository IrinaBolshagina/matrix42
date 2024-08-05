from vector import Vector


if __name__ == '__main__':
    v1 = Vector([0, 0])
    v2 = Vector([1, 1])
    print("Dot product of [0, 0], [1,1] = ")
    print(v1.dot(v2),'\n')

    v1 = Vector([1, 1])
    v2 = Vector([1, 1])
    print("Dot product of [1, 1] and [1,1] = ")
    print(v1.dot(v2),'\n')

    v1 = Vector([-1, 6])
    v2 = Vector([3, 2])
    print("Dot product of [-1, 6] and [3, 2] = ")
    print(v1.dot(v2),'\n')

    print("Dot product of [-1, 6] and [3, 2] = ")
    print(v1.dot(v2),'\n')

    # complex vectors example
    print("------------- bonus -------------\n")

    v1 = Vector([1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j])
    v2 = Vector([2.0 + 1.0j, 3.0 + 2.6j, 4.7 + 3.2j])
    print("Dot product for vectors of complex numbers: \n")
    print("[1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j] and [2 + 1j, 3 + 2j, 4 + 3j] = ")
    print(v1.dot(v2), '\n')

