class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d  = dict()

        for l in nums:      
            d[l] = d.get(l , 0)+1
        
        sorted_d = dict(
    sorted(d.items(), key=lambda x: x[1], reverse=True)
        )


        answer = []

        for key in sorted_d:
            if k==0:
                break
            answer.append(key)
            k-=1


        return answer

        