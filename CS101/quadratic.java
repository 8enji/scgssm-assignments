import java.util.Scanner;
public class quadratic
{
   public static void main(String [] args)
   {
     Scanner scan = new Scanner(System.in);
     double a;
     double b;
     double c;
     double xa;
     double xb;
     
     System.out.println("Please input the value of a.");
     a = scan.nextDouble();
     
     System.out.println("Please input the value of b.");
     b = scan.nextDouble();
     
     System.out.println("Please input the value of c.");
     c = scan.nextDouble();
   
     if((Math.pow(b,2)) - (4*a*c) < 0)
    
     System.out.println("The discriminant is negative.");
     else 
     {
     if( 2*a == 0)
     System.out.println("The denominator is zero.");
     else {
     xa = (-b + Math.sqrt(Math.pow(b,2) - (4*a*c))) / (2*a);
     xb = (-b - Math.sqrt(Math.pow(b,2) - (4*a*c))) / (2*a);
     
     System.out.println("The two solutions for x are " + xa + " and " + xb + ".");
     
     }
     }
  
   
   }

}