class C
{
static int a[]={10,9,8,4,2,1};
public static void main(String args[])
{


int res1=0,res2=0,res3=0;
int temp;
res1=a[0];

           for(int i=0;i<a.length;i++)
        {
            if(res1<a[i])
        {
           temp=a[i];
           a[i]=res1;
           res1=temp;
        }
        }


res2=find_next(res1);
res3=find_next(res2);


System.out.println("The top 3 Maximum Elements");

System.out.println("  "+res1+" "+res2+" "+res3);
System.out.println("");

}



static int find_next(int x)
{
int temp=x;
int tmp=a[0];


for(int i=0;i<a.length;i++)
if(tmp<a[i] && temp!=a[i])
{
tmp=a[i]+tmp;
a[i]=tmp-a[i];
tmp=tmp-a[i];
}

return tmp;
}
}
