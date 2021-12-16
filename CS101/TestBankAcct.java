public class TestBankAcct
{
   public static void main(String [] args)
   {
      BankAccount myMoney = new BankAccount(400.0);
      double currentAmt = myMoney.getBalance();
      System.out.println("Balance in bank: " + currentAmt);
      
      myMoney.deposit(550.0);
      currentAmt = myMoney.getBalance();
      System.out.println("Balance in bank now: " + currentAmt);
      
      myMoney.withdraw(200.0);
      System.out.println(myMoney.getBalance());

      BankAccount BenAccount = new BankAccount(0.0);
      BenAccount.deposit(550.0);
      System.out.println("Ben has " + BenAccount.getBalance());
      if (BenAccount.getBalance () < 1000.0)
         BenAccount.deposit(100.0);
      System.out.println("Ben has " + BenAccount.getBalance());
      
   }
   
}