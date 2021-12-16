import java.util.Scanner;
import java.util.Random;

public class hiLoGame
{
   public static void main(String [] args)
   {
      Scanner scan = new Scanner(System.in);
      Random generator = new Random();
      int tries = 1;
      String answer = null;
      
      
      System.out.println("would you like to play the game?");
      answer = scan.nextLine();
      while (answer.equals("yes"))
      {
      int value = generator.nextInt(101);
      System.out.println(value);
      
      System.out.println("Guess a number from 1 to 100");
      int guess = scan.nextInt();
      
      while (guess != value) 
      {
      if (guess > value)
      {
      System.out.println("guess is too high");
      }
      
      if (guess < value)
      {
      System.out.println("guess is too low");
      }
      System.out.println("Guess again!");
      guess = scan.nextInt();
      tries = tries + 1;
      
     
      }
      
      System.out.println("you got it " + value + " in " + tries + " guesses"); 
            System.out.println("Would you like to play again?");
      answer = scan.nextLine();
      }
      
      
   
      
      
      
      
   }
  
  
}