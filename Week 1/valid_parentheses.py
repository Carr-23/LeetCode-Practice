class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for string in s:
            if string in "({[":
                stack.append(string)
            else:
                if not stack:
                    return False
                if (
                    string == "}"
                    and stack[-1] == "{"
                    or string == "]"
                    and stack[-1] == "["
                    or string == ")"
                    and stack[-1] == "("
                ):
                    stack.pop()
                else:
                    return False
        return True if not stack else False
