class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr = 0
        for i in range(k):
            curr += nums[i]
        max_avg = float(curr)/k

        for i in range(k,len(nums)):
            curr -= nums[i-k]
            curr += nums[i]
            avg = float(curr)/k
            max_avg = max(max_avg,avg)
        return max_avg          
        