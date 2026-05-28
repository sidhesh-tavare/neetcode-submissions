class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def recursion(index,curr):
            if index == n:
                ans.append(curr[::])
                return 
            
            for i in range(index,n):
                c = s[index:i+1]
                if c == c[::-1]:
                    curr.append(c)
                    recursion(i+1,curr)
                    curr.pop()
        recursion(0,[])
        return ans