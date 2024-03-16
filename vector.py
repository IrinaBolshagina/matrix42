
class Vector:
    
     # Usage: v = Vector([1,2])
    def __init__(self, vect: list):
        self.vect = vect
    
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
        str_list = ['['+ str(v) + ']' for v in self.vect]
        return('\n'.join(str_list))
    
    # Operator+ overload
    def __add__(self, other):
        assert isinstance(other, Vector), "ValueError: can only add vector type"
        assert len(self.vect) == len(other.vect), "ValueError: can only add vectors that have equal length"
        sum_vect = [self.vect[i]+other.vect[i] for i in range(len(self.vect))]
        return Vector(sum_vect)
    
    # Operator- overload
    def __sub__(self, other):
        assert isinstance(other, Vector), "ValueError: can only substract vector type"
        assert len(self.vect) == len(other.vect), "ValueError: can only substract vectors that have equal lenghth"
        sub_vect = [self.vect[i]-other.vect[i] for i in range(len(self.vect))]
        return Vector(sub_vect)

    # Operator* overload    
    def __mul__(self, other):
        mul_vect = [self.vect[i]*other for i in range(len(self.vect))]
        return Vector(mul_vect)
    
    # Reversed operator* overload
    def __rmul__(self, other):
        mul_vect = [self.vect[i]*other for i in range(len(self.vect))]
        return Vector(mul_vect)
