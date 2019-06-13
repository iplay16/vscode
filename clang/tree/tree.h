using namespace std;
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct TreeNode TreeNode;

TreeNode *createnode(int val);
TreeNode *init();
int depth(TreeNode *tree);
void preorder(TreeNode *root);
void BFSprint(TreeNode *p);
TreeNode *copytree(TreeNode *t);
