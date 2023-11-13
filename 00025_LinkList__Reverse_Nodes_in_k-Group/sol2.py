# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def _reverse(self, 
        head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head:
            return head

        curr = head
        _prev = None
        _next = None
        while curr:
            _next = curr.next
            curr.next = _prev

            _prev = curr
            curr = _next
        
        return _prev

    def _print(self, 
        head: Optional[ListNode]
    ) -> None:
        if not head:
            return "(none)"
        curr = head
        msg = ""
        while curr:
            msg += f"{curr.val} -> "
            curr = curr.next
        print(msg)


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        _ans = head

        _tmp_head_prev = None
        _tmp_head = head
        prev = None
        curr = head
        _next = curr.next
        cnt = 0
        while curr:
            cnt += 1
            if cnt % k == 0:
                curr.next = None
                reversed_head = self._reverse(_tmp_head)

                _new_tail = _tmp_head
                _new_head = reversed_head

                if cnt == k:
                    _ans = _new_head

                if _tmp_head_prev:
                    _tmp_head_prev.next = _new_head
                _new_tail.next = _next

                prev = _new_tail
                curr = _next
                _next = None if not curr else curr.next
                _tmp_head = curr
                _tmp_head_prev = _new_tail
            else:
                prev = curr
                curr = _next
                _next = None if not curr else curr.next


        
        return _ans

