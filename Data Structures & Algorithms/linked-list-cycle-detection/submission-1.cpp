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
    bool hasCycle(ListNode* head) {
        // Creates a map. The key is the node and value is the int.
        std::map<ListNode*, int> nodes;
        while (head != nullptr) {
            if (!nodes.contains(head)) {
                nodes[head] = head->val;
            } else {
                return true;
            }
            head = head->next;
        }
        return false;
    }
};
