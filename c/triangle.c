#include<stdio.h>
#include<math.h>
void main(){
    int a,b,c;
    printf("enter the three sides of the triangle:\n");
    scanf("%d%d%d",&a,&b,&c);
    float s,s1;
    s1=(a+b+c)/2;
    s=s1*(s1-a)*(s1-b)*(s1-c);
    s=pow(s,(0.5));
    s1=s1*2;
    printf("area of the triangle:%f and perimeter:%f",s,s1);
}