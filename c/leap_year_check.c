#include<stdio.h>
void main(){
    int y;
    printf("enter the year:");
    scanf("%d",&y);
    if (y%4==0 || y%400==0){
        printf("this year is a leap year");   
    }
    else{
        printf("thie is not a leap year");
    }
}