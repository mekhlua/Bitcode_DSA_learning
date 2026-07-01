class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        holder=0

        for i in nums:
            if i == 1:
                count +=1
                holder=max(holder,count)
            else:
                count=0
        return holder 

        