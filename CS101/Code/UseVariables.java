public class UseVariables
{
   public static void main(String [] args)
   {
      int count;
      count = 0;
      
      int numberOfQuarters;
      numberOfQuarters = 5;    
      
      int numberOfDollars;
      numberOfDollars = 3;
      
      count = numberOfQuarters*25 + numberOfDollars*100;
      
      System.out.println(count + "pennies" );
      
      int dollars = count / 100;
      int cents = count%100;
      
      System.out.println("$" + dollars + "." + cents);
System.out.println(35 + 55  + " is the sum.");


   }
   
}