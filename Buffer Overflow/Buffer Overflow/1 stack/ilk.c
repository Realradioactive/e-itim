#include <stdio.h>
#include <stdlib.h>

function1(int i){
	char *local_degisken = "Function 1";
	int loca_degisken2 = 0x44444444;
	
	return 1;	
}

int main(int argc, char *argv[])
{
	char *local_var1 = "Main Fonksiyonu";
	int local_var2 = 0x18221822;
	function1(0x18224444);
	return 0;
}
