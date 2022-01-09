class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        preMap = {} # val : index
        for ind,val in enumerate(nums):
            diff = target - val
            if diff in preMap:
                return [preMap[diff] , ind]
            preMap[val] = ind
