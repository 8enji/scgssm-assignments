//code by Benjamin Charest - 10/2/2020 - Purpose: Create product class

public class Product
{

   private double price;
   private String name;
   private double amount = price * .85;
   public Product(String n, double p)
   {
      name = n;
      price = p;
   }

   public String getName(){
      return name;
   }
   
   public double getPrice(){
      return price;
   }
   
   public void reducePrice(double amount)
   { price = price - amount;}

   public double price()
   { 
      return price; }

}
