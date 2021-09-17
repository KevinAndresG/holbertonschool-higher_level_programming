#include "lists.h"
/**
 * dlistint_len - return number of elements in a list
 *
 * @h: an struct
 * Return: a size_t
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t n = 0;

	while (h != NULL)
	{
		h = h->next;
		n++;
	}
	return (n);
}
