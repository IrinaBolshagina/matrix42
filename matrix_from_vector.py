from vector import Vector

class Matrix:

    rows = 0
    columns = 0

    # Usage: m = Matrix([[1, 2], [3, 4]]) or m = Matrix([v1, v2, v3])
    def __init__(self, matr: list):

        self.rows = len(matr)

        if isinstance(matr[0], Vector):
            self.matr = [row.vect for row in matr]
            self.vectors = Vector([row for row in matr])
            self.columns = matr[0].size()
        
        elif isinstance(matr[0], list):
            self.matr = matr
            self.vectors = Vector([Vector(row) for row in matr])
            self.columns = len(matr[0])
            # for row in matr:
            #     v = Vector(row) # use zip to reverse matrix

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
    

    # A function to print a matrix on the standard output
    def print(self):
        print(self)
    
    
    # Overload print()
    def __str__(self):
        if self.columns > 1:
            str_print = [str(row) for row in self.matr]
        else:
            str_print = ['['+ str(value) + ']' for value in self.matr]
        return('\n'.join(str_print))


    # operator+ overload
    def __add__(self, other):
        assert isinstance(other, Matrix), "ValueError: can only add matrix type"
        assert self.shape() == self.shape(), "ValueError: can only add matrice that have equal shape"
        sum_matr = []
        for i in range(self.rows):
            sum_matr.append((self.vectors[i] + other.vectors[i]))
        return(Matrix(sum_matr))
    
    
    # A function to reshape a matrix into a vector
    def reshape(self):
        if self.columns > 1:
            vect = [element for row in self.matr for element in row]
            return(Vector(vect))
        else:
            return(self.matr)