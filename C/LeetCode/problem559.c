/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */
#include <stdio.h>
struct Node {
     int val;
     int numChildren;
     struct Node** children;
};

int maxDepth(struct Node* root) {
    if (root == NULL){
        return 0;
    }
    if (root->numChildren == 0){
        return 1;
    }
    
    int maior = 0;
    struct Node* n;
    for (int i = 0; i < root->numChildren; i++){
        int tmp = maxDepth(root->children[i]) + 1;
        if (tmp > maior){
            maior = tmp;
        }
        
    }
    return maior;
}