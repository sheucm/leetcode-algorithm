/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int SIZE = 0;
        ListNode* curr = head;

        while(curr) {
            SIZE++;
            curr = curr->next;
        }
        
        if (SIZE == 1) return NULL;

        int idx = SIZE - n;
        if (idx == 0) {
            curr = head;
            head = head->next;
            delete curr;
            return head;
        }

        int i = 0;
        ListNode* target = NULL;
        ListNode* next = NULL;
        ListNode* prev = head;
        while (i++ < idx - 1) {
            prev = prev->next;
        }

        target = prev->next;
        next = target->next;

        prev->next = next;
        target->next = NULL;
        delete target;
        return head;
    }
};