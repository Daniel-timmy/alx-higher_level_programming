#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: singly linked list.
 * Return: returns 1 upon success, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *cnt;
	listint_t *arr;
	int n = 0;
	int i = 0;
	int j;
	printf("start");
	if (*head == NULL)
	{
		return (0);
	}
	else
	{

		cnt = *head;
		arr = *head;
		printf("mid");

		while (cnt->next != NULL)
		{
			n++;
		}

		int data[n];

		printf("no of nodes: %d", n);
		while (arr->next != NULL)
		{
			data[i] = arr->n;
			i++;
		}

		i--;
		printf("compare %d", i);
		for (j = 0; j < n; j++, i--)
		{
			if (data[i] != data[j])
				return (0);
		}
	}
	return (1);
}
