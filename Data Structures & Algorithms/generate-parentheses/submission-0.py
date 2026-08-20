class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def path(openPar, closePar, combo):
            if openPar == closePar and openPar + closePar == n*2:
                res.append(combo)
                return

            if openPar < n:
                path(openPar+1, closePar, combo + "(")
            
            if closePar < openPar:
                path(openPar, closePar+1, combo + ")")

            return res

        path(0,0, "")
        return res