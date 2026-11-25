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
    ListNode* reverse(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr) {
            ListNode* tmp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tmp;
        }
        return prev;
    }

    void reorderList(ListNode* head) {
        // this solution involves putting the list into two halves where the bigger side when odd is on the right side of the list
        if (head == nullptr || head->next == nullptr) return; // size 0 or 1

        ListNode* l = head; // slow
        ListNode* r = head->next; // fast 
        // cout << l->val << endl;
        while (r && r->next) { // may not work with size 3
            l = l->next;
            r = r->next->next;
        }

        // cout << l->val << endl;
        // cout << r->val << endl;
        r = l->next;
        l->next = nullptr;
        l = head;

        // reverse right list
        r = reverse(r);

        while (l && r) {
            ListNode* tmp = l->next;
            l->next = r;
            r = r->next;
            l->next->next = tmp;
            l = tmp;
        }
    }
};
