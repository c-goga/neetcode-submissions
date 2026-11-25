class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] =  freq[num] + 1

        print(freq)
        
        l = list(freq.keys())[:k]

        for key, value in list(freq.items())[k:]:
            print("list:")
            print(l)
            min = [-1, 0]
            print(min[1])
            for i in range(len(l)):
                print("in loop")
                print(key)
                print(value)
                print(freq[l[i]])
                if value > freq[l[i]]:
                    if min[0] == -1:
                        min[0] = i
                        min[1] = freq[l[i]]
                    elif min[1] > freq[l[i]]:
                        min[0] = i
                        min[1] = freq[l[i]]
                print(min)
            if min[0] != -1:
                l[min[0]] = key

            
        # for i in range(len(l)):
        #     l[i] = freq[l[i]]
        
        return l

                    
