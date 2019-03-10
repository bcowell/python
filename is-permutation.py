# isPermutation
# Given two strings, determine if one is a permutation of the other

# Solution 1
# Sort both strings, if they're permutations the sorted strings will be equal
# O(a log(a) + b log(b)) - where a, b are the lenghths of the two strings
class Solution:
    def isPermutation(self, A: str, B: str) -> bool:
        return sorted(A) == sorted(B)

solution = Solution()
print(solution.isPermutation("abc", "bca")) # True
print(solution.isPermutation("abcde", "ecbadd")) # False
print(solution.isPermutation("abc", "a")) # False

# Solution 2
# Compare the number of distinct characters
# O(a + b) - where a,b are the lengths of A and B
class Solution2:
    def isPermutation(self, A: str, B: str) -> bool:
        # Permutations must be the same length
        if len(A) != len(B):
            return False

        # count number of each letter in A
        letters = {}
        for a in A:
            if a in letters:
                letters[a] = letters[a] + 1
            else:
                letters[a] = 1
        # Verify counts are the same
        for b in B:
            if b not in letters:
                return False
            letters[b] = letters[b] - 1
            if letters[b] < 0:
                return False

        return True

solution = Solution2()
print(solution.isPermutation("abba", "bbaa")) # True
print(solution.isPermutation("ddabcf", "ecbadd")) # False
print(solution.isPermutation("abcd", "dacc")) # False