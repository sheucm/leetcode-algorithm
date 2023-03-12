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
    ListNode* oddEvenList(ListNode* head) {

        if (!head) return NULL;
        if (!head->next) return head;
        
        ListNode* first_list_head = NULL;
        ListNode* first_list_tail = NULL;
        ListNode* second_list_head = NULL;
        ListNode* second_list_tail = NULL;

        int cnt = 0;
        ListNode* curr = head;
        ListNode* tmp_next = NULL;
        while (curr) {
            cnt++;

            if (curr->next) tmp_next = curr->next;
            curr->next = NULL;

            if (cnt % 2 == 1) {
                if (!first_list_head) {
                    first_list_head = curr;
                    first_list_tail = curr;
                }
                else {
                    first_list_tail->next = curr;
                    first_list_tail = curr;
                }
            }
            else {
                if (!second_list_head) {
                    second_list_head = curr;
                    second_list_tail = curr;
                }
                else {
                    second_list_tail->next = curr;
                    second_list_tail = curr;
                }
            }

            curr = tmp_next;
            tmp_next = NULL;
        }


        first_list_tail->next = second_list_head;
        return first_list_head;

    }
};