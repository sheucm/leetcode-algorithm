class Solution:
    def trap(self, height: List[int]) -> int:
        _stack = []
        total_area = 0

        for x, y in enumerate(height):
            
            ## Get trap area
            if x != 0:
                right = x
                bottom = height[x-1]

                while (
                    len(_stack) > 0
                    and y > bottom
                ):
                    left = _stack.pop(-1)

                    top = min(height[left], y)
                    if height[left] > y:
                        _stack.append(left)
                    

                    area = (top - bottom) * (right - left - 1)
                    assert area >= 0, "Err: area should be > 0"
                    total_area += area

                    bottom = top
            
            # Push Stack
            if (
                x+1 < len(height)
                and y > height[x+1]
            ):
                _stack.append(x)

        return total_area




                
