class Solution:
    def reverse(self, x: int) -> int:
        strX = str(x)
        revX = ""
        negative = False

        if strX[0] == '-':
            negative = True
            strX = strX.replace('-', '')
        # print(f"strX = {strX}")

        for i in range(len(strX), 0, -1):
            revX += strX[i-1]
        # print(f"revX = {revX}")

        if revX == '0':
            return 0
        while revX[0] == '0':
            revX = revX[1:]
        # print(f"after del 0 revX = {revX}")
        if int(revX) > pow(2, 31):
            return 0
        elif negative:
            return int(revX) * (-1)
        else:
            return int(revX)
        