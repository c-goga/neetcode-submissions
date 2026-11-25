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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = ((l1->val + l2->val) / 10 >= 1) ? 1 : 0;
        ListNode* newHead = new ListNode((l1->val + l2->val) % 10);
        ListNode* p = newHead;
        l1 = l1->next;
        l2 = l2->next;
        while (l1 || l2) {
            int num1 = l1 ? l1->val : 0;
            int num2 = l2 ? l2->val : 0;
            p->next = new ListNode((num1 + num2 + carry) % 10);
            carry = ((num1 + num2 + carry) / 10 >= 1) ? 1 : 0;
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
            p = p->next;
        }
        if (carry == 1) p->next = new ListNode(carry); 
        return newHead;
    }
};
