#include <stdio.h>
void main(){
    int i,s,max;
    printf("enter the size of the array");
    scanf("%d",&s);
    int a[s];
    
    printf("enter the values; \n");
    for (i = 0; i < s; i++){
        scanf("%d",&a[i]);
    }
    max=a[0];
    for ( i = 0; i <s; i++){
        if(a[i]>max){
            max=a[i];
        }
    }
    printf("the max value is %d",max);
    
}