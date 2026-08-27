class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] =  counts[nums[i]] + 1
            else:
                counts[nums[i]] = 1
        return sorted(counts, key=lambda x: counts[x], reverse=True)[:k]