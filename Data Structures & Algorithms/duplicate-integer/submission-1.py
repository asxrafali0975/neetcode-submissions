class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap  = dict({})
        
        for num in nums:
            if not hashmap.get(num):
                hashmap[num] = 1
            else:
                hashmap[num]+=1
        
        for key in hashmap:
            if hashmap[key]>1:
                return True

        return False


        