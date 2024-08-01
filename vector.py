# check if the input is a list
# check if all the elements in the list are of the same type

# import math
# import cmath

class Vector:
    
    # Usage: v = Vector([1,2])
    def __init__(self, vect):
        self.vect = vect.copy()
    
    # A function to return the size of a vector
    def size(self):
        return len(self.vect)
    
    # A function to print a vector on the standard output
    def print(self):
        print(self)
    
    # A function to reshape a vector into a matrix
    def reshape(self):
        from matrix import Matrix
        return(Matrix(self.vect))
    
    # Operator[] overoad
    def __getitem__(self, key):
        return self.vect[key]

    # Print overload
    def __str__(self):
        if isinstance(self.vect[0], float):
            str_list = ['['+ str('%.1f' % v) + ']' for v in self.vect]
        else:
            str_list = ['['+ str(v) + ']' for v in self.vect]
        return('\n'.join(str_list))
    
    # Operator+ overload
    def __add__(self, other):
        if not isinstance(other, Vector) or self.size() != other.size():
            raise ValueError("Can only add two vectors of the same demention")
        sum_vect = [self.vect[i]+other.vect[i] for i in range(len(self.vect))]
        return Vector(sum_vect)
    
    # Operator- overload
    def __sub__(self, other):
        if not isinstance(other, Vector) or self.size() != other.size():
            raise ValueError("Can only substract vectors of the same demention")
        sub_vect = [self.vect[i]-other.vect[i] for i in range(len(self.vect))]
        return Vector(sub_vect)

    # Operator* overload for scalar and dot product   
    def __mul__(self, other):
        
        #multiplication to scalar
        if isinstance(other, type(self.vect[0])):
            mul_vect = [self.vect[i]*other for i in range(len(self.vect))]
            return Vector(mul_vect)
        
        #dot product
        elif isinstance(self, type(other)):
            if self.size() != other.size():
                raise ValueError("Two vectors must be of the same dimension to calculate dot product")
            dot = sum([self.vect[i]*other.vect[i] for i in range(len(self.vect))])
            return dot
        # else:
        #     raise ValueError("Vector and scalar must have the same data type for multiplication")

    
    # Reversed operator* overload
    def __rmul__(self, other):
        if not isinstance(other, type(self.vect[0])):
            raise ValueError("Vector and scalar must have the same data type for multiplication")
        mul_vect = [self.vect[i]*other for i in range(len(self.vect))]
        return Vector(mul_vect)

    
# a1*v1 + a2*v2 + a3*v3 + ...
def linear_combination(list_vect, list_scal):
    res = 0
    for v, s in zip(list_vect, list_scal):
        if res == 0:
            res = v * s
        else:
            res += v * s
    return(res)


def dot(v1, v2):
    if v1.size() != v2.size():
        raise ValueError("Two vectors must be of the same dimension to calculate dot product")
    dot = sum(v1.vect[i]*v2.vect[i] for i in range(len(v1.vect)))
    return dot


# linear_interpolation
def lerp(point1, point2, t):
    # check point1, point2 are of the same type
    # check if t is a scalar 
    # (type equals to point1, point2 or equals to type of the element of point1, point1)
    return (1.0 - t) * point1 + t * point2


# manhattan norm p(x) = |x1| + |x2| + ... + |xn|
def norm_1(vect):
    # for v in vect:
    #     print(v)
    return sum(abs(v) for v in vect).real


# euclidean norm p(x) = sqrt(x1^2 + x2^2 + ... + xn^2)
def norm(vect):
    return (sum(v*v for v in vect) ** 0.5).real


# supremum norm 
def norm_inf(vect):
    return max(abs(v) for v in vect).real


def angle_cos(v1, v2):
    cos = dot(v1,v2) / (norm(v1) * norm(v2))
    
    if type(cos) == float:
        return round(cos, 9) # this is to avoid floating point errors
    else:
        return cos