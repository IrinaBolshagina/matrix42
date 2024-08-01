from vector import Vector

# check if input is a list
# check if elements have the same type
# check if dimensions are the same for all rows
# make input for one-dimentional matrix as a simple list

def check_matrix(matr: list):
    assert isinstance(matr, list), "ValueError: input must be a list"
    # assert all(isinstance(row, list) for row in matr), "ValueError: input must be a list of lists"
    assert all(len(row) == len(matr[0]) for row in matr), "ValueError: all rows must have the same length"
    assert all(isinstance(element, type(matr[0][0])) for row in matr for element in row), "ValueError: all elements must have the same type"

class Matrix:

    rows_num = 0
    cols_num = 0

    # Usage: m = Matrix([[1, 2], [3, 4]]) or for one-dimentional matrix: m = Matrix([1, 2, 3, 4])
    def __init__(self, data: list):
        
        check_matrix(data)
        
        # Matrix from list of lists ex
        if isinstance(data[0], list):
            self.matr = data.copy()
            self.rows_num = len(self.matr)
            self.cols_num = len(self.matr[0])
        
        # One-dimentional matrix from list
        else:
            self.matr = [data.copy()]
            self.rows_num = 1
            self.cols_num = len(data)


    # A function to return the shape of a matrix
    # returnes tuple of array dimentions
    def shape(self):
        return(self.rows_num, self.cols_num)
    

    # A function to print a matrix on the standard output
    def print(self):
        print(self)
    
    
    # A function to reshape a matrix into a vector in column-major order
    def reshape(self):
        vect = []
        for i in range(self.rows_num):
            for j in range(self.rows_num):
                vect.append(self.matr[j][i])
        # vect = [element for row in self.matr for element in row]
        return(Vector(vect))
    

    # A function to check if a matrix is square
    def is_square(self):
        return self.cols_num == self.rows_num
    

    # Overload print()
    def __str__(self):
        str_print = [str(row) for row in self.matr]
        return('\n'.join(str_print))


    # Operator+ overload
    def __add__(self, other):
        sum_matr = [[self.matr[i][j]+other.matr[i][j] for j in range(self.cols_num)] for i in range(self.rows_num)]
        return Matrix(sum_matr)
    
    
    # Operator- overload
    def __sub__(self, other):
        sub_matr = [[self.matr[i][j]-other.matr[i][j] for j in range(self.cols_num)] for i in range(self.rows_num)]
        return Matrix(sub_matr)
        
    
    # Operator* overload for scalar
    def __mul__(self, other):
        mul_matr = [[self.matr[i][j]*other for j in range(self.cols_num)] for i in range(self.rows_num)]
        return Matrix(mul_matr)

        
    # Reversed operator* overload
    def __rmul__(self, other):
        mul_matr = [[self.matr[i][j]*other for j in range(self.cols_num)] for i in range(self.rows_num)]
        return Matrix(mul_matr)