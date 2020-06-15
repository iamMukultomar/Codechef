import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Main
{
	public static void main (String[] args) throws java.lang.Exception{
	    Scanner sc=new Scanner(System.in);
	    int t=sc.nextInt();
	    while(t--!=0){
	        int[] coi=new int[3];
	        int i=0;
	        Arrays.fill(coi,0);
	        int n=sc.nextInt();
	        int[] ar=new int[n];
	        for(i=0;i<n;i++){
	            ar[i]=sc.nextInt();
	        }
	        if(ar[0]>5) System.out.println("NO");
	        else{
	            coi[0]+=1;
	            for(i=1;i<n;i++){
	                if(ar[i]==5) coi[0]+=1;
	                else if(ar[i]>5){
	                    if(ar[i]==10){
	                        if(coi[0]==0) break;
	                        else{coi[0]-=1;coi[1]+=1;}
	                        }
	                        else{
	                            if(coi[1]!=0 || coi[0]>=2){
	                                if(coi[1]>=1) coi[1]-=1;
	                                else coi[0]-=2;
	                                 }
	                                 else break;
	                }
	            }
	        }
	          if(i==n)System.out.println("YES");
	          else System.out.println("NO");
	            
	        }
	}
	}
}