class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 기존의 O(n^2) time complexity말고 더 짧게
        # dictionary구조에서 dict[key]은 value이다
        # 여기서 seen dictionary의 key는 remaining을 요청한 값이고 value는 그 값의 index
        seen = {}
        for i, value in enumerate(nums):
          remaining = target - value
          if remaining in seen:
            return [i, seen[remaining]]
          else:
            seen[value] = i
     