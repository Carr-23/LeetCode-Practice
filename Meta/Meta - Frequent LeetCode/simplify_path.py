class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirN = ""
        path += "/"

        for s in path:
            if s == "/" and dirN:
                if dirN != "." and dirN != "..":
                    stack.append(dirN)
                    dirN = ""
                elif dirN == ".":
                    dirN = ""
                    continue
                elif dirN == "..":
                    if stack:
                        stack.pop()
                    dirN = ""

            if s == "/":
                continue

            dirN += s

        return "/" + "/".join(stack)
