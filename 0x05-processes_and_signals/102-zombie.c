#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * infinite_while - infinite loop
 * Return: Nothing
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - main function for zombies processes
 * Return: Integer status
 */
int main(void)
{
	pid_t child;
	int count = 0;


	while (count < 5)
	{
		child = fork();
		if (child == 0)
			exit(0);
		else if (child > 0)
		{
			printf("Zombie process created, PID: %d\n", child);
		}
		else
		{
			exit(0);
		}
		count++;
		printf("count %d\n", count);
	}
	infinite_while();
	printf("child %d %d\n", child, getpid());

	return (0);
}
