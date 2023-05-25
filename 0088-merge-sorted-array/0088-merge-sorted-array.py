class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i_nums1, i_nums2, i_sorted = m-1, n-1, m+n-1
        while i_nums2 >= 0:
            if nums1[i_nums1] >= nums2[i_nums2] and i_nums1 >= 0:
                nums1[i_sorted] = nums1[i_nums1]
                i_nums1 -= 1
            else:
                nums1[i_sorted] = nums2[i_nums2]
                i_nums2 -= 1
            i_sorted -= 1