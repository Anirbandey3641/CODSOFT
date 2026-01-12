#include <stdio.h>
int main(){
    float si,r,t,p;
    printf("enter the principal amount,rate of interest and time");
    scanf("%f%f%f",&p,&r,&t);
    si=(p*r*t)/100;
    printf("the simple interest is %f",si);
    return 0;
}