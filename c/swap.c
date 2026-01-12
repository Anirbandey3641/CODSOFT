#include <stdio.h>
void main(){
    int a,b;
    printf("enter 2 numbers a and b:");
    scanf("%d%d",&a,&b);
    a=a+b;
    b=a-b;
    a=a-b;
    printf("the numbers  are swaped a=%d and b=%d",a,b);
}