//code by Benjamin Charest - 10/2/2020 - Purpose: Sell items

import java.util.Scanner;
public class AsSeenOnTV
{
   public static void main(String [] args)
   {
   double amount = 0;
   double cart = 0;
   String answer = ("a");
   Scanner myScan = new Scanner(System.in);
      
   Product robotSweeper = new Product("Robot Sweeper", 24.95);
   amount = robotSweeper.getPrice() * .15;
   System.out.println("The name of the product is " + robotSweeper.getName() + " and it's price is " + robotSweeper.getPrice() + ". Would you like to but it?");
   answer = myScan.nextLine();
   if (answer.equals("yes"))
   cart = cart + robotSweeper.getPrice();
   else
   {
   robotSweeper.reducePrice(amount);
   System.out.println("but wait,there's more its on sale today for $" + robotSweeper.getPrice() +"?");
   answer= myScan.nextLine();
   if (answer.equals("yes"))
   cart = cart + robotSweeper.getPrice();
      }
      

   Product sam = new Product("Samurai Pro", 14.99);
   amount = sam.getPrice() * .15;
   System.out.println("The name of the product is " + sam.getName() + " and it's price is " + sam.getPrice() + ". Would you like to but it?");
   answer = myScan.nextLine();
   if (answer.equals("yes"))
   cart = cart + sam.getPrice();
   else
   {
   sam.reducePrice(amount);
   System.out.println("but wait,there's more its on sale today for $" + sam.getPrice() +"?");
   answer= myScan.nextLine();
   if (answer.equals("yes"))
   cart = cart + sam.getPrice();
      }
      
      
   Product ronco = new Product("Ronco Veg-a-matic", 19.95);
   amount = ronco.getPrice() * .15;
   System.out.println("The name of the product is " + ronco.getName() + " and it's price is " + ronco.getPrice() + ". Would you like to but it?");
   answer = myScan.nextLine();
   if (answer.equals("yes"))
   cart = cart + ronco.getPrice();
   else
   {
   ronco.reducePrice(amount);
   System.out.println("but wait,there's more its on sale today for $" + ronco.getPrice() +"?");
   answer= myScan.nextLine();
   if (answer.equals("yes"))
   cart = cart + ronco.getPrice();
      }
      
   System.out.println("The total price for your cart is $" + cart);
   
 
   
   }
   
}
   