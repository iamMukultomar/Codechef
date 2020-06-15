/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner scan=new Scanner (System.in);
		int t =scan.nextInt();
		while(t--!=0){
		    int n=scan.nextInt();
		    
		    int b=0;
		    for(int i=0;i<n;i++){
		        
		        if(i%2==0){
		            for(int j=0;j<n;j++){
		                b++;
		                
		                System.out.print(b + " ");
		            }
		           }
		        
		        else{
		            for(int j=0;j<n;j++){
		                
		                
                        System.out.print((b+n) + " ");
		            
		                b--;
		            }
		            b=b+(2*n);
		           }
		        
		        System.out.println();
		        }
		} 
	}
}	
