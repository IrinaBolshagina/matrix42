# check if the input is a list

def check_vector(vect):
    assert isinstance(vect, list), "ValueError: input must be a list"

class Vector:
    
    # Usage: v = Vector([1,2])
    def __init__(self, vect):
        check_vector(vect)
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
        str_list = ['['+ str(round(x, 9) if isinstance(x, float) else x) + ']' for x in self.vect]
        return('\n'.join(str_list))
    
    
    # Operator+ overload
    def __add__(self, other):
        sum_vect = [self.vect[i]+other.vect[i] for i in range(len(self.vect))]
        return Vector(sum_vect)
    
    
    # Operator- overload
    def __sub__(self, other):
        sub_vect = [self.vect[i]-other.vect[i] for i in range(len(self.vect))]
        return Vector(sub_vect)
    

    # Operator* overload for scalar   
    def __mul__(self, other):
        mul_vect = [self.vect[i]*other for i in range(len(self.vect))]
        return Vector(mul_vect)
    

    # Reversed operator* overload
    def __rmul__(self, other):
        mul_vect = [self.vect[i]*other for i in range(len(self.vect))]
        return Vector(mul_vect)
    
    
    # dot product of two vectors
    # a*b = a1*b1 + a2*b2 + a3*b3 + ...
    def dot(self, other):
        dot = sum(self.vect[i]*other.vect[i] for i in range(len(self.vect)))
        return dot
    
    
    # manhattan norm p(x) = |x1| + |x2| + ... + |xn|
    def norm_1(self):
        return round(sum(abs(v) for v in self.vect).real, 9)
    

    # euclidean norm p(x) = sqrt(x1^2 + x2^2 + ... + xn^2)
    def norm(self):
        return round((sum(v*v for v in self.vect) ** 0.5).real, 9)
    

    # supremum norm p(x) = max(|x1|, |x2|, ..., |xn|)
    def norm_inf(self):
        return round(max(abs(v) for v in self.vect).real, 9)
    
    
# Linear combination of vectors [v1, v2, ...] and scalars [a1, a2, ...]
# a1*v1 + a2*v2 + a3*v3 + ...
def linear_combination(list_vect, list_scal):
    res = 0
    for v, s in zip(list_vect, list_scal):
        if res == 0:
            res = v * s
        else:
            res += v * s
    return(res)


# linear_interpolation 
def lerp(point1, point2, t):
    # check point1, point2 are of the same type
    # check if t is a scalar 
    # (type equals to point1, point2 or equals to type of the element of point1, point1)
    return (1.0 - t) * point1 + t * point2


# cosine of the angle between two vectors: cos(theta) = (v1 * v2) / (||v1|| * ||v2||)
def angle_cos(v1, v2):
    cos = v1.dot(v2) / (v1.norm() * v2.norm())
    if type(cos) == float:
        return round(cos, 9) # this is to avoid floating point errors
    else:
        return cos
    

# cross product of two vectors in 3D space
def cross_product(v1, v2):
    if v1.size() != 3 or v2.size()!= 3:
        raise ValueError("Vectors must be 3-dimentional")
    cross = [v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0]]
    return Vector(cross)