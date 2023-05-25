class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascalTri = [[1]]
        for i in range(2, numRows + 1):
            row = []
            for j in range(1, i + 1):
                # print(f"i = {i} j = {j}")
                if j == 1 or j == i:
                    row.append(1)
                else:
                    row.append(pascalTri[i-2][j-2] + pascalTri[i-2][j-1])
            pascalTri.append(row)
        return pascalTri

        