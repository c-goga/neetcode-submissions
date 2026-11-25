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

        // have to do size - 1 because sizes 3 and 4 only need 1 rotation, 5 and 6 need 2, 7 and 8 need 3 and so on...
        for(int i = 0; i < (size - 1) / 2; i++) {
            ListNode* tmp = r->next; // get temp since we are making end null again
            r->next = nullptr; // makes end null
            tmp->next = l->next; // makes next of end node the current next of l
            l->next = tmp; // next of l turns into end node
            l = l->next->next; // doesn't cause issues since we know l had two more nodes ahead of it
            r = l; // reset r to l then find end again
            if (r->next == nullptr) break; // if already at end, stop. this preventes issues with while loop immediately after as well
            while (r->next->next != nullptr) {
                r = r->next;
            }
        }
    }
};
