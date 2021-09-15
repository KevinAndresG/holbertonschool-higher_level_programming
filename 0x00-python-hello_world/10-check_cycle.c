#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it
 * @list: it is the list
 * Return: an int
 */
int check_cycle(listint_t *list)
{
	while (list)
	{
		if (list->next >= list)
		{
			return (1);
		}
		list = list->next;
	}
}
