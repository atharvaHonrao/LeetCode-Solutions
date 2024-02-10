class Solution(object):
    def setZeroes(self, matrix):
        n = int(len(matrix))
        m = int(len(matrix[0]))
        x = []
        y = []
        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j]==0:
                    if i not in x:
                        x.append(i)
                    if j not in y:
                        y.append(j)
        for i in x:
            for j in range(0,m):
                matrix[i][j]=0
        for j in y:
            for i in range(0,n):
                matrix[i][j]=0
            
