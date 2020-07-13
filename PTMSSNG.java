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
		while(t--!=0){
		    int n=scan.nextInt();
		    
		    int r=4*n-1;
		    int[] a=new int[r];
		    int[] b=new int[r];
		    for(int i=0;i<r;i++){
		        a[i]=scan.nextInt();
		        b[i]=scan.nextInt();
		    }
		     
    int res=0;
    int res1=0;
		     for (int i = 0; i < r; i++) { 
                res=res^a[i];
               
                
		     }
		     System.out.print(res+" ");
		     
		     for (int i = 0; i < r; i++) { 
                res1=res1^b[i];
                
                
		     }
		     System.out.println(res1);
		     
		}
	    
	}
}