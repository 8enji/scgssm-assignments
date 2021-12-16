// Convert celcius to fahrenheit assignment - 9/14/2020


import java.util.Scanner;

public class ConvertCtoF
{
   public static void main(String [] args)
   {
   Scanner myScan = new Scanner(System.in);
   double celcius;
   System.out.println("Please input any Celcius temperature below to convert it to Fahrenheit.");
   celcius = myScan.nextDouble();
   double fahrenheit;
   fahrenheit = celcius * 9 / 5 + 32;
   System.out.println("Celcius = " + celcius);
   System.out.println("Fahrenheit = " + fahrenheit);
   
   }
   
}