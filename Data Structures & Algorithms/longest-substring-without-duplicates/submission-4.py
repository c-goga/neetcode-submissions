class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        res = 0
        string = []
        for c in s:
            print('s', string)
            if c in string:
                res = max(res, len(string))
                string = string[string.index(c)+1:len(string)]
                print('in', string)
            string.append(c)
        
        res = max(res, len(string))
        
        return res