#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to list to be freed
 * Return: int
 */
 int check_cycle(listint_t *list)
 {
	listint_t *current;
 
	if (list == NULL)
		return (0);

	current = list->next;
	while (current != NULL)
	{
		if (current == list)
			return (1);
		current = current->next;
	}
	return (0);
 }
