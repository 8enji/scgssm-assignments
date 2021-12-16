import java.util.Scanner;

public class WrapperString
{
   public static void main(String [] args)
   {
      Scanner scan = new Scanner(System.in);

      System.out.println("Enter birthday in form mm/dd/yyyy");
      String birthday = scan.nextLine();
      
      String year = birthday.substring(6,10);

      System.out.println("Enter the current date in mm/dd/yyyy");
      String currentDate = scan.nextLine();
         
      String currentYear = currentDate.substring(6,10);
      System.out.println("The current year is " + currentYear);
      System.out.println("Your birth year is " + year);
      
      int intcurrentYear = Integer.parseInt(currentYear);
      int intyear = Integer.parseInt(year);
      
      System.out.println("It has been " + (intcurrentYear - intyear) + " years since you were born"); 
   
   }
   
   

}