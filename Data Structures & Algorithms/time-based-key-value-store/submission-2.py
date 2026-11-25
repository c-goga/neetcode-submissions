class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        newKey = key + str(timestamp)
        self.store[newKey] = value

    def get(self, key: str, timestamp: int) -> str:
        newKey = key + str(timestamp)
        if newKey in self.store:
            return self.store[newKey]
        else:
            res = ""
            l, r = 1, timestamp
            while l <= r:
                # mid = l + r // 2
                # possibleKey = key + str(mid)
                # if possibleKey in self.store:
                #     l = mid + 1
                #     res = self.store[possibleKey]
                # else:
                #     r = mid - 1
                possibleKey = key + str(r)
                if possibleKey in self.store:
                    res = self.store[possibleKey]
                    break;
                r -= 1
            return res
