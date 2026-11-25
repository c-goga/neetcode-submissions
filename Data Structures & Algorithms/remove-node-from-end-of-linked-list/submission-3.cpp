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
        if (head == nullptr || head->next == nullptr) return nullptr; // size 1 or 2

        ListNode* slow = head;
        ListNode* fast = head;
        for (int i = 1; i < n; i++) {
            if (fast->next != nullptr) {
                fast = fast->next;
            }
        }

        // do this so that slow can stop one before the one that should be removed
        if (fast->next != nullptr) fast = fast->next;
        else return slow->next;

        while (fast->next != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }

        // if (slow == head) {
        //     cout << "1" << endl;
        //     return head->next;
        // } else {
            cout << "2" << endl;
            slow->next = slow->next->next;
            return head;
        // }
    }
};
