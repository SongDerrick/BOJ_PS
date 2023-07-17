#include <stdio.h>
#include <stdlib.h>

int main(void) {
	
	int i, j;
	char *s = malloc(sizeof(char) * 1000000);
	//scanf("%s", s);
	gets(s);
	int count = 0;
	j = 0;
	
	for(i=0;i<1000000;i++)
	{
		if(s[i]=='\0'){
			break;}
		else if(s[i]==' '){
			count++;
			j++;}
		else 
			j++;
	}
	//printf("%d %d\n", j, count);
	//printf("%s\n",s);
	//printf("%c\n", s[j-1]);
	
	if(s[0]==' '&&s[j-1] == ' ')
		printf("%d", count-1);
	else if(s[0]== ' ')
		printf("%d", count);
	else if(s[j-1]== ' ')
		printf("%d", count);
	else
		printf("%d", count + 1);
		
	
	free(s);
	return 0;
}
