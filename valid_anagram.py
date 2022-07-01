class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ord = []
        t_ord = []
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_ord.append(s[i])
            t_ord.append(t[i])
        s_ord.sort()
        t_ord.sort()
        if s_ord == t_ord:
            return True
        else:
            return False