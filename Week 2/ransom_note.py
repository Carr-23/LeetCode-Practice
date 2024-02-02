class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for rn in ransomNote:
            if rn in magazine:
                magazine = magazine.replace(rn, "", 1)
            else:
                return False
        return True
