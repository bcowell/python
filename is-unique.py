# isUnique
# Determine if a string has all unique characters
# O(n) - where n is the number of characters in the string
class Solution:
    def isUnique(self, S: str) -> bool:
        hashMap = {}
        for char in S:
            if (char in hashMap):
                return False
            hashMap[char] = char
        return True

solution = Solution()
print(solution.isUnique("abc")) # True
print(solution.isUnique("abca")) # False
print(solution.isUnique("hgjfls;dp;")) # False
print(solution.isUnique("abcdefghijklmnopqrstuvwxyz")) #True