class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''sumy = 0
        for i in range(0,len(nums)+1):
            sumy+=i
        return sumy - sum(nums)'''
        n = len(nums)
        return n * (n+1) //2 - sum(nums)
