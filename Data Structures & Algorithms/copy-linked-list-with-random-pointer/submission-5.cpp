/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;
        
        Node* l = head;
        while(l) {
            Node* n = new Node(l->val);
            n->next = l->next;
            l->next = n;
            l = l->next->next;
        }

        l = head;
        while (l) {
            if (l->random) l->next->random = l->random->next;
            l = l->next->next;
        }

        Node* r = head->next;
        Node* tmp = r;
        l = head->next->next;
        while (l) {
            tmp->next = l->next;
            l = l->next->next;
            tmp = tmp->next;
        }

        return r;
    }
};
