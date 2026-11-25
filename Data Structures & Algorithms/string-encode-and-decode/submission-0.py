class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedS = ""
        for s in strs:
            encodedS = encodedS + str(len(s)) + "#" + s
        return encodedS
    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i < len(s): # first index
            j = i # second index
            while s[j] != '#':
                j += 1 # iterate through until '#' is reached right before the string
            length = int(s[i:j]) # extract number
            i = j + 1 # set new first index to start of the word
            j = i + length # set end of second index to the end of the word
            l.append(s[i:j]) # extract the word
            i = j # set first index to the end of the word and continue extracting

        return l

