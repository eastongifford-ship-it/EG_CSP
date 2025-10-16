// 3rd period - Update Hello World assignment
#include <stdio.h>


void say_hello(const char *name) {
	if (name[0] == '\0')
		printf("Hello, stranger!\n");
	else
		printf("Hello, %s!\n", name);
}

int main(void) {
	say_hello("Aisha");
	say_hello("Chris");
	say_hello("Maya");
	say_hello("Liam");
	say_hello("Noah");
	return 0;
}

