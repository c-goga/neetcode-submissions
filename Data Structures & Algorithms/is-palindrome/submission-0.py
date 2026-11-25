class Solution:
    def isPalindrome(self, s: str) -> bool:

        newS = ""

        for c in s:
            if (ord(c) >= 65 and ord(c) <= 90):
                newS += chr(ord(c) + 32)
            elif (ord(c) >= 97 and ord(c) <= 122):
                newS += c
            elif (ord(c) >= 48 and ord(c) <= 57):
                newS += c

        print(newS)

        i = 0
        j = len(newS) - 1
        
        firstHalfEnd = int(len(newS) / 2) - 1
        secondHalfStart = int(len(newS) / 2)
        if len(newS) % 2 == 1:
            secondHalfStart = int(len(newS) / 2) + 1

        while i <= firstHalfEnd and j >= secondHalfStart:
            if newS[i] != newS[j]:
                return False
            i += 1
            j -= 1

        return True