class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A)<2:
            return 0
        max_sum = 0
        A = list(A)
        A.sort()
        for i in range(len(A)-1):
            if A[i+1]-A[i] >max_sum:
                max_sum = A[i+1]-A[i]
        return max_sum
        