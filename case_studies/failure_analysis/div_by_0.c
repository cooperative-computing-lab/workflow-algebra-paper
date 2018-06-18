
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	time_t t;

	srand(atoi(argv[1]));

	char* useless = calloc(1, 1024*1024);

	int temp = rand() % 5;
	switch(temp){
		case 0:
			return 1/temp;
		default:
			return 0;
	}
}
