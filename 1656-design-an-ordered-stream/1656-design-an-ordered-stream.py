class OrderedStream:

    def __init__(self, n: int):
        self.values = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1  # Adjust idKey to be zero-based
        self.values[idKey] = value
        chunk = []

        # Check if the current position is filled and consecutive values are available
        while self.ptr < len(self.values) and self.values[self.ptr] is not None:
            chunk.append(self.values[self.ptr])
            self.ptr += 1

        return chunk
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)