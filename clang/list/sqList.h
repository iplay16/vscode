struct ListNode {
    int val;
    struct ListNode *next;
};

typedef struct ListNode ListNode;
ListNode *createListNode(int val);
ListNode *createList();
ListNode *createListwithhead();
void showList(ListNode *p);
void showListwithhead(ListNode *head);
void test_List();
int listsize(ListNode *p);
void showListwithhead(ListNode *head);
