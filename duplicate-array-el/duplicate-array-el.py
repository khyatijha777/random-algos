class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A= list(A)
        A.sort()
        for i in range(len(A)-1):
            if A[i]==A[i+1]:
                return A[i]
        return -1