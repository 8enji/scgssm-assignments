
import java.util.Scanner;

public class TestRectangle
{
   public static void main(String [] args)
   {
      double height;
      double width;
      double perimeter;
      double area;
      double diagonal;
      
      Scanner scan = new Scanner(System.in);
      System.out.println("Enter height and width of a rectangle");
      height = scan.nextDouble();
      width = scan.nextDouble();
      
      perimeter = (height * 2) + (width * 2);
      area = height * width;
      diagonal = Math.sqrt(Math.pow(height, 2) + Math.pow(width, 2));
      
      
      System.out.println(" width is " + width + " and height is " + height);
      System.out.println(" perimeter is " + perimeter);
      System.out.println(" area is " + area);
      System.out.println(" diagonal is " + diagonal);
      }
      }