class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        low = 0
        high = k-1
        answer_list = []

        largest_number = self.largest_num(nums , low,high)
        answer_list.append(largest_number)

        while high+1<size:
            high+=1

            """
            case 1 : when nums[high] (upcoming) is the larger than current largest

            sol : to is case me 
            """

            if nums[high] > largest_number:
                largest_number = nums[high]

            """
            case 2: if nums[low] if the highest num and we are leaving that window
            """

            if nums[low]==largest_number:
                #so leave it and search for number bw low+1 , high
                largest_number = self.largest_num(nums,low+1 , high)
                
                
            answer_list.append(largest_number)

            low+=1




        return answer_list

        

      
    def largest_num(self,nums,low,high):
        largest_number  = nums[low]
        for i in range(low , high+1):
            if nums[i]>largest_number:
                largest_number = nums[i]

        return largest_number
