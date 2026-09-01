class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result =[]
        left_product= 1
        right_product = 1
        left = []
        right = [0] *len(nums)
        for i in range(len(nums)):
            left.append(left_product)
            left_product *=nums[i]
            right[len(nums) -1-i] = right_product
            
            right_product *= nums[len(nums) -1 -i]
        for i in range(len(nums)):
            result.append(right[i] *left [i])
        return result

        