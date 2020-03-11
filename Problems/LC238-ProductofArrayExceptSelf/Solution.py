class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        output = []

        # calculate the right side
        initial = 1
        for i in range(length): 
            output.append(initial)
            initial = initial * nums[i]

        # calculate the left side
        initial = 1
        for i in range(length-1, -1, -1): # start from right->left
            output[i] = output[i] * initial
            initial = initial * nums[i]
        return output
