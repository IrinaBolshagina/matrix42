from vector import Vector

class Matrix:

    rows = 0
    columns = 0

    # Usage: m = Matrix([[1, 2], [3, 4]]) or m = Matrix([v1, v2, v3])
    def __init__(self, matr: list):

        self.matr = matr

        #if isinstance(matr[0], Vector) 
        self.rows = len(self.matr)
        
        if isinstance(matr[0], list):
            self.columns = len(self.matr[0])

            # for row in matr:
            #     v = Vector(row) # use zip to reverse matrix

        else:
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
        assert isinstance(other, Matrix), "ValueError: can only add vector type"
        assert self.shape() == self.shape(), "ValueError: can only add matrix that have equal shape"
        sum_matr = [self.vect[i]+other.vect[i] for i in range(len(self.vect))]
        return Vector(sum_matr)
    
    
    # A function to reshape a matrix into a vector
    def reshape(self):
        vect = [element for row in self.matr for element in row]
        return(Vector(vect))