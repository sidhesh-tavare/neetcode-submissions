class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def recursion(curr_index,curr_sub):
            if curr_index == n:
                ans.append(curr_sub[::])
                return 
            
            for i in range(curr_index,n):
                c = s[curr_index:i+1]
                if c == c[::-1]:
                    curr_sub.append(c)
                    recursion(i+1,curr_sub)
                    curr_sub.pop()
        recursion(0,[])
        return ans