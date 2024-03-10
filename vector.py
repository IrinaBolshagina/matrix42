
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
        return(Matrix(self.vect))

    # Print overload
    def __str__(self):
        str_list = ['['+ str(v) + ']' for v in self.vect]
        return('\n'.join(str_list))
    
    # operator+ overload
    def __add__(self, other):
        assert isinstance(other, Vector), "ValueError: can only add vector type"
        assert len(self.vect) == len(other.vect), "ValueError: can only add vectors that have equal lenghth"
        sum_vect = [self.vect[i]+other.vect[i] for i in range(len(self.vect))]
        return Vector(sum_vect)
    
    # operator- overload
    def __sub__(self, other):
        assert isinstance(other, Vector), "ValueError: can only substract vector type"
        assert len(self.vect) == len(other.vect), "ValueError: can only substract vectors that have equal lenghth"
        sub_vect = [self.vect[i]-other.vect[i] for i in range(len(self.vect))]
        return Vector(sub_vect)

    # operator* overload    
    def __mul__(self, other):
        mul_vect = [self.vect[i]*other for i in range(len(self.vect))]
        return Vector(mul_vect)
    
    # reversed operator* overload
    def __rmul__(self, other):
        mul_vect = [self.vect[i]*other for i in range(len(self.vect))]
        return Vector(mul_vect)



class Matrix:

    rows = 0
    columns = 0

    # Usage: m = Matrix([[1, 2], [3, 4]])
    def __init__(self, matr: list):
       
        # if type(matr[0]) is list:
        self.matr = matr
        self.rows = len(self.matr)
        try:
            self.columns = len(self.matr[0]) # one-dimentional matrix
        except:
            columns = 0

    
    # A function to return the shape of a matrix
    # returnes tuple of array dimentions
    def shape(self):
        # self.rows = len(self.matr)
        # try:
        #     self.columns = len(self.matr[0])
        # except:
        #     print(self.rows)
        #     print(self.columns)
        #     return(self.rows,)
        # print(self.rows)
        # print(self.columns)
        # return(self.rows,self.columns)
        if self.columns == 0:
            return (self.rows,)
        return(self.rows,self.columns)
    # A function to print a matrix on the standard output
    def print(self):
        print(self.rows)
        print(self.columns)
        if (self.columns) == 0:
            print(self.matr)
        else:
            print('[', end='')
            print(self.matr[0])
            i = 1
            while i < self.rows-1:
                print('', self.matr[i])
                i = i+1
            print('', self.matr[i], end='')
            print(']')
    
    # A function to reshape a matrix into a vector
    def reshape(self):
        vect = [element for row in self.matr for element in row]
        # return(vect)
        return(Vector(vect))