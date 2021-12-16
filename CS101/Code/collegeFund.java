public class collegeFund
{
   public static void main(String [] args)
   {
      SavingsAccount college = new SavingsAccount(10);
      
      college.deposit(1000);
      college.addInterest();
      
      System.out.println("Savings balance after one year with 10% return rate: " + college.getBalance());
      
      college.addInterest();
      
      System.out.println("Savings balance after two years with 10% return rate: " + college.getBalance());
      
      college.addInterest();
      
      System.out.println("Savings balance after three years with 10% return rate: " + college.getBalance());

      
  }
  
}