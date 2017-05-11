#include <iostream>
#include <vector>

using namespace std;

typedef struct Node 
{
  int num;
  int idx;
  Node* left;
  Node* right;
} Node ;

/**
 * Class BinaryTree.
 * @brief    Binary Tree for holding the integers. Just implemented for brushup, albeit not a good approach.
 *           Directly operate on the indices of the integer-array using binary-search for a faster solution.
 */
class BinaryTree
{
public:
  explicit BinaryTree():root(NULL)
  {}
  void initTree(const vector<int>& nums)
  {
    int idx = 0;
    for (auto it=nums.cbegin(); it!= nums.cend(); ++it) {
      insert(*it,idx);
      ++idx;
    }
  }
  void insert(int num, int idx) 
  {
    if (root != NULL) {                     // elements are already present in the tree
      insertElement(num,idx,root);
    }
    else {                                  // this is the first element to be inserted into the tree
      root = new Node;
      root->num = num;
      root->idx = idx;
      root->left = NULL;
      root->right = NULL;
    }
  }
  int searchIndex(int target, Node* parent)
  {
    int idx = -1;
    if (parent == NULL) return idx;
    if (target == parent->num) {
      idx = parent->idx;
    }
    else if (target < parent->num) {        // search left subtree      
      if (parent->left == NULL) return -1;
      idx = searchIndex(target,parent->left);
    }
    else if (target > parent->num) {        // search right subtree
      if (parent->right == NULL) return -1;
      idx = searchIndex(target,parent->right);
    }
    return idx;
  }
  void print()
  {
    if (root == NULL) {
      cout << "tree empty\n";
      return;
    }
    inorderTraverse(root);
  }
  Node* getRoot() {
    return root;
  }

private:
  Node* root;
  void insertElement(int num, int idx, Node* parent) 
  {
    if (num <= parent->num) {               // insert the new element into the left subtree      
      if (parent->left != NULL) {           // left-subtree not empty
        insertElement(num,idx,parent->left);
      }
      else {  
        Node* pn = new Node;                // left-subtree is empty, insert the first left-node
        pn->num = num;
        pn->idx = idx;
        pn->left = NULL; 
        pn->right = NULL; 
        parent->left = pn;
      }      
    }
    else {                                  // insert the new element into the right subtree
      if (parent->right != NULL) {
        insertElement(num,idx,parent->right);
      }
      else {
        Node* pn = new Node;
        pn->num = num;
        pn->idx = idx;
        pn->left = NULL;
        pn->right = NULL;
        parent->right = pn;
      }
    }
  }
  void inorderTraverse(Node* node) 
  {
    if (node == NULL) return;
    inorderTraverse(node->left);
    cout << node->idx << "\t" << node->num << "\n";
    inorderTraverse(node->right);    
  }
};

class Solution 
{
public:
  Solution():pbt(NULL)
  {}
  int search(vector<int>& nums, int target) 
  {
    if (!nums.size()) return -1;
    pbt = new BinaryTree();
    pbt->initTree(nums);
    // pbt->print();                       // prints the tree, inorder traversal.
    int idx = pbt->searchIndex(target,pbt->getRoot());
    return idx;
  }
private:
  BinaryTree* pbt;
};


/**
 * @brief    Solution to Leetcode problem 33.
 * @details  URL : https://leetcode.com/problems/search-in-rotated-sorted-array/#/description
 */
int main() 
{
  vector<int> nums = {1,3};
  Solution s;
  int idx = s.search(nums,2);
  cout << idx << "\n";
  return 0;
}