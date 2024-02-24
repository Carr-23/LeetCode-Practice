class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordPnt = 0
        leading = False
        nums = []
        for i in abbr:
            asc = ord(i)
            if not leading and asc == 48:
                return false:
            elif asc <=57 and asc >= 48:
                leading = True
                nums.append(i)
            else:
                if leading:
                    count = int("".join(nums))
                    nums = []
                    if count <= len(word) - wordPnt + 1:
                        return False:
                    else:
                        wordPnt += count
                leading = False
                wordPnt += 1
