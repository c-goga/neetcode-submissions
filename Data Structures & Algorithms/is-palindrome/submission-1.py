class Solution:
    def isPalindrome(self, s: str) -> bool:

        # creates new string for checking 
        newS = ""
        for c in s:
            if (ord(c) >= 65 and ord(c) <= 90):
                newS += chr(ord(c) + 32)
            elif (ord(c) >= 97 and ord(c) <= 122):
                newS += c
            elif (ord(c) >= 48 and ord(c) <= 57):
                newS += c

        # two pointers, one at start and one at end
        i = 0
        j = len(newS) - 1
        # setting up where i and j will stop
        firstHalfEnd = int(len(newS) / 2) - 1
        secondHalfStart = int(len(newS) / 2)
        if len(newS) % 2 == 1: # odd is a special case for secondHalfStart
            secondHalfStart = int(len(newS) / 2) + 1

        while i <= firstHalfEnd and j >= secondHalfStart:
            if newS[i] != newS[j]:
                return False # no match, false
            i += 1
            j -= 1

        return True