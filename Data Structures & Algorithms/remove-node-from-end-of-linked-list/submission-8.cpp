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
        if (head == nullptr || head->next == nullptr) return nullptr;
        ListNode dummy(0, head);
        ListNode* slow = &dummy; // slow pointer
        ListNode* fast = head; // fast pointer

        while (n > 0) {
            fast = fast->next;
            n--;
        }


        while (fast != nullptr) {
            // move fast and slow pointer until end is reached
            fast = fast->next; 
            slow = slow->next;
        }

        // slow pointer now in right position, remove element nth from last
        slow->next = slow->next->next;
        return dummy.next;
    }
};
