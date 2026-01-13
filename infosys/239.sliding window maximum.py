from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0:
            return []

        dq = deque()   # stores indices
        result = []

        for i in range(len(nums)):

            # Remove indices out of current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove smaller elements (maintain decreasing order)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Start adding results once window size is k
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
