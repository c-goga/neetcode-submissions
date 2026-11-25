class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] =  freq[num] + 1

        l = list(freq.keys())[:k]

        for key, value in list(freq.items())[k:]:
            min = [-1, 0]
            for i in range(len(l)):
                if value > freq[l[i]]:
                    if min[0] == -1:
                        min[0] = i
                        min[1] = freq[l[i]]
                    elif min[1] > freq[l[i]]:
                        min[0] = i
                        min[1] = freq[l[i]]
            if min[0] != -1:
                l[min[0]] = key
        
        return l

                    
