#include <stdio.h>
void main(){
    float c,f;
    printf("enter the temperature in degree celcius");
    scanf("%f",&c);
    f=(c*1.8)+32;
    printf("the temperature farenheit :%f",f);  
    getch();
}