// Code by Benjamin Charest - 10/12/2020 - I did this code myself
// expectations - I want this code to be able to create new instances of the food class and to be able able to use all of its methods with issues
public class foodTester
{
   public static void main(String [] args)
   {
   
   // constructor 1 testing
   
   // creates new food with specified parameters
   Food burger = new Food(4.99, "burger");
   
   // prints the type of food and price assigned by constructor
   System.out.println("The type of food is a/an " + burger.getType() + " and it's price is $" + burger.getPrice() ); 
  
   // changes the price of the burger to price + (-2)
   burger.changePrice(-2);
   
   // prints new price of burger
   System.out.println("After the discount, the " + burger.getType() + " is now $" + burger.getPrice());
  
   // changes type of food to "burger w/o tomatoes"
   burger.changeType("burger w/o tomatoes");
   
   // prints out new type of food with new price
   System.out.println("Your final order is a " + burger.getType() + " for $" + burger.getPrice());
   
   
   // constructor 2 testing
   
   // creates new food with default instance variables
   Food test2 = new Food();
   
   // prints the type of food and price assigned by constructor
   System.out.println("The type of food is a/an " + test2.getType() + " and it's price is $" + test2.getPrice() );
   
   // changes type of food to "pizza"
   test2.changeType("pizza");
   
   // prints out new type of food
   System.out.println("The type of food is a/an " + test2.getType() );
   
   // changes price of food to price + 10.99
   test2.changePrice(10.99);
   
   // prints out new type of food with new price
   System.out.println("The type of food is a/an " + test2.getType() + " and it's price is $" + test2.getPrice() );
   }
   
}