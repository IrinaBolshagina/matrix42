from vector import Vector

class Matrix:

    rows = 0
    columns = 0

    # Usage: m = Matrix([[1, 2], [3, 4]]) or m = Matrix([v1, v2, v3])
    def __init__(self, matr: list):
       
        # if type(matr[0]) is list:
        # if isinstance(matr[0], Vector) = 
        
        if isinstance(matr[0], list):
            for row in matr:
                v = Vector(row) # use zip to reverse matrix

        # self.matr = matr
        # self.rows = len(self.matr)
        # try:
        #     self.columns = len(self.matr[0]) # one-dimentional matrix
        # except:
        #     columns = 0

    
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