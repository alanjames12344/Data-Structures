#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

typedef struct Node
{
    int data;
    struct Node *next;
} node;

node *create_node(int val)
{
    node *temp = (node *)malloc(sizeof(node));
    if (temp == NULL) //Dynamic memory allocation error / Exception generated
        perror("Node Creation error");

    temp->data = val;
    temp->next = NULL;
    return temp;
}


/* Given a reference (pointer to pointer) to the head of a list 
   and an int,  inserts a new node on the front of the list. */
void push(struct Node** head_ref, int new_data) 
{ 
    /* 1. allocate node */
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node)); 
   
    /* 2. put in the data  */
    new_node->data  = new_data; 
   
    /* 3. Make next of new node as head */
    new_node->next = (*head_ref); 
   
    /* 4. move the head to point to the new node */
    (*head_ref)    = new_node; 
} 

/* Insert node after a given value of the node */
void insert_after(node ** prev_node, int val1, int val2)
{
    // Check the data kept in prev_node (a reference to the head)
    while((*prev_node)->data != val1)
    {
        if((*prev_node) == NULL )
        {
            printf("%d Not Found",val1);
            return;
        }
        // Hold the address of next address of the head pointer in prev_node 
        // this way the prev_node will be shifted to next node but this will not affect the head
        // (*prev_node)->next gives the value of next address of *prev_node
        // to hold the address we have to use & before that , it gives the address of next of prev_node.
        prev_node = &((*prev_node)->next);
    }

    // Create new node
    node *new_node = (node *)malloc(sizeof(node));
    // Store the data
    new_node->data = val2;
    // Make new->next  = current_node->next
    new_node->next = (*prev_node)->next;
    // Make current_node->next = new_node
    (*prev_node)->next = new_node;
}


void printList(node *ptr)
{
    while (ptr != NULL)
    {
        printf(" %d ", ptr->data);
        ptr = ptr->next;
    }
}

int main(int argc, char const *argv[])
{
    node *head = NULL;
    head = create_node(1);
    head->next = create_node(3);
    push(&head,2);
    insert_after(&head,3,4);

    printList(head);
    return 0;
}
