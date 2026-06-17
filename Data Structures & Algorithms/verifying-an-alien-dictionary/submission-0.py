class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapper = {}
        for idx,ch in enumerate(order):
            mapper[ch]=idx

        n = len(words)
        for i in range(1,n):
            fw,sw = words[i-1],words[i]
            minlen = min(len(fw),len(sw))
            if fw[:minlen] == sw[:minlen] and len(fw)>len(sw):
                return False
            for j in range(minlen):
                c1,c2=fw[j],sw[j]
                if c1==c2: continue
                if mapper[c1]<mapper[c2]:break
                if mapper[c1]>mapper[c2]:return False

        return True