class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""    # 나머지? rest?
        for i in range(len(s)): # s의 길이만큼 i(;0~i)반복문
            # max function return the item with the higest value
            tmp = max(self.local_lP(s, i, i), self.local_lP(s, i, i+1), key = len)
            if len(tmp) > len(res):
                res = tmp
        return res
    
    # l:lest char, r:right char
    def local_lP(self, s, l: int, r: int) -> str:
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
    