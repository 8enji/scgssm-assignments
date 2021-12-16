import java.util.Scanner;

public class FermatTheory
{
   public static void main (String [] args)
   {
   Scanner scan = new Scanner(System.in);
   int a;
   int b;
   int c;
   int n;
   
   System.out.println("Please enter a value for a.");
   a = scan.nextInt();
   
   System.out.println("Please enter a value for b.");
   b = scan.nextInt();
   
   System.out.println("Please enter a value for c.");
   c = scan.nextInt();
   
   System.out.println("Please enter a value for n.");
   n = scan.nextInt();
   
   if (n > 2 && Math.pow(a,n) + Math.pow(b,n) == Math.pow(c,n))
   System.out.println("Holy smokes, Fermat was wrong!");
   else
   System.out.println("No, that doesn't work.");
   
   }
   
}