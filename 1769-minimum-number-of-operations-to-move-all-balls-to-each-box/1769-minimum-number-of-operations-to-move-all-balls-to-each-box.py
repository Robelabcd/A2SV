class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        counter = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                counter.append(i)
        ans = []
        for i in range(len(boxes)):
            temp = 0
            for y in counter:
                temp += abs(i - y)
            ans.append(temp)

        return ans