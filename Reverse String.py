class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            # Python's inbuilt feature to swap 2 variable vals is
            # a, b = b, a
            # In python arr[-i] gives the last ith element in array starting from
            # arr[-1]
            # Since i in for loop begins with 0, we are taking s[-i-1] which is
            # in simple form s[-(i + 1)]
            s[i], s[-i - 1] = s[-i - 1], s[i]
