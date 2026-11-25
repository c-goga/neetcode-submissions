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
        unordered_map<Node*, Node*> mp; // map used to find deep copy address
        Node* tmp = head; // pointer for original list
        Node* n = new Node(tmp->val); // head of deep copy list
        Node* tmp2 = n; // pointer for deep copy list
        mp[tmp] = n; // enter head into map where value is n
        while(tmp->next) {
            Node* m = new Node(tmp->next->val); // next node
            if (!mp[tmp->next]) {
                mp[tmp->next] = m;
                tmp2->next = m; // add to deep copy of list
            } else {
                tmp2->next = mp[tmp->next];
            }

            if (tmp->random) {
                Node* r = new Node(tmp->random->val); // random node
                if (!mp[tmp->random]) {
                    mp[tmp->random] = r;
                    tmp2->random = r;
                } else {
                    tmp2->random = mp[tmp->random];
                }
            }
            // mp[tmp->next] = m; // put into map
            
            tmp2 = tmp2->next; // continue on using deep copy pointer
            tmp = tmp->next; // continue on original list
        }

        if (tmp->random) {
            Node* r = new Node(tmp->random->val); // random node
            if (!mp[tmp->random]) {
                mp[tmp->random] = r;
                tmp2->random = r;
            } else {
                tmp2->random = mp[tmp->random];
            }
        }

        // // now we need to pass through again put look at random this time using the map entries we put in
        // tmp = head; // reset original
        // tmp2 = n; // reset deep copy
        // while (tmp && tmp2) { // tmp2 check not needed but i like it for readability
        //     tmp2->random = mp[tmp->random]; // get node of deep copy that matches original
        //     tmp = tmp->next; // move original forward
        //     tmp2 = tmp2->next; // move deep copy forward
        // }
        
        return n; // return deep copy
    }
};
