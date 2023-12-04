#include "lists.h"

/**
 * insert_node - inserts a number in a sorted list
 * @head: address of the pointer to the head
 * @number: the number to be added
 *
 * Return: pointer to the added node, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nw_node, *front = NULL, *back = NULL;

	if (head && *head)
		front = *head;

	while (front && front->next && (front->n < number))
	{
		back = front;
		front = front->next;
	}

	nw_node = malloc(sizeof(listint_t));
	if (nw_node)
	{
		nw_node->n = number;
		if ((front == *head) || !front)
		{
			nw_node->next = front;
			*head = nw_node;
		}
		else if (front->next)
		{
			nw_node->next = front;
			back->next = nw_node;
		}
		else
		{
			nw_node->next = front->next;
			front->next = nw_node;
		}
	}

	return (nw_node);
}
