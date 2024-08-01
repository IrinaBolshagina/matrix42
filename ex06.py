from vector import Vector
from vector import cross_product

if __name__ == '__main__':
    v1 = Vector([0, 0, 1])
    v2 = Vector([1, 0, 0])
    print("cross product for [0, 0, 1], [1, 0, 0] = ")
    print(cross_product(v1,v2),'\n')

    v3 = Vector([1, 2, 3])
    v4 = Vector([4, 5, 6])
    print("cross product for [1, 2, 3], [4, 5, 6] = ")
    print(cross_product(v3,v4),'\n')

    v5 = Vector([4, 2, -3])
    v6 = Vector([-2, -5, 16])
    print("cross product for [4, 2, -3], [-2, -5, 16] = ")
    print(cross_product(v5,v6),'\n')

    print("------------- bonus -------------\n")

    v7 = Vector([1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j])
    v8 = Vector([2.0 + 1.0j, 3.0 + 2.6j, 4.7 + 3.2j])
    print("cross product for vectors of complex numbers: \n")
    print("[1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j] and [2 + 1j, 3 + 2j, 4 + 3j] = ")
    print(cross_product(v7,v8), '\n')
