#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: the head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *node = *head;
	int list[], rect = 0, vers = 0;

	if (!*head || !(*head)->next)
		return (1);
	while (tail)
	{
		list[vers] = node->n;
		node = node->next;
		vers++;
	}
	vers--;
	while (vers >= rect)
	{
		if (list[rect] != list[vers])
			return (0);
		rect++;
		vers--;
	}
	return (1);
}
