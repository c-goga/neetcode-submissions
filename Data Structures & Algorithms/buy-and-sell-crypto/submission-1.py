class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = [0, prices[0]]
        maximum = [0, prices[0]]
        res = 0
        for i in range(1, len(prices)):
            print('min', minimum)
            print('max', maximum)
            if prices[i] < minimum[1]:
                minimum[0] = i
                minimum[1] = prices[i]
                maximum[1] = 0
                continue;
            if prices[i] > maximum[1]:
                maximum[0] = i
                maximum[1] = prices[i]
            if maximum[0] > minimum[0] and maximum[1] - minimum[1] > res:
                res = maximum[1] - minimum[1]
                print('res', res)

        return res
        