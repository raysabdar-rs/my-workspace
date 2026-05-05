# Given an integer array height of length n. There are n vertical lines drawn 
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that 
# the container contains the most water.
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mx = 0
        rv = 0
        i, j = 0, len(height)-1

        while (i < j):
            if height[i] < height[j]:
                mx = height[i] * (j-i)
                i += 1
            else:
                mx = height[j] * (j-i)
                j -= 1
            rv = max(rv, mx)
        return rv

        
            
        
