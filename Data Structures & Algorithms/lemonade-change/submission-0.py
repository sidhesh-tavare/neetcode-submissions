class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f,te,tw = 0,0,0 
        for bill in bills:
            if bill==5:
                f+=1
            elif bill==10:
                te+=1
                f-=1
            else:
                tw+=1

                if(te>=1 and f>=1):
                    te-=1
                    f-=1
                
                elif(f>=3):
                    f-=3
                else: return False
            if(f<0 or te<0 or tw<0):
                return False
        return True

        