class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=[]
        s = s1
        for c in s2:
            print(s)
            print('char', c)
            if c in s:
                print('1')
                s = s.replace(c, "", 1)
                window.append(c)
                print('re', s)
            elif c in s1:
                print('2')
                idx = window.index(c)
                print('before', window, idx)
                window = window[idx + 1:]
                print('after', window)
                window.append(c)
                s = s1
                for w in window:
                    s = s.replace(w, "", 1)
                print('234', s)
            else :
                s = s1
            
            if len(s) == 0:
                return True
        
        return False
