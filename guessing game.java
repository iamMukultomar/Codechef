import java.util.*;
import java.lang.*;
import java.io.*;

public class Main{
	public static void main (String[] args) throws java.lang.Exception
	{
          Scanner scan=new Scanner(System.in);
          
          int n=scan.nextInt();
          
          char a=' ';
          
          int min=1;
          int max=n;
          System.out.println(min);
          char t=scan.next().charAt(0);
          
          if(t=='E') a=t;
          else {
              System.out.println(max);
              char s=scan.next().charAt(0);
              
              if(s=='E') a=s;
              else {min+=1; max-=1;} 
          }
          
          
          
            while(a!='E'){
              int m=(int) ((Math.random() * (max - min)) + min);
              System.out.println(m);
              char b=scan.next().charAt(0);
              if(b=='E') {a='E'; break;}
              System.out.println(m+1);
              char c=scan.next().charAt(0);
              if(c=='E') {a='E'; break;}
              
              if(b==c){
                  if(b=='G') min=m;
                  else max=m;
                      }
                      
                       
          }
          
	} 
}