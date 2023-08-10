#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	if (!list)
		(return 0);

	listint_t *slow = list;
	listint_t *fast = list;

	do

	{
		slow = slow->next;
		fast = fast->next;

		if (!fast)
			(return 0);

		fast = fast->next;

		if (!fast)
			(return 0);

	} while (slow != fast);

	(return 1);
}

