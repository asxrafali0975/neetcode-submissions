class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zeros : int = 0
        product : int = 1
        size : int = len(nums)

        for num in nums:
            if num!=0:
                product *= num
            elif num==0:
                count_zeros+=1

        if count_zeros ==0:
            answer = []
            for n in nums:
                value = product // n
                answer.append(value)
            return answer

        if count_zeros ==1:
            answer = []
            for n in nums:
                if n==0:
                    answer.append(product)
                else:
                    answer.append(0)
            return answer
        

        if count_zeros >1:
            return [0 for _ in range(size)]
        
        


        