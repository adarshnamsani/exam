import java.lang.*;
import java.util.Scanner;
class B
{
public static void main(String ar[])
{
int a[]={1,2,3,4,5,6};
Scanner sc=new Scanner(System.in);

r1: System.out.println("Enter Number");
int x=sc.nextInt();
if(x<-1 || x>6)
System.out.println("Enter number between 0 and "+a.length);
else
{
int y=x;
int i=0, temp=0;
int first=a[0];
while(x>0)
{
temp=a[5];
//tmp=temp;
for(i=5;i>=0;i--)
{

if(i-1!=-1)
a[i]=a[i-1];
else
a[i]=temp;
}

x--;
}


System.out.println("Left Shifted by "+y+" times");
for(i=0;i<a.length;i++)
System.out.print(a[i]+" ");

System.out.println("");
}
}
}
