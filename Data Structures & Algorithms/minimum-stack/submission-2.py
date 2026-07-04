class MinStack:

    def __init__(self):
        self.q = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.minStack.append(min(val, self.minStack[-1] if len(self.minStack) > 0 else val))
        self.q.append(val)

    def pop(self) -> None:
        self.q.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
