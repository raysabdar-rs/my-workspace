# TowSum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        clist = {}
        for n in nums:
            if target - n in clist.keys():
                return (i, clist[target-n])
            clist[n] = i
            i += 1
        return None
