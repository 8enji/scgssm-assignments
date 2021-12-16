import java.util.Scanner;

public class GasEfficiency
{
   public static void main(String [] args)
   {
      
      Scanner scan = new Scanner(System.in);
      double gallons;
      double fueleff;
      double price;
      double cost;
      double far;
      
      System.out.println("Please input the gallons of gas in the tank.");
      gallons = scan.nextDouble();
      
      System.out.println("Please input the fuel efficiency of the car in miles per gallon.");
      fueleff = scan.nextDouble();
      
      System.out.println("Please input the price of gas per gallon.");
      price = scan.nextDouble();
      
      
      cost = 100 / fueleff * price;
      System.out.println("It will cost you " + cost + " dollars to drive 100 miles");
      
      far = (gallons - (100 / fueleff)) * fueleff;
      System.out.println("You can travel " + far + " more miles after 100 if you started with a full tank");
   }
    
}
