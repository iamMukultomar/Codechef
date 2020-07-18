import java.util.*;
import java.lang.*;
import java.io.*;


class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes herea
      Scanner scan=new Scanner(System.in);
      int t=scan.nextInt();
      while(t--!=0){
              int n=scan.nextInt();
              int a=0;
              int b=0;
              

              for(int i=0;i<n;i++){
                  
                  int sum=0,remainder=0;
                  int sum1=0,remainder1=0;
                  int c=scan.nextInt();
                  int d=scan.nextInt();
                  while (c != 0) { remainder = c % 10; sum = sum + remainder; c = c / 10; }
                  while (d != 0) { remainder1 = d % 10; sum1 = sum1 + remainder1; d = d / 10; }
              

            if(sum>sum1) a++;
            else if(sum==sum1) {a++; b++;}
            else b++;
 }
 if(a>b) {System.out.print(0+" "); System.out.println(a);}
 else if(a==b) {System.out.print(2+" "); System.out.println(a);}
 else {System.out.print(1+" "); System.out.println(b);}
}
}
}
