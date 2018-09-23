typedef struct node{
    int data;
    struct node* next;
} node;

node * new_node(int val)
{
    node *temp = (node *)malloc(sizeof(node));

    temp->data = val;
    temp->next = NULL;
    return temp;
}