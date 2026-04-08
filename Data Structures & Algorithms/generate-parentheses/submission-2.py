class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #if you pick an open...
            #you can pick a another open (up to possible opens left)
            #or pick a close
            #open count goes down if we pick an open
            #close count stays if we pick a close
            # we can keep hitting them as long as we have opens
            res = []
            def backtrack(curr, opens_available, closes_available):
                if curr and len(curr) == n*2:
                    res.append(''.join(curr))
                    return 
                #pick an open
                if opens_available > 0:
                    curr.append('(')
                    backtrack(curr, opens_available-1, closes_available+1)
                    curr.pop()
                #pick a close
                if closes_available > 0:
                    curr.append(')')
                    backtrack(curr, opens_available, closes_available-1)
                    curr.pop()
            backtrack([], n, 0)
            return res

           