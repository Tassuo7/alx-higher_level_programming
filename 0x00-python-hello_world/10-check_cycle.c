#include "lists.h"

/**
 * check_cycle - function that checks if a LL has a cycle
 * @list: the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *lista, *listb;

	if (!list)
		return (0);
	lista = list;
	listb = list->next;
	while (lista && listb && listb->next)
	{
		if (lista == listb)
			return (1);
		lista = lista->next;
		listb = listb->next->next;
	}
	return (0);
}
