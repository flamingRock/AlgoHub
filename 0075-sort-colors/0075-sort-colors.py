class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {'red': 0, 'white': 0, 'blue': 0}
        actions = {
            0: lambda: counts.update({'red': counts['red'] + 1}),
            1: lambda: counts.update({'white': counts['white'] + 1}),
            2: lambda: counts.update({'blue': counts['blue'] + 1})
        }
        
        color_mapping = {'red': 0, 'white': 1, 'blue': 2}
        for num in nums:
            action = actions.get(num)
            if action:
                action()
        
        idx = 0
        for color in ['red', 'white', 'blue']:
            count = counts[color]
            for _ in range(count):
                nums[idx] = color_mapping[color]
                idx += 1