# https://leetcode.com/problems/roman-to-integer/
# input Roman numerals, output integer of that num

class Solution:
    def romanToInt(self, s: str) -> int:
      sum = 0
      for i, ch in enumerate(s):
        if ch == 'I':
          if s[i+1:i+2] == 'V' or s[i+1:i+2] == 'X':
            sum += -1
          else:
            sum += 1
        elif ch == 'V':
          sum += 5
        elif ch == 'X':
          if s[i+1:i+2] == 'L' or s[i+1:i+2] == 'C':
            sum += -10
          else:
            sum += 10
        elif ch == 'L':
          sum += 50
        elif ch == 'C':
          if s[i+1:i+2] == 'D' or s[i+1:i+2] == 'M':
            sum += -100
          else:
            sum += 100
        elif ch == 'D':
          sum += 500
        elif ch == 'M':
          sum += 1000
          
      return sum