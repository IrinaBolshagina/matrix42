from vector import Vector

class Matrix:

    rows_num = 0
    cols_num = 0

    # Usage: m = Matrix([[1, 2], [3, 4]]) 
    def __init__(self, matr: list):

        self.matr = matr.copy()
        self.rows_num = len(self.matr)
        self.cols_num = len(self.matr[0])
        self.elem_type = type(matr[0][0])


    # A function to return the shape of a matrix
    # returnes tuple of array dimentions
    def shape(self):
        return(self.rows_num, self.cols_num)
    

    # A function to print a matrix on the standard output
    def print(self):
        print(self)
    
    
    # Overload print()
    def __str__(self):
        str_print = [str(row) for row in self.matr]
        return('\n'.join(str_print))


    # operator+ overload
    def __add__(self, other):
        assert isinstance(other, Matrix), "ValueError: can only add matrix type"
        assert self.shape() == self.shape(), "ValueError: can only add matrix that have equal shape"
        sum_matr = [self.row[i]+other.row[i] for i in range(len(self.vect))]
        return Matrix(sum_matr)
    
    
    # A function to reshape a matrix into a vector in column-major order
    def reshape(self):
        vect = []
        for i in range(self.rows_num):
            for j in range(self.rows_num):
                vect.append(self.matr[j][i])
        # vect = [element for row in self.matr for element in row]
        return(Vector(vect))
    
    def is_square(self):
        return self.cols_num == self.rows_num