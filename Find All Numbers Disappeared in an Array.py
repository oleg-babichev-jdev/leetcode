class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''l = []
        for i in range(1,len(nums)+1):
            l.append(i)
        return set(l)-set(nums)'''
        i = 0
        while i < len(nums):
          pos = nums[i] - 1 # correct position
          if nums[i] != nums[pos]:
            nums[i], nums[pos] = nums[pos], nums[i]
          else:
            i += 1

        miss = []
        for i in range(len(nums)):
          if nums[i] != i + 1:
            miss.append(i + 1)

        return miss
