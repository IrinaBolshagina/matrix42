
class Vector:
    
     # Usage: v = Vector([1,2])
    def __init__(self, vect: list):
        self.vect = vect
    
    # A function to return the size of a vector
    def size(self):
        return len(self.vect)
    
    # A function to print a vector on the standard output
    def print(self):
        print(self.vect)
    
    # A function to reshape a vector into a matrix
    def reshape(self):
        return(Matrix(self))



class Matrix:

    # Usage: m = Matrix([[1, 2], [3, 4]])
    def __init__(self, matr: list):
       
        # if type(matr[0]) is list:
        self.matr = matr
        # one-dimentional matrix
        # else:
        #     self.matr = []
        #     self.matr.append(matr)

    
    # A function to return the shape of a matrix
    # returnes tuple of array dimentions
    def shape(self):
        return(len(self.matr), len(self.matr[0]))
    
    # A function to print a matrix on the standard output
    def print(self):
        print('[', end='')
        print(self.matr[0])
        i = 1
        while i < len(self.matr)-1:
            print('', self.matr[i])
            i = i+1
        print('', self.matr[i], end='')
        print(']')
    
    # A function to reshape a matrix into a vector
    def reshape(self):
        vect = [element for row in self.matr for element in row]
        # return(vect)
        return(Vector(vect))