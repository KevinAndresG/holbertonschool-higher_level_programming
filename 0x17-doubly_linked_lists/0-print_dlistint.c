#include "lists.h"
/**
 * print_dlistint - print an list
 *
 * @h: an struct
 * Return: a size_t
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t n = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		n++;
	}
	return (n);
}
