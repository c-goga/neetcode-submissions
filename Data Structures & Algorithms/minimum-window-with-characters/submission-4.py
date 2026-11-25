class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count1, count2 = {}, {}

        for c in t:
            count2[c] = 1 + count2.get(c, 0)
        need = len(t)
        curr = 0
        total = 0
        l = -1
        res = ""
        for r in range(len(s)):
            print(s[r])
            total += 1
            print('start total', total)
            if s[r] in t:
                if l == -1:
                    l = r

                count1[s[r]] = 1 + count1.get(s[r], 0)
                if count1[s[r]] <= count2[s[r]]:
                    curr += 1
                if curr >= need and res == "":
                    res = s[l:r+1]
                    print('res1', res)
                print('aftrt', curr)
                # if res != "" and s[r] != s[l]:
                #     continue
                if res != "" and len(res) > 1:
                    print('ere')
                    # count1[s[l]] -= 1
                    # total -= 1
                    # l += 1
                    while total > need:
                        print(count1)
                        print('l', l)
                        print('curr', curr)
                        print('total', total)
                        if s[l] in t:
                            if count1[s[l]] > count2[s[l]]:
                                count1[s[l]] -= 1
                                print('c1', count1)
                            else:
                                break;
                        l += 1
                        total -=1
                    # while s[l] not in t:
                    #     l += 1
                    print('due', count1)
                    print('dude', l)
                    if len(res) > len(s[l:r+1]):
                        res = s[l:r+1]

                if len(res) > len(s[l:r+1]):
                    res = s[l:r+1]
                    print('res', res)
        
        return res

