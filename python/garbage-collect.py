# There are three types of garbage truck for Metal (M), Paper (P) and Glass (G) 
# Their picking up and travel time is given by two lists. Find the minimal amount
# of time to collect all garbage
class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """

        total = 0
        mins = 0
        last = {'M': 0, 'P': 0, 'G': 0}
        distance = [0] * len(garbage)

        # find index of last house with a type of garbage
        for i in range(len(garbage)):
            for ch in last.keys():
                if ch in garbage[i]:
                    last[ch] = i

        # total pickup times
        for g in garbage:
            for ch in g:
                mins += 1

        # accumulative distance
        distance[0] = 0
        for i in range(1, len(garbage)):
            distance[i] = distance[i-1] + travel[i-1]
        total = 0
        for i in last.keys():
            total += distance[last[i]]
        return total + mins
