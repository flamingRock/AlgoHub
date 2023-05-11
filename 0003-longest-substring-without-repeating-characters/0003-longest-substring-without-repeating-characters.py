class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_length = 0
        used_chars = {}
        
        # for i in range(len(s)):
        #     if s[i] in used_chars and start <= used_chars[s[i]]:
        #         start = used_chars[s[i]] + 1
        #     else :
        #         max_length = max(max_length, i - start + 1)
        #     used_chars[s[i]] = i
        # to simplify the code by enumerate method
        # for i, c in enumerate(s):
        #     if c in used_chars and start <= used_chars[c]:
        #         start = used_chars[c] + 1
        #     else :
        #         max_length = max(max_length, i - start + 1)
        #     used_chars[c] = i
        
        for i, c in enumerate(s):
            if c in used_chars and start <= used_chars[c]:
                start = used_chars[c] + 1
            else :
                max_length = max(max_length, i - start + 1)
            used_chars[c] = i
        
        
        return max_length
            



# 이건 중복안되는 substring의 최대 길이를 구하는 solution
# 문제는 중복되는 char이 하나도 없는 substring의 최대 길이
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if s:
#             first = s[0]
#             last = s[0]
#             local_max = 1
#             glob_max = 1
#         else:
#             return 0
        
#         for i in range(1, len(s)):
#             # subs와 i번째 문자와 겹치면
#             if first == s[i] or last == s[i]:
#                 first = s[i]
#                 last = s[i]
#                 local_max = 1
#                 print("Cross this char = {}, and max = {}".format(s[i], glob_max))
#             # 겹치지 않으면
#             else:
#                 last = s[i]
#                 local_max += 1
#                 if local_max > glob_max:
#                     glob_max = local_max
#                 print("local_max + 1 at s[{}]= {}, local = {} max = {}"
#                       .format(i, s[i], local_max, glob_max))
            
#         if local_max > glob_max:
#             glob_max = local_max
            
#         return glob_max
                