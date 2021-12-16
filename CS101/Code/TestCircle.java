import java.util.Scanner;

public class TestCircle
{
   public static void main(String [] args)
   {
      double radius;
      double area;
      double circumference;
      double volume;
      double surface;
   
      
      
      
      Scanner scan = new Scanner(System.in);
      System.out.println("Enter radius of a circle");
      radius = scan.nextDouble();
   
      
      area = Math.pow(radius, 2) * Math.PI;
      circumference = radius * Math.PI;
      volume = (4.0/3.0)* Math.PI * Math.pow(radius, 3);
      surface = 4.0 * Math.PI * Math.pow(radius, 2);
      
      
      System.out.println(" radius is " + radius  );
      System.out.println(" circmference is " + circumference);
      System.out.println(" area is " + area);
      System.out.println(" volume is " + volume);
      System.out.println(" surface area is " + surface);
      }
      }
      
   