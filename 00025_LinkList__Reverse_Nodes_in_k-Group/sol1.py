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

    def _get_last_node(self, head: ListNode):
        prev = None
        curr = head
        while curr:
            prev = curr
            curr = curr.next
        return prev

    def _merge(self,
        head_list: List[ListNode]
    ) -> ListNode:
        assert len(head_list) > 0

        head = head_list[0]

        for i in range(len(head_list) - 1):
            last = self._get_last_node(head)
            last.next = head_list[i+1]
        
        return head
            



    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        head_list = []
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

                # print(f'append list...')
                # self._print(reversed_head)
                head_list.append(reversed_head)

                prev = None
                curr = _next
                _next = None if not curr else curr.next
                _tmp_head = curr
            else:
                prev = curr
                curr = _next
                _next = None if not curr else curr.next
        
        if _tmp_head:
            head_list.append(_tmp_head)
        
        ans = self._merge(head_list)


        return ans

