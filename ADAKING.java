/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes heread
		Scanner scan=new Scanner(System.in);
		int t=scan.nextInt();
		while(t--!=0){
		    int k=scan.nextInt();
		    char[][] a=new char[8][8];
		    int f=9;
		    for(int i=0;i<8;i++){
		        for(int j=0;j<8;j++){
		            if(k>0){
		                a[i][j]='.';
		                k--;
		            }
		            else if(f>0){
		                a[i][j]='X';
		                f--;
		            }
		            else{
		                a[i][j]='.';
		                 }
		        }
		    }
		    a[0][0]='O';
		      for(int i=0;i<8;i++){
		        for(int j=0;j<8;j++){
		            System.out.print(a[i][j]);
		        }
		          System.out.println();
		      }
		    
		    
		}
	}
}
