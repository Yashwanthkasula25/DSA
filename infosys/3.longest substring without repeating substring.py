class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        r = 0
        result = set()
        for i in range(len(s)):
            while s[i] in result:
                result.remove(s[l])
                l += 1
            w = (i - l) + 1
            r = max(r,w)
            result.add(s[i])
        return r    
