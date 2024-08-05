from vector import Vector

# check if input is a list
# check if dimensions are the same for all rows
# make input for one-dimentional matrix as a simple list

def check_matrix(matr: list):
    assert isinstance(matr, list), "ValueError: input must be a list"
    assert all(len(row) == len(matr[0]) for row in matr), "ValueError: all rows must have the same length"


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
    

    # Multiplication matrix by vector
    def mul_vec(self, other: Vector):
        res = [0 for i in range(self.cols_num)]
        for i in range(self.cols_num):
            for j in range(self.rows_num):
                res[i] += self.matr[i][j] * other.vect[i]
        return Vector(res)
    

    # Multiplication of two matrices
    def mul_mat(self, other: 'Matrix'):
        res = [[0 for i in range(other.cols_num)] for j in range(self.rows_num)]
        for i in range(self.rows_num):
            for j in range(other.cols_num):
                for k in range(self.cols_num):
                    res[i][j] += self.matr[i][k] * other.matr[k][j]
        return Matrix(res)


    # Trace of a matrix
    def trace(self):
        if not self.is_square():
            raise ValueError("Matrix is not square")
        return sum(self.matr[i][i] for i in range(self.rows_num))
    

    # Transpose of a matrix
    def transpose(self):
        res = [[0 for i in range(self.rows_num)] for j in range(self.cols_num)]
        for i in range(self.rows_num):
            for j in range(self.cols_num):
                if isinstance(self.matr[i][j], complex):
                    res[j][i] = self.matr[i][j].conjugate()
                else:
                    res[j][i] = self.matr[i][j]
        return Matrix(res)
    

    # Reduced row echelon form of a matrix
    def row_echelon(self):
        res = self.matr.copy()
        for i in range(self.rows_num):
            if res[i][i] == 0:
                for j in range(i+1, self.rows_num):
                    if res[j][i] != 0:
                        res[i], res[j] = res[j], res[i]
                        break
            if res[i][i] != 0:
                res[i] = [elem/res[i][i] for elem in res[i]]
                for j in range(self.rows_num):
                    if j != i:
                        res[j] = [res[j][k] - res[j][i]*res[i][k] for k in range(self.cols_num)]
        return Matrix(res)
    

    # Reduced row echelon form of a matrix
    def row_echelon(self):
        res = self.matr.copy()        
        lead = 0
        for r in range(self.rows_num):
            if lead >= self.cols_num:
                return res
            i = r
            while res[i][lead] == 0:
                i += 1
                if i == self.rows_num:
                    i = r
                    lead += 1
                    if lead == self.cols_num:
                        return res
            res[i], res[r] = res[r], res[i]
            lv = res[r][lead]
            res[r] = [mrx / lv for mrx in res[r]]
            for i in range(self.rows_num):
                if i != r:
                    lv = res[i][lead]
                    res[i] = [iv - lv*rv for rv, iv in zip(res[r], res[i])]
            lead += 1
        # res = [[x*(-1) for x in row if x == -0.0] for row in res]
        return Matrix(res)


    # Determinant of a matrix
    def det(self):
        if not self.is_square():
            raise ValueError("Matrix is not square")
        if self.rows_num == 1:
            return self.matr[0][0]
        if self.rows_num == 2:
            return self.matr[0][0]*self.matr[1][1] - self.matr[0][1]*self.matr[1][0]
        else:
            det = 0
            for i in range(self.rows_num):
                det += ((-1)**i) * self.matr[0][i] * self.minor(0, i).det()
        return det
        

       