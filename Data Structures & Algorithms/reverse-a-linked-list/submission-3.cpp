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
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;
        
        ListNode* l = head;
        ListNode dummy(0, head); // sentinel node
        while (l->next != nullptr) { // stop on last element
            ListNode* tmp = l->next;
            l->next = l->next->next;
            dummy.next = tmp;
            tmp->next = head;
            head = dummy.next;
        }

        return dummy.next;
    }
};
