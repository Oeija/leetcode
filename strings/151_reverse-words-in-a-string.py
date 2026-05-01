class Solution(object):
    def reverseWords(self, s):

        words = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == " ":
                i -= 1
                continue

            j = i
            while i >= 0 and s[i] != " ":
                i -= 1

            words.append(s[i+1:j+1])

        return " ".join(words)
        
        """
        :type s: str
        :rtype: str
        """
        