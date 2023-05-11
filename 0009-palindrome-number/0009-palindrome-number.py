class Solution:
    # Solution 1
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False
        
    #     s = str(x)
    #     lenS = len(s)

    #     for i in range(lenS//2):
    #         print(f"lenS = {lenS}")
    #         if s[i] == s[lenS-1-i]:
    #             continue
    #         else:
    #             return False
    #     return True

    # Solution 2
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

    # Solution 3
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0 or x > 0 and x % 10 = 0:
    #         return False
         