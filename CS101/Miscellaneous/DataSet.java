public class DataSet
{
   public static void main(String [] args){
      BankAccount myAcct = new BankAccount(250.0);
      Coin myCollection = new Coin(4.5, 1918, 100.0);
      
      
      Measureable x = myAcct;
      Measureable y = myCollection;
      
      
      double sum = 0;
      sum = x.getMeasure();
      sum += y.getMeasure();
      
      System.out.println(sum);
      
      }
      
}