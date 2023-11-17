

class FreqStack:

    def __init__(self):
        self.max_level: int = 0
        self.level_stack: Dict[int, List[int]] = {}  # key: level,  val: level stack values
        self.level_map: Dict[int, int] = {}         # key: val,   val: level
        

    def push(self, val: int) -> None:
        self.level_map[val] = self.level_map.get(val, 0) + 1
        level = self.level_map[val]
        self.level_stack[level] = self.level_stack.get(level, []) + [val]
        self.max_level = max(self.max_level, level)
        
    def pop(self) -> int:
        assert len(self.level_stack[self.max_level]) > 0

        p_val = self.level_stack[self.max_level].pop(-1)
        if len(self.level_stack[self.max_level]) <= 0:
            self.max_level -= 1
        
        assert self.level_map[p_val] > 0
        self.level_map[p_val] -= 1

        return p_val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
