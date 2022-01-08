class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''uni = 0
        for i in nums:
            if nums.count(i)==1:
                uni = i
        return uni'''
        mask = 0
        for num in nums:
          mask ^= num
        return mask
