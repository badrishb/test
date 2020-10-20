
#include<stdio.h>
#include<string.h>
int get_min(int a, int b)
{
if(a < b)
return a;
return b;
}
int edit_distance(char *s1, char *s2)
{
int len1,len2,i,j,min;
len1 = strlen(s1);
len2 = strlen(s2);
int arr[len1 + 1][len2 + 1];
for(i = 0;i <= len1; i++)
arr[i][0] = i;
for(i = 0; i <= len2; i++)
arr[0][i] = i;
for(i = 1; i <= len1; i++)
{
for(j = 1; j <= len2; j++)
{
min = get_min(arr[i-1][j],arr[i][j-1]) + 1;
if(s1[i - 1] == s2[j - 1])
{
if(arr[i-1][j-1] < min)
min = arr[i-1][j-1];
}
else
{
if(arr[i-1][j-1] + 1 < min)
min = arr[i-1][j-1] + 1;
}
arr[i][j] = min;
}
}
return arr[len1][len2];
}
int main()
{
char s1[] = "monday", s2[] = "tuesday";
int ans = edit_distance(s1, s2);
printf("%d",ans);
return 0;
}
