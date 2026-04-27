class Solution(object):
    def isSubsequence(self, s, t):

        count = 0

        for x in range(len(t)):
            if count == len(s):
                break

            if t[x] == s[count]:
                count += 1 
        
        return len(s) == count