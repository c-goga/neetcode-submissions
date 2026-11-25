class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #makes list for each number and check +- 1 of them and add to the list

        seq = []

        for num in nums: # each num
            new = True
            for s in seq: # each seq of numbers
                if num == s[0] - 1:
                    new = False
                    s.insert(0, num)
                elif num == s[len(s) - 1] + 1:
                    new = False
                    s.append(num)
                # elif num >= s[0] and num <= s[len(s) - 1]:
                #     new = False
            if new:
                seq.append([num])

        print(seq)

        i = 0 
        while i < len(seq):
            # print(i)
            lastIdx = len(seq[i]) - 1
            # [print(lastIdx)]
            j = 0
            while j < len(seq):
                if j == i:
                    j += 1
                    continue
                if seq[i][lastIdx] == seq[j][0]:
                    seq[i] = seq[i][:-1] + seq[j]
                    seq.remove(seq[j])
                    i -= 1
                    break
                j += 1
            i += 1
        
        print(seq)

        max = 0
        for s in seq:
            if (len(s) > max):
                max = len(s)
        return max
                