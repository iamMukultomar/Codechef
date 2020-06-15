/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner scan=new Scanner(System.in);
		int t=scan.nextInt();
		for(int i=0;i<t;i++){
		    long n=scan.nextLong();
		    
		    
		if(n%2==1)
		   System.out.println((n-1)/2);
		   else if((n&n-1)==0)
		   System.out.println("0");
		else{
		    while(n%2==0){
		        n=n/2;
		    }
		    System.out.println((n-1)/2);
		}
		}
	}
}