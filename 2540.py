class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = list(set(nums1).intersection(set(nums2)))
        return min(intersection) if intersection else -1
        