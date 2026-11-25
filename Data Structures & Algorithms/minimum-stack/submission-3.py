class MinStack:

    def __init__(self):
        self.stack = []
        self.minList = []
        self.size = 0
        self.minListSize = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (self.size == 0 or val <= self.minList[self.minListSize - 1]):
            self.minList.append(val)
            self.minListSize += 1
        self.size += 1
        print('push', self.stack)
        print('push min', self.minList)

    def pop(self) -> None:
        print('pop b', self.stack, self.size)
        if self.stack[self.size-1] == self.minList[self.minListSize - 1]:
            del self.minList[len(self.minList) - 1]
            self.minListSize -= 1
        del self.stack[self.size-1]
        self.size -= 1
        print('pop a', self.stack)

    def top(self) -> int:
        print(self.size)
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        print('getmin', self.minList)
        return self.minList[self.minListSize - 1]
