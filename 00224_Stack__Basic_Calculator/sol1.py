class Solution:

    def _cal (self,
        s: str
    ) -> int:
        
        assert len(s) > 0

        prev = 0
        sign = 1
        tmp = ""
        
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            sign = -1


        for ch in s:
            if ch == '+':
                prev = prev + sign * int(tmp)
                tmp = ""
                sign = 1
            elif ch == '-':
                prev = prev + sign * int(tmp)
                tmp = ""
                sign = -1
            else:
                tmp += ch
        if tmp:
            prev = prev + sign * int(tmp)
        return prev

    def calculate(self, s: str) -> int:

        _stack = []
        for ch in s:
            if ch == ' ':
                continue
            elif ch == '(':
                _stack.append(ch)
            elif ch == ')':
                tmp_s = ""
                while True:
                    pop_s = _stack.pop(-1)
                    if pop_s == '(':
                        break
                    tmp_s = pop_s + tmp_s
                integer = self._cal(tmp_s)
                if integer < 0 and len(_stack) > 0:
                    pop_t = _stack.pop(-1)
                    if pop_t == '-':
                        integer *= -1
                        _stack.append('+')
                _stack.append(str(integer)) 
            else:
                _stack.append(ch)
        
        
        tmp_s = ""
        while _stack:
            pop_s = _stack.pop(-1)
            tmp_s = pop_s + tmp_s
        integer = self._cal(tmp_s)
        return integer

        
        
                
                

