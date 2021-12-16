/* Code by Benjamin Charest 10/9/2020
   - Creates a type of food with a price
   - Will be able to get price, get type, change price, change type
*/

public class Food
{
   // instance variables - price and type
   private double price;
   private String type;
   
   
   // constructor
   public Food(double price, String type)
   {
      this.price = price;
      this.type = type;
   }
   // default constructor - sets price to 0 and type to null
   public Food()
   {
      price = 0;
      type = null;
   }
   
   // returns type of food
   public String getType() 
   {
      return type;
   }
   
   // returns price of food
   public double getPrice()
   {
      return price;
   }
   
   // changes the price of food
   public void changePrice(double priceChange)
   {
      price = price + priceChange;
   }
   
   // changes the type of food
   public void changeType(String type2)
   {
   type = type2;
   }
}