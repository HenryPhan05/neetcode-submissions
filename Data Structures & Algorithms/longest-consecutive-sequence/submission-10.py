class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        seen = set()
        if nums == []:
            return 0
        for num in nums :
            if num in seen: 
                continue
            seen.add(num)

        for num in seen:
            if num-1 not in seen:
                length = 1
                while num+1 in seen:
                    num = num+1
                    length+=1
                count = max(count,length)
                 

        return  count 
        