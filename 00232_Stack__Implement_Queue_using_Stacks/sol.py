class MyQueue:

    def __init__(self):
        self.st = []
        self.r_st = [] # reversed stack

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        if not self.r_st:
            while self.st:
                p = self.st.pop()
                self.r_st.append(p)
        return self.r_st.pop()

    def peek(self) -> int:
        if not self.r_st:
            while self.st:
                p = self.st.pop()
                self.r_st.append(p)
        return self.r_st[-1]

    def empty(self) -> bool:
        return not self.st and not self.r_st


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()