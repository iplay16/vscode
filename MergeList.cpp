#include "sqList.h"
struct ListNode *mergeTwoLists(struct ListNode *l1, struct ListNode *l2)
{
    ListNode *head = createListNode(0);
    ListNode *l3 = head;
    while (l1 != NULL && l2 != NULL)
    {
        if (l1->val < l2->val)
        {
            l3->next = l1;
            l1 = l1->next;
            l3 = l3->next;
        }
        else
        {
            l3->next = l2;
            l2 = l2->next;
            l3 = l3->next;
        }
    }

    if (l1 != NULL && l2 == NULL)
    {
        while (l1)
        {
            l3->next = l1;
            l1 = l1->next;
            l3 = l3->next;
        }
    }
    if (l1 == NULL && l2 != NULL)
    {
        while (l2)
        {
            l3->next = l2;
            l2 = l2->next;
            l3 = l3->next;
        }
    }
    l3->next = NULL;
    l3 = head->next;
    return l3;
}

void test_mergeTwoLists()
{
    ListNode *l1 = createList();
    ListNode *l2 = createList();
    showList(l1);
    showList(l2);
    ListNode *l3 = mergeTwoLists(l1, l2);
    showList(l3);
}

int main()
{
    test_mergeTwoLists();
    exit(0);
}
