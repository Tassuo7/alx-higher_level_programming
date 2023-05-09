#include "lists.h"

/**
 * check_cycle - function that checks if a LL has a cycle
 * @list: the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *lista;

	if ((list) || (list->next))
		return (0);
	lista = list->next;
	while (lista != NULL && lista->next != NULL)
	{
		list = lista;
		lista = lista->next;
		if (lista == list)
			return (1);
	}
	return (0);
}
