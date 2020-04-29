class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        row=[[0,1,0]]
        for k in range(1,A+1):
            temp = []
            temp.append(0)
            for j in range(len(row[k-1])-1):
                temp.append(row[k-1][j]+row[k-1][j+1])
            temp.append(0)
            row.append(temp)
        return row[A][1:-1]