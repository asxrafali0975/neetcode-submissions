class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size  = len(nums)

        hashmap = dict({})

        for i in range(size):
            hashmap[nums[i]] = i

        for i in range(size):
            number = nums[i]
            leftover = target - number
            if hashmap.get(leftover):
                if i!=hashmap[leftover]:
                    return [i , hashmap[leftover]]
        


        