#include "lists.h"


/**
 * print_dlistint - prints all the elements of a
 * dlistint_t list
 * @h: head of the list
 * Return: the number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *current = h;

	if (current == NULL)
		return 0;

	while (current->prev != NULL)
		current = current->prev;

	while (current != NULL)
	{
		printf("%d\n", current->n);
		current = current->next;
	}

	return (1);
}

