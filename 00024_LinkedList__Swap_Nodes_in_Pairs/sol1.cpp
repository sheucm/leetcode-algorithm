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
    ListNode* swapPairs(ListNode* head) {

        if (!head) return NULL;
        if (!head->next) return head;

        ListNode* curr = head;
        ListNode* prev = NULL;
        while (curr) {
            if (curr == head) head = head->next;
            if (!_swap(prev, curr)) break;
            prev = curr;
            curr = curr->next;
        }
        return head;
    }
private:
    bool _swap(ListNode* prev, ListNode* n1) {
        if (!n1 || !n1->next) return false;
        ListNode* n2 = n1->next;
        ListNode* next = n2->next;

        n1->next = next;
        n2->next = n1;
        if (prev) prev->next = n2;
        return true;
    }
};