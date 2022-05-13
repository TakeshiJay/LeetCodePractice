# Answer for two-sum leetcode problem using train, maxi, and mini


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mini = 0 # set minimum train value for iterative search for value
        __maxi_train__ = len(nums)-1 # set the non moving train value to identify the max value
        maxi = len(nums)-1 # moving train value that will come to the closure of the array of values
        # iterative process that exits on the process of the minimum value equaling the maximum values
        while (mini != __maxi_train__):
            if (((nums[maxi] + nums[mini]) == target) and (mini != maxi)):
                arr = {mini, maxi}
                return arr
            elif (nums[maxi] + nums[mini] != target):
                maxi -= 1
            if (maxi == mini):
                mini += 1
                maxi = __maxi_train__
            
        
