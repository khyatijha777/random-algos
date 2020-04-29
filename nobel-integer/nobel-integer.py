class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        A.sort()
        # print(A)
        for i in range(len(A)):
            j = i
            while  j<len(A) and A[i] ==A[j]:
                j+=1
            if A[i] == len(A)-j:
                return 1
        return -1
