# A+B - 2, 2020년 8월 1일 22:58:32, 1112kb, 0ms, 203b
#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
int main()
{
    int a,b;
    scanf("%d %d",&a,&b);
    if(a<=0||a>=b||b>=10)
      scanf("%d %d",&a,&b);
    printf("%d",a+b);
    return 0;
}
