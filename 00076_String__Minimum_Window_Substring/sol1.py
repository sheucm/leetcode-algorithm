class Solution:    
    def _get_cnt_map(self, target: str) -> Dict[str, int]:
        _map = {}
        for c in target:
            if _map.get(c) is None:
                _map[c] = 1
            else:
                _map[c] += 1
        return _map

    def _is_ok(self, _cnt_m) -> bool:
        return len([v for v in _cnt_m.values() if v > 0]) == 0

    def minWindow(self, s: str, t: str) -> str:

        _cnt_m: Dict[str, int] = self._get_cnt_map(t)
        s_idx_list = [idx for idx, c in enumerate(s) if _cnt_m.get(c) is not None]

        # [queue] <-- : -1  until _cnt_m <= 0
        # --> [queue]: +1  until _cnt_m <= 0 but close to zero
        answer = ""
        queue = []
        for s_idx in s_idx_list:

            _cnt_m[s[s_idx]] -= 1
            queue.append(s_idx)

            if self._is_ok(_cnt_m):

                while _cnt_m[s[queue[0]]] + 1 <= 0:
                    _cnt_m[s[queue[0]]] += 1
                    queue = queue[1:]
                    
                # store answer
                tmp_answer = s[queue[0]:queue[-1]+1]
                if len(answer) == 0 or len(tmp_answer) < len(answer):
                    answer = tmp_answer

                # drop the first one
                _cnt_m[s[queue[0]]] += 1
                queue = queue[1:]

        return answer
                


