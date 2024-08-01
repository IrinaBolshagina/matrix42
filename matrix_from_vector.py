from vector import Vector

class Matrix:

    rows_num = 0
    cols_num = 0

    # Usage: m = Matrix([[1, 2], [3, 4]]) or m = Matrix([v1, v2, v3])
    def __init__(self, matr: list):

        # Matrix from vector of vectors ex: m = Matrix(vect)
        if isinstance(matr, Vector):
            matr = [row for row in matr]

        self.rows_num = len(matr)

        # Matrix from list of vectors ex: m = Matrix([v1, v2, v3])
        if isinstance(matr[0], Vector):
            self.matr = [row.vect for row in matr]
            self.vectors = Vector([row for row in matr])
            self.columns = matr[0].size()
        
        # Matrix from list of lists ex: m = Matrix([[1, 2], [3, 4]])
        elif isinstance(matr[0], list):
            self.matr = matr
            self.vectors = Vector([Vector(row) for row in matr])
            self.columns = len(matr[0])

        # One-dimentional matrix
        else:
            self.vectors = Vector(matr)
            self.columns = 1

    
    # A function to return the shape of a matrix
    # returnes tuple of array dimentions
    def shape(self):
        if self.columns == 1:
            return (self.rows,)
        return(self.rows,self.columns)
    
    
    # A function to reshape a matrix into a vector
    def reshape(self):
        if self.columns > 1:
            vect = [element for row in self.matr for element in row]
            return(Vector(vect))
        else:
            return(self.matr)
    

    # A function to print a matrix on the standard output
    def print(self):
        print(self)
    
    
    # Overload print()
    def __str__(self):
        if self.columns == 1:
            return(self.vectors.__str__())
        else:
            str_print = []
            for row in self.matr:
                if isinstance(row[0], float):
                    str_row = '['+ ', '.join([str('%.1f'%value) for value in row]) + ']'
                else:
                    str_row = str(row)
                str_print.append(str_row)
    
            #     str_print = [str(row) for row in self.matr]
            # else:
            #     str_print = ['['+ str('{%.1f}'%value) + ']' for value in self.matr]
            return('\n'.join(str_print))


    # Operator+ overload
    def __add__(self, other):
        assert isinstance(other, Matrix), "ValueError: Can only add matrix type"
        assert self.shape() == self.shape(), "ValueError: Can only add matrices that have equal shape"
        return(Matrix(self.vectors + other.vectors))
    
    # Operator- overload
    def __sub__(self, other):
        assert isinstance(other, Matrix), "ValueError: Can only substract matrix type"
        assert self.shape() == self.shape(), "ValueError: Can only substract matrices that have equal lenghth"
        return(Matrix(self.vectors - other.vectors))
    
    # Operator* overload    
    def __mul__(self, other):
        # assert isinstance(other, type(self.vectors[0])), "ValueError: Matrix and scalar must have the same data type for multiplication"
        res = []
        # for v in self.vectors:
        #     res.append(v*other)
        mul_vectors = [self.vectors[i]*other for i in range(self.rows)]
        return Matrix(mul_vectors)
    
    
    # Reversed operator* overload
    def __rmul__(self, other):
        # assert isinstance(other, type(self.vect[0])), "ValueError: Matrix and scalar must have the same data type for multiplication"
        mul_vectors = [self.vectors[i]*other for i in range(self.rows)]
        return Matrix(mul_vectors)
    
# def lerp(m1: Matrix, m2: Matrix, t):
#     a = 1-t
#     print(a)
#     b = m1*a
#     c = t*m2
#     print("b =", b,"\nc =",c)
#     res = b+c
#     return(res)
#     # return (1.0 - t) * m1 + t * m2

