class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_paren, close_paren, curr):
            if len(curr) == (n*2):
                res.append(''.join(curr))
            if open_paren < n:
                curr.append('(')
                backtrack(open_paren+1, close_paren, curr)
                curr.pop()
            if close_paren < open_paren:
                curr.append(')')
                backtrack(open_paren, close_paren+1, curr)
                curr.pop()
        
        backtrack(0,0,[])
        return res
                

        