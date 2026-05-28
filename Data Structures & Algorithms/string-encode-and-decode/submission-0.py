class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            str_to_add = str(len(word)) + '#' + word
            res += str_to_add
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0 
        res = []
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i+=1
            
            length = int(length)
            i+=1

            word = s[i:i+length]
            res.append(word)
            i+=length
        print(res)
        return res

        
