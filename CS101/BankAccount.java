public class BankAccount {
   // instance variable
   private double balance;
   
   // contructor - create a new object
   public BankAccount (double initBalance)
   {
      this.balance = initBalance;
   }
   public BankAccount()
   {
      this.balance = 0.0;
   }
  // methods (ways to access and/or change bank account)
   
   public void deposit(double amount) {
      balance = balance + amount;
   }
   public void withdraw(double amount) {
      balance = balance - amount;
   }
   public double getBalance() {
      return balance;
   }
}
   
   