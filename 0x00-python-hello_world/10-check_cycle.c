#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to list to be freed
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *test;
	int count, count_test;

	if (list == NULL)
		return (0);

	current = list->next;
	count = 1;
	while (current != NULL)
	{
		test = list;
		count_test = 0;
		while (count_test != count - 1)
		{
			if (current == test || current == test->next)
				return (1);
			test = test->next->next;
			count_test = count_test + 2;
		}
		current = current->next;
		count++;
	}
	return (0);
}
