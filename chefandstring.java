/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner scan=new Scanner(System.in);
		int t=scan.nextInt();
	    for(int i=0;i<t;i++){
	    String s=scan.next();
		int pairs=0;
		    for(int j=0;j<s.length()-1;j++){
		        if(s.charAt(j)!=s.charAt(j+1)){
		            ++pairs;
		            ++j;
		        }
		        
		      
		    }
		    System.out.println(pairs);  
		}
		
	}
}