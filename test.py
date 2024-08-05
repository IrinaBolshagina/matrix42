from vector import Vector
from matrix import Matrix

if __name__ == '__main__':
    v1 = Vector([0, 0])
    v2 = Vector([1.0, 1.8])
    v3 = Vector([1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j])

    print(v1)
    print(v2)
    print(v3)

    complex_number = 1.0 + 2.2j
    print(complex_number)
    print(complex_number.conjugate())