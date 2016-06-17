import java.lang.*;
import java.util.Scanner;
class A
{
public static void main(String ar[])
{
int a[]={1,2,3,4,5,6};
Scanner sc=new Scanner(System.in);

System.out.println("Enter Number");
int x=sc.nextInt();
int k=a.length-x;
int j=0;
for(int i=x;i<a.length+x;i++){
System.out.println(a[i%6]+"  "+i);
a[j++]=a[i%6];
}

}
}
