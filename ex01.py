
from vector import Vector, linear_combination
from matrix_from_vector import Matrix

# a1*v1 + a2*v2 + a3*v3 + ...
# [a1,a2,a3, ...] - list of numbers, [v1,v2,v3,...] - list of vectors
def linear_combination1(list_vect, list_scal):
    res = 0
    for v, s in zip(list_vect, list_scal):
        if res == 0:
            res = v * s
        else:
            res += v * s
    print(res)



if __name__ == '__main__':

    v1 = Vector([1,2,3])
    v2 = Vector([0,10,-100])
    v3 = Vector([0,0,1])
    a = [10,-2]

    res = linear_combination([v1,v2], a)
    print(res)
