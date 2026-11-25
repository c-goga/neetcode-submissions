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
        int carry = ((l1->val + l2->val) / 10 >= 1) ? 1 : 0; // represents carrying a 1 to the next place when the sum of digits is >= 10
        ListNode* newHead = new ListNode((l1->val + l2->val) % 10); // create head of new list
        ListNode* p = newHead; // get pointer for new list
        l1 = l1->next; // change positions of both lists forward
        l2 = l2->next;
        while (l1 || l2) { // if either are not null
            int num1 = l1 ? l1->val : 0; // if not null then l1->val, null then 0
            int num2 = l2 ? l2->val : 0; // if not null then l2->val, null then 0
            p->next = new ListNode((num1 + num2 + carry) % 10); // create new list node using carry and (% 10) because it can only be a single digit
            carry = ((num1 + num2 + carry) / 10 >= 1) ? 1 : 0; // reset carry
            l1 = l1 ? l1->next : l1; // move both list forward if available
            l2 = l2 ? l2->next : l2;
            p = p->next; // move new pointer of list forward
        }
        if (carry == 1) p->next = new ListNode(carry); // if carry still left over create one last node with 1 as it's value
        return newHead; // return new list
    }
};
