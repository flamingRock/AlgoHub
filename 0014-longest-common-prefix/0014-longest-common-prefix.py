class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # solution using startswith func
        # pre = strs[0]
        # for word in strs:
        #     while not word.startswith(pre):
        #         pre = pre[:-1]
        # return pre

        # solution using prefix compare with first and last one
        count = 0
        mini, maxi = min(strs), max(strs)
        for i in range(len(mini)):
            if mini[i] != maxi[i]: break
            else: count += 1
        return mini[:count]
