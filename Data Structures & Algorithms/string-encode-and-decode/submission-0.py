class Solution:
    # thanks for helping of chatGPT I figured out how encode and decode
    # it helped me to figure out where does string start/end and how i know that
    def encode(self, strs: List[str]) -> str:
        #as first I will try to mark the start string in list using  "#" 
        #for ex : ["Hello", "World"] --> str: 5#Hello5#World 
        #it will convert the string like                   lenght|startofString|string|length|startOfString|stirng
        encoded_str = "" # initialize the variable store value encoded word
        for word in strs:
            count = str(len(word)) # convert int to str
            encoded_word = count + "#" + word
    
            encoded_str += encoded_word # save encoded word into str
        return encoded_str  
        
        

    def decode(self, s: str) -> List[str]:
        decoded_strs = [] # initialize the variable store value decoded
        i=0
        while i< len(s):
            j=s.find("#", i) # the position of  "#"
            len_str = int(s[i:j]) # it will get the integer from start to end "#"
            word_decoded = s[j+1: j +1 + len_str] # word decoded will start after "#" and end at "length of string that I encoded"
            decoded_strs.append(word_decoded) # then it will join into decoded string

            i += j-i + len_str +1
        return decoded_strs

            

        