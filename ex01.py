
from vector import Vector, linear_combination


if __name__ == '__main__':

    v1 = Vector([1.0, 0.0, 0.0])
    v2 = Vector([0.0, 1.0, 0.0])
    v3 = Vector([0.0, 0.0, 1.0])
    a = [10.0, -2.0, 0.5]

    print("\nLinear combination of vectors ([1,0,0], [0,1,0], [0,0,1] and scalars [10,-2,0.5] = )\n")
    print(linear_combination([v1,v2,v3], a), '\n')
    
    v4 = Vector([1, 2, 3])
    v5 = Vector([0, 10, -100])
    a = [10, -2]

    print("\nLinear combination of vectors ([1,2,3], [0,10,-100] and scalars [10,-2] = )\n")
    print(linear_combination([v4,v5], a), '\n')


    print("------------bonus------------\n")
    print("Operations for complex numbers: \n")
    v6 = Vector([1.0 + 2.2j, 2.0 + 3.9j])
    v7 = Vector([2.0 + 1.0j, 3.0 + 2.6j])
    a = [10.0 + 2.0j, -2.0 + 1.0j]

    print("\nLinear combination of vectors ([1.0 + 2.2j, 2.0 + 3.9j] and [2 + 1j, 3 + 2j] and scalars [10,-2] = )\n")
    print(linear_combination([v6,v7], a), '\n')
