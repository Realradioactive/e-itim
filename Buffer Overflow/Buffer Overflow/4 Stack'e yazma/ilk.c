#include <stdio.h>
#include <stdlib.h>


calistir(){
	printf("isminiz nedir?\n");
	char mesaj[10];
	gets(mesaj);//kullanicidan veri al
	printf(mesaj);
	
	return 1;	
}

int main(int argc, char *argv[])
{
	char *local_var1 = "Main Fonksiyonu";
	int local_var2 = 0x18221822;
	calistir(local_var2);
	return 0;
}
