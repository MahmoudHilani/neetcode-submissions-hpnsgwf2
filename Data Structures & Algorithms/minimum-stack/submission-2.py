class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = deque()

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minSt or val <= self.minSt[-1]:
            self.minSt.append(val)
        else:
            self.minSt.appendleft(val)

    def pop(self) -> None:
        val = self.st.pop()
        if val == self.minSt[-1]:
            self.minSt.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minSt[-1]
