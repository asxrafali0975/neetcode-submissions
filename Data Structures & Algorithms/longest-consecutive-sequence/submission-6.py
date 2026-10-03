class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        size = len(nums)
        if size==0:
            return 0
        sett = set(nums)
        maxcount = 1

        for num in nums:
            current_num = num
            count = 1
            if current_num-1 not in sett:

                while current_num+1 in sett:
                    count+=1
                    current_num+=1
                maxcount = max(maxcount , count)
        return maxcount
