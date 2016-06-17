class C1
{
static int a[]={9,8,10,4,3,2,1};
public static void main(String args[])
{


int res1=0,res2=0,res3=0;
int temp;
res1=a[0];
res2=a[1];
res3=a[2];





           for(int i=3;i<a.length;i++)
{
if(a[i]>res1)
{
a[i]=a[i]+res1;
res1=a[i]-res1;
a[i]=a[i]-res1;

}
else if(a[i]>res2)
{
a[i]=a[i]+res2;
res2=a[i]-res2;
a[i]=a[i]-res2;

}
else if(a[i]>res3)
{
a[i]=a[i]+res3;
res3=a[i]-res3;
a[i]=a[i]-res3;

}
}
System.out.println("The top 3 Maximum Elements");

System.out.println("  "+res1+" "+res2+" "+res3);
System.out.println("");

}





}
