class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapper = {c:i for i,c in enumerate(order)}
        n = len(words)

        for i in range(1,n):
            fw,sw = words[i-1],words[i]
            minlen = min(len(fw),len(sw))

            for j in range(minlen):
                c1,c2 = fw[j],sw[j]
                if mapper[c1]<mapper[c2]: break 
                elif mapper[c1]>mapper[c2]: return False
            else:
                if len(fw)>len(sw): return False
        return True
                

        