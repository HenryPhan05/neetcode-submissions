#this exercise will help me to avoid the list that have numbers be same .
class Solution:
   def hasDuplicate(self, nums: list[int])-> bool:
    numbers=set()
    for number in nums:
      if number in numbers:
        return True
      numbers.add(number)
    return False