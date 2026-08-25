#this exercise will help me to avoid the list that have numbers be same .
class Solution:
  def hasDuplicate(self, num: list[int]) -> bool:
    count=0
    for i in range(len(num)):
      for j in range(i+1, len(num)):
        if num[i] == num[j]:
          count+=1
    if count:
      return True
    else: 
      return False