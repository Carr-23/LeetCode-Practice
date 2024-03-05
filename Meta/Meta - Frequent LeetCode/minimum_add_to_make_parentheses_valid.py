class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        count = 0
        for p in s:
            if p == ")" and not stack:
                count += 1
            elif p == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(p)

        return count + len(stack)
