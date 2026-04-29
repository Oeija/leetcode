class Solution(object):
    def longestCommonPrefix(self, strs):

        char = ""
        result = ""
        flag = True
        index = 0
        shortest_len = len(min(strs, key=len))

        if not strs: 
            return ""
        elif len(strs) == 1:
            result += strs[0]
            return result
        else:
            
            for i in range(shortest_len):

                char = strs[0][index]

                for x in range(len(strs)):
                    if strs[x][index] != char:
                        flag = False
                        break
                
                if flag == True:
                    result += char
                    index += 1
                else:
                    return result
            
            return result