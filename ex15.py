from vector import Vector
from vector import cross_product, linear_combination, lerp, angle_cos
from matrix import Matrix

if __name__ == '__main__':
    print('\n Bonus: exersises ex00-ex13 for complex numbers')

    v1 = Vector([1.0 + 2.2j, 2.0 + 3.9j])
    v2 = Vector([3.0 + 4.0j, 4.0 + 5.0j])
    m1 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j],
                [3.0 + 4.0j, 4.0 + 5.0j]])
    m2 = Matrix([[1.0 + 1.0j, 5.0 - 2.0j],
                [0.0 + 0.0j, 2.0 - 3.0j]])
    
    #00
    print("Addition, substruction and scale for vectors")
    print("\nVectors:")
    print(v1)
    print(v2)
    print("\nVectors addition:")
    print(v1 + v2)
    print("\nVectors subtraction:")
    print(v1 - v2)
    print("\nVectors scale v1*2:")
    print(v1 * 2)

    print("Addition, substruction and scale for mitrices")

    print("\nMatrices:")
    print(m1)
    print(m2)
    print("\nMatrices addition:")
    print(m1 + m2)
    print("\nMatrices subtraction:")
    print(m1 - m2)
    print("\nMatrices scale v1*2:")
    print(m1 * 2)

    #01
    v6 = Vector([1.0 + 2.2j, 2.0 + 3.9j])
    v7 = Vector([2.0 + 1.0j, 3.0 + 2.6j])
    a = [10.0 + 2.0j, -2.0 + 1.0j]

    print("\nLinear combination of vectors:\n[1.0 + 2.2j, 2.0 + 3.9j] and [2 + 1j, 3 + 2j] and scalars [10,-2]:\n")
    print(linear_combination([v6,v7], a), '\n')

    #02
    v1 = Vector([1.0 + 2.2j, 2.0 + 3.9j])
    v2 = Vector([2.0 + 1.0j, 3.0 + 2.6j])
    t = 0.3
    print("Linear_interpolation for vectors: \n[1.0 + 2.2j, 2.0 + 3.9j], [2.0 + 1.0j, 3.0 + 2.6j], 0.3")
    print(lerp(v1,v2,t), '\n')

    #03
    v1 = Vector([1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j])
    v2 = Vector([2.0 + 1.0j, 3.0 + 2.6j, 4.7 + 3.2j])
    print("Dot product for vectors: ")
    print("[1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j] and [2 + 1j, 3 + 2j, 4 + 3j] = ")
    print(v1.dot(v2), '\n')

    #04
    v5 = Vector([1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j])
    print("Norm for vector:")
    print(v5)
    print(f"norm_1 = {v5.norm_1()}, norm = {v5.norm()}, norm_inf = {v5.norm_inf()}\n") # 10.1, 6.0, 3.0

    #05
    v11 = Vector([1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j])
    v12 = Vector([2.0 + 1.0j, 3.0 + 2.6j, 4.7 + 3.2j])
    print("Cosine of vectors:\n[1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j], [2 + 1j, 3 + 2j, 4 + 3j] =")
    print(angle_cos(v11, v12), '\n')

    #06
    v7 = Vector([1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j])
    v8 = Vector([2.0 + 1.0j, 3.0 + 2.6j, 4.7 + 3.2j])
    print("Cross product for vectors:")
    print("[1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j] and [2 + 1j, 3 + 2j, 4 + 3j] =")
    print(cross_product(v7,v8), '\n')

    #07
    print("\nMultiplication of matrix by vector:")
    m10 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j], [3.0 + 4.0j, 4.0 + 5.0j]])
    v4 = Vector([1.0 + 2.2j, 2.0 + 3.9j])
    print("Matrix:")
    print(m10,  '\n')
    print("Vector:")
    print(v4,  '\n')
    print("Result:")
    print(m10.mul_vec(v4), '\n')

    #08
    print("Trace of matrix:")
    m4 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j],
                [3.0 + 4.0j, 4.0 + 5.0j]])
    print("Matrix:")
    print(m4,  '\n')
    print("Trace:")
    print(m4.trace(), '\n')

    #09
    print("Conjugate transpose of matrix: \n")
    m4 = Matrix([[1.0 + 2.2j, 5],
                [0.0, 4.0 - 5.0j]])
    print("Matrix:")
    print(m4,  '\n')
    print("Conjugate transpose:")
    print(m4.transpose(), '\n')

    #10
    print("\nRow echelon form of matrix:")
    m5 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j],
                 [3.0 + 4.0j, 4.0 + 5.0j]])
    print("Matrix:")
    print(m5,  '\n')
    print("Row-echeleon form:")
    print(m5.row_echelon(), '\n')

    #11
    print("Determinant of a matrix:")
    m6 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j],
                 [3.0 + 4.0j, 4.0 + 5.0j]])
    print("Matrix:")
    print(m6,  '\n')
    print("Determinant:")
    print(m6.det(), '\n')

    #12
    print("Inverse matrix: \n")
    m5 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j],
                 [3.0 + 4.0j, 4.0 + 5.0j]])
    print("Matrix:")
    print(m5,  '\n')
    print("Inverse matrix:")
    print(m5.inverse(), '\n')

    #13
    print("Rank of matrix: \n")
    m5 = Matrix([[1.0 + 2.2j, 2.0 + 3.9j],
                 [3.0 + 4.0j, 4.0 + 5.0j]])
    print("Matrix:")
    print(m5,  '\n')



    

