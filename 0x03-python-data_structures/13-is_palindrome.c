#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	int tmp[25];
	listint_t *current;
	int up = 0, down = 0, number = 0;

	if (*head == NULL)
		return (1);

	current = *head;
	while (current != NULL)
	{
		tmp[number] = current->n;
		current = current->next;
		number++;
	}

	if (number % 2 == 0)
	{
		up = number / 2;
		down = number / 2 - 1;
	}
	else
	{
		up = number / 2;
		down = number / 2 - 2;
	}

	while (down >= 0)
	{
		if (tmp[up] != tmp[down])
			return (0);
		down--;
		up++;
	}
	return (1);
}



