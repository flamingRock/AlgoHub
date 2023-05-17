class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 내가 짠 mapping 방식은 너무 느림, 12.67%만을 이김
        # counts = {'red': 0, 'white': 0, 'blue': 0}
        # actions = {
        #     0: lambda: counts.update({'red': counts['red'] + 1}),
        #     1: lambda: counts.update({'white': counts['white'] + 1}),
        #     2: lambda: counts.update({'blue': counts['blue'] + 1}),
        # }
        
        # # mapping할 때는 dict형식의 자료형을
        # color_mapping = {'red': 0, 'white': 1, 'blue': 2}
        # for num in nums:
        #     action = actions.get(num)
        #     if action:
        #         action()
        
        # # dict형식의 key와 value값을 loop에 각각 사용할 땐 .items()를
        # idx = 0
        # for color in ['red', 'white', 'blue']:
        #     count = counts[color]
        #     for _ in range(count):
        #         nums[idx] = color_mapping[color]
        #         idx += 1
        
        
        # 위의 방식을 속도 개선을 위해, dict 조회가 아닌 list를 활용한 룩업테이블로 작성
        # 이 방식은 그래서 41% 이김
        # 딕셔너리 조회, 딕셔너리 업데이트는 인덱스를 직접 활용한 list의 동일 동작보다 훨씬 느림
        # 하지만 key-value에 따른 장점도 있으니 list를 활용할 수 없는 환경에서 쓰고, 여기선 X
        # color_counts = [0, 0, 0]
        # color_mapping = {0: 0, 1: 1, 2: 2}
        
        # for num in nums:
        #     color_counts[num] += 1
        
        # idx = 0
        # for color, count in enumerate(color_counts):
        #     for _ in range(count):
        #         nums[idx] = color_mapping[color]
        #         idx += 1
        
        
        # 가장 빠른 방식은 for루프를 각각의 0, 1, 2각각에 맞게 돌리면서 교체해주는 것
        # 이 방식을 뭐라 했더라, 3 way partitioning quick sort
        i = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                i += 1
        
        for idx in range(len(nums)):
            if nums[idx] == 1:
                nums[idx], nums[i] = nums[i], nums[idx]
                i += 1
        
        for idx in range(len(nums)):
            if nums[idx] == 2:
                nums[idx], nums[i] = nums[i], nums[idx]
                i += 1
        