class Solution:
    def checkValidString(self, s: str) -> bool:
        left,star = [],[]
        for i,char in enumerate(s):
            if char =="(": left.append(i)
            elif char=="*":star.append(i)
            else:
                if left: left.pop()
                elif star: star.pop()
                else: return False
        
        while star and left:
            star_idx = star.pop()
            left_idx = left.pop()
            if star_idx<left_idx:
                return False

        return not left


        