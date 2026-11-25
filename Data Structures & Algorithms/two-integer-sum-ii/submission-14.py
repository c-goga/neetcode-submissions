class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        res = [0] * 2
        found = False
        while i < len(numbers):
            j = i + 1
            while j < len(numbers):
                print(numbers[i])
                print(numbers[j])
                if numbers[i] + numbers[j] == target:
                    found = True
                    res[0] = i + 1
                    res[1] = j + 1
                    break
                j += 1
            if found:
                break
            i += 1

        return res