#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>

/* ------------- [ STRUCTURE ]----------------- */
// DLL Node
typedef struct DLLNode
{
    int data;

    struct DLLNode *next;
    struct DLLNode *prev;
} DLLNode;

/* ------------- [ CREATION ]----------------- */
// Create a new node
DLLNode *create_node(int val)
{
    // Allocating the memory for the data
    DLLNode *new_node = (DLLNode *)malloc(sizeof(DLLNode));

    // Check for memory error
    if (!new_node)
    {
        perror("Memory error");
        exit(0);
    }

    // Create the new node
    new_node->data = val;
    new_node->next = NULL;
    new_node->prev = NULL;

    //  Return the node
    return new_node;
}

/* ------------- [ INSERTION ]----------------- */
// insert value at the beginning
void push(DLLNode **head_ref_ref, int val)
{
    DLLNode *new_node = create_node(val);
    // If head is NULL
    if (*head_ref_ref == NULL)
    {
        // Make head = New_node
        *head_ref_ref = new_node;
    }
    // If head is not NULL
    else
    {
        new_node->next = *head_ref_ref;
        (*head_ref_ref)->prev = new_node;
        (*head_ref_ref) = new_node;
    }
}

// Insert at the end
void append(DLLNode **head_ref, int val)
{
    DLLNode *new_node = create_node(val);

    // If head is empty
    if (*head_ref == NULL)
    {
        *head_ref = new_node;
    }
    else
    {
        DLLNode *last = *head_ref;
        // Search the last node
        while (last->next != NULL)
        {
            last = last->next;
        }

        // Make new_node->left = last
        new_node->prev = last;
        // Make last->next = new_node
        last->next = new_node;
    }
}

// Insert after a given value
void insert_after(DLLNode **head_ref, int item, int val)
{
    // Make a pointer to the head
    DLLNode *ptr = *head_ref;
    DLLNode *new_node;

    // Search the item pos
    while(ptr->data != item)
    {
        // If ptr is NULL then the searched item doesn't exist
        if(ptr == NULL)
        {
            printf("Position not found");
            return;
        }
        // Goto the next node
        ptr = ptr->next;
    }

    // Now ptr has the required node to be inserted after
    // Now create the node Insert it without breaking the link
    new_node = create_node(val);
    // Make new_node->prev = current node
    new_node->prev = ptr;
    // Make new_node->next = current node->next
    new_node->next = ptr->next;

    // Now break the link between two nodes 
    // First break the current -> next node
    ptr->next->prev = new_node;
    // Now break the current link to next
    ptr->next = new_node;

}

/* ------------- [ DELETION ]----------------- */
// Deleting the first node
void remove_first(DLLNode **head_ref)
{
    // Take a pointer to the location of the head 
    DLLNode *temp = *head_ref;

    // Make head = the next node of head
    (*head_ref) = (*head_ref)->next;
    // Make head -> prev = NULL
    (*head_ref)->prev = NULL;

    // Free the temp location
    free(temp);
}

// Deleting the last node
void remove_last(DLLNode **head_ref)
{
    // Taking two pointers last to point the last 
    // and pre_last to point the previous last element
    DLLNode *last = *head_ref, *pre_last=NULL;
    while(last->next != NULL)
    {
        pre_last = last;
        last= last->next;
    }

    // Make pre_last next to null
    pre_last->next = NULL;
    // Make last->prev = NULL
    last->prev = NULL;
    // Free the last
    free(last);
}

// Deleting the intermediate node
void remove_at(DLLNode **head, int val)
{
    DLLNode *prev_node=NULL,*curr_node,*next_node=NULL;
    curr_node = *head;

    while(curr_node->data != val && curr_node!= NULL)
    {
        curr_node = curr_node->next; //Set current node to next node
        prev_node = curr_node->prev; //Set previous node
        next_node = curr_node->next; //Set next node
    }
    printf("PREV: %d CURR: %d NEXT:%d",prev_node->data,curr_node->data,next_node->data);
    // IF curr_node == NULL then return 
    if(curr_node == NULL)
    {
        printf("Node not exist");
        return;
    }

    // Else set the nodes 
    prev_node->next = next_node;
    next_node->prev = prev_node;

    // Free the current node
    free(curr_node);
}

/* ------------- [ DISPLAY ]----------------- */
// Print the list
void print_list(DLLNode **head_ref)
{
    DLLNode *ptr = *head_ref;
    printf("\n[");
    while (ptr != NULL)
    {
        printf(" %d ", ptr->data);
        ptr = ptr->next;
    }
    printf("]\n");
}

/* ------------- [ MAIN ]----------------- */
int main(int argc, char const *argv[])
{
    DLLNode *head = NULL;
    push(&head, 1);
    print_list(&head);
    push(&head, 2);
    print_list(&head);
    push(&head, 3);
    print_list(&head);
    push(&head, 4);
    print_list(&head);

    append(&head, 5);
    print_list(&head);
    append(&head, 6);
    print_list(&head);
    append(&head, 7);
    print_list(&head);
    append(&head, 8);
    print_list(&head);
    append(&head, 9);
    print_list(&head);

    insert_after(&head,1, 10);
    print_list(&head);
    insert_after(&head,1, 11);
    print_list(&head);
    insert_after(&head,1, 12);
    print_list(&head);
    insert_after(&head,1, 13);
    print_list(&head);
    insert_after(&head,1, 15);
    print_list(&head);

    remove_first(&head);
    print_list(&head);
    remove_last(&head);
    print_list(&head);
    remove_at(&head,13);
    print_list(&head);
    remove_at(&head,11);
    print_list(&head);
    remove_at(&head,3);
    print_list(&head);

    return 0;
}
