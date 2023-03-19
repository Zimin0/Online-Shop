#include <stdio.h> 
#include <string.h>
int sub_main(char* str)
{    
   char sep [2]=" ";
   char *istr;
   char *pre_last = "";

   istr = strtok(str,sep);
   
   while (1){
	   if (istr == NULL) {
		   break;
	   }
	   printf ("%s ",pre_last);
	   pre_last = istr;
      istr = strtok (NULL,sep);
   }
   printf ("\n");
   return 0;
}



void main(){
	char arr_of_strings[20][129];
	char str_orig[] = {"\0"};

	printf("------------Input------------\n");

	////////////////////////Input////////////////////////
	for (int i = 0; i < 20; i++) {
		char str[129];
		gets(arr_of_strings[i]); 
		if (!strcmp(arr_of_strings[i], str_orig )){
			break;
		}
	}
	printf("-----------------------------");
	////////////////////////////////////////////////////
	///////////////////////Output///////////////////////
	printf("\n\nOUTPUT:\n");
		for (int i = 0; i < 20; i++){
		char new_word[129];
		if (!strcmp(arr_of_strings[i], str_orig )){
			printf("End of reading!");
			break;
		}
		printf("--------------line-%d--------------\n", i);
		sub_main(arr_of_strings[i]);
		printf("-----------------------------------\n", i);
	}
	////////////////////////////////////////////////////
}
