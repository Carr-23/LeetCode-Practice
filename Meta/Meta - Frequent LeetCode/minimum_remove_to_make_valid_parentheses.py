class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        par = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == "(":
                par.append(i)
            elif s[i] == ")":
                if par:
                    par.pop()
                else:
                    s[i] = ""

        for i in par:
            s[i] = ""

        return "".join(s)
