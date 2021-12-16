public class TestProduct
{
   public static void main(String [] args)
   {
      Product myMoney = new Product(400.0);
      double currentAmt = myMoney.getBalance();
      System.out.println("Balance in bank: " + currentAmt);
      
      myMoney.deposit(550.0);
      currentAmt = myMoney.getBalance();
      System.out.println("Balance in bank now: " + currentAmt);
      
      myMoney.withdraw(200.0);
      System.out.println(myMoney.getBalance());
      
   }
   
}