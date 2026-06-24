class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty, val is the min. Otherwise, it's the min of val and the current min.
        if self.min_stack:
            val = min(val, self.min_stack[-1])
        self.min_stack.append(val)

    def pop(self) -> None:
        # The problem guarantees pop is always called on a non-empty stack
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # The problem guarantees top is always called on a non-empty stack
        return self.stack[-1]

    def getMin(self) -> int:
        # The problem guarantees getMin is always called on a non-empty stack
        return self.min_stack[-1]