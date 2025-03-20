class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        table = [0]*26
        for index in range(len(s)):
            table[ord(s[index]) - ord('a')] += 1
            table[ord(t[index]) - ord('a')] -= 1

        for num in table:
            if num != 0:
                return False
        
        return True

s = Solution()
assert s.isAnagram("anagram", "nagaram") == True
assert s.isAnagram("racecar", "carrace") == True
assert s.isAnagram("rat", "car") == False
