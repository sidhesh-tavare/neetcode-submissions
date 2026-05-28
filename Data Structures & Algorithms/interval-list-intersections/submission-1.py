class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not secondList or not firstList:
            return []
        secondList.sort()
        firstList.sort()
        fn,sn = len(firstList),len(secondList)
        f,s = 0,0
        res = []

        while f<fn and s<sn:
            fs,fe=firstList[f]
            ss,se = secondList[s]
            start = max(fs, ss)
            end = min(fe, se)

            if start <= end:
                res.append([start, end])
            if fe<se:
                f+=1
            else:
                s+=1
        
        return res