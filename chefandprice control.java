/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner scan=new Scanner(System.in);
		int t=scan.nextInt();
		for(int i=0;i<t;i++){
		    int n=scan.nextInt();
		    int k=scan.nextInt();
		    int sum=0;
		    for(int j=0;j<n;j++){
		        int price=scan.nextInt();
		        if(price>k)
		      sum+=price-k;
		        }
		        System.out.println(sum);
		        
		}
	}
}
