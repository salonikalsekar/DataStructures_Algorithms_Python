class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:

        set1 = set()
        i = 0
        count = 0

        while i < len(A):

            if A[i] in set1:
                A[i] += 1
                count += 1

            else:
                set1.add(A[i])
                i += 1

        return (count)