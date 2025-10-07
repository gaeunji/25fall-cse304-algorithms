from typing import List, Tuple

class Matrix:
    def __init__(self, mat):
        self.n = len(mat)
        self.matrix = mat
    
    def __add__(self, other):
        mat = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                mat[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(mat)

    def __sub__(self, other):
        mat = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                mat[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(mat)

    def __mul__(self, other):
        mat = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    mat[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(mat)
            
def partition(n: int, M: Matrix) -> Tuple[Matrix, Matrix, Matrix, Matrix]:
    m = n // 2
    m1 = [[0] * m for _ in range(m)]
    m2 = [[0] * m for _ in range(m)]
    m3 = [[0] * m for _ in range(m)]
    m4 = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            # Complete the code here
            # 4개의 부분 행렬 생성
            m1[i][j] = M.matrix[i][j]
            m2[i][j] = M.matrix[i][j+m]
            m3[i][j] = M.matrix[i+m][j]
            m4[i][j] = M.matrix[i+m][j+m]

    return Matrix(m1), Matrix(m2), Matrix(m3), Matrix(m4)
    
def combine(n: int, M1: Matrix, M2: Matrix, M3: Matrix, M4: Matrix) -> Matrix:
    m = n // 2
    mat = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            # Complete the code here
            # 4개의 부분 행렬 조합 -> 원래 행렬 생성
            mat[i][j] = M1.matrix[i][j]
            mat[i][j+m] = M2.matrix[i][j]
            mat[i+m][j] = M3.matrix[i][j]
            mat[i+m][j+m] = M4.matrix[i][j]

    return Matrix(mat)
   
def strassen(n: int, A: Matrix, B: Matrix) -> Matrix:
    global threshold

    if n <= threshold:
        return A * B
    else:
        A11, A12, A21, A22 = partition(n, A)
        B11, B12, B21, B22 = partition(n, B)
        
        # Complete the code here
        C11 = strassen(n//2, A11, B11) + strassen(n//2, A12, B21)
        C12 = strassen(n//2, A11, B12) + strassen(n//2, A12, B22)
        C21 = strassen(n//2, A21, B11) + strassen(n//2, A22, B21)
        C22 = strassen(n//2, A21, B12) + strassen(n//2, A22, B22)

        return combine(n, C11, C12, C21, C22)

threshold = 1