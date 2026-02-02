# 242 .Valid_Anagram

class Solution(object):
    def isAnagram(self, s, t):
    
        if len(s) != len(t):
            return False
        
        count_s = {}
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1
    
        count_t = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1
    
        return count_s == count_t
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("listen","silent")) 