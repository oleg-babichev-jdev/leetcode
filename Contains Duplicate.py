class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''if len(set(nums)) == len(nums):
            return False
        else:
            return True'''
        seen = set([])
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False 
