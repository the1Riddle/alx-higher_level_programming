#include "lists.h"

/**
 * check_cycle - checks for cycle in a linked list
 * @l: list to be checked
 *
 * Return: 1 if the list has a cycle else 0.
 */
int check_cycle(listint_t *l)
{
	listint_t *slow = l;
	listint_t *fast = l;

	if (l == NULL)
	{
		return (0);
	}
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
