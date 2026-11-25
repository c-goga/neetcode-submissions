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
    void reorderList(ListNode* head) {
        // brute force approach for now where i take fast pointer and go to the n -1.. n-m position then put it next to the slow pointer
        if (head == nullptr || head->next == nullptr) return;

        ListNode* l = head; //slow
        ListNode* r = head; //fast

        int size = 2;
        while (r->next->next != nullptr) {
            r = r->next;
            size++; // get size of list, will use this to know when we are done
        }

        for(int i = 0; i < (size - 1) / 2; i++) {
            ListNode* tmp = r->next;
            cout << tmp->val << endl;
            r->next = nullptr;
            tmp->next = l->next;
            l->next = tmp;
            cout << l->val << ", " << l->next->val << ", " << l->next->next->val << endl;
            l = l->next->next; // could cause issues
            r = l;
            if (r->next == nullptr) break;
            while (r->next->next != nullptr) { // also issues
                r = r->next;
            }
        }
    }
};
