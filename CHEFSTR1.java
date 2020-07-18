/* package codechef; // don't place packsage name! */

import java.util.*;
import java.lang.*;
import java.io.*;


class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner scan=new Scanner(System.in);
		int t=scan.nextInt();
		while(t--!=0){
		    int n=scan.nextInt();
		    int[] a=new int[n];
		    for(int i=0;i<n;i++){
		        a[i]=scan.nextInt();
		        }
		    long sum=0;      
		        for(int i=1;i<n;i++){
		            sum+=(Math.abs(a[i]-a[i-1])-1);
		            
		        }
		        System.out.println(sum);
		    
		}
	}
}
