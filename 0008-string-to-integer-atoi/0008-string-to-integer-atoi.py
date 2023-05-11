class Solution:
    def myAtoi(self, s: str) -> int:
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        n, empty, sign = '', True, 1
        for char in s:
            if empty:
                if char == ' ': continue
                elif char == '-': sign = -1
                elif char.isdigit(): n += char
                elif char != '+': return 0
                empty = False
            else:
                if char.isdigit(): n += char
                else: break
        if n: atoiNum = sign * int(n)
        else: return 0

        if atoiNum > MAX: return MAX
        elif atoiNum < MIN: return MIN
        else:
            return atoiNum
        
        # 불분명한 문제의 핵심 알고리즘은 다 구현한 내 방식의 코드
        # tempInt = ""
        # start = False
        # for ch in s:
        #     try:
        #         int(ch)
        #         start = True
        #         tempInt += ch
        #     except:
        #         if not start:
        #             if ch == ' ': continue
        #             elif ch == '+':
        #                 start = True
        #                 continue
        #             elif ch == '-': 
        #                 start = True
        #                 tempInt += ch
        #         else:
        #             if ch == ' ' or ch == '+' or ch == '-':
        #                 break
        #             elif tempInt == '': return 0
                    
        # try:
        #     int(tempInt)
        #     print(f"tempInt in try = {tempInt}")
        # except:
        #     print(f"tempInt in exception = {tempInt}")
        #     return 0

        # if int(tempInt) > pow(2, 31) - 1:
        #     return pow(2,31) - 1
        # elif int(tempInt) < pow(-2, 31):
        #     return pow(-2, 31)
        # else:
        #     return int(tempInt)
            