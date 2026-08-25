#hashmap
class Solution: 
  def isAnagram(self, s:str, t:str)-> bool: # return boolean
    if len(s) !=len(t): #compare length s and t if it's different return false
      return False
    
    countS={} # empty list character
    countT={} 
    for c in range(len(s)): # browse each character in len(s) 
      countS[s[c]]= 1+ countS.get(s[c],0) # get (key,value)
      countT[t[c]]=1+ countT.get(t[c],0)
    return countS == countT