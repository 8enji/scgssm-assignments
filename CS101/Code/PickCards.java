// Author - Ben Charest
// I did not give or receive help on this assignment

import java.util.Random;
import java.util.Scanner;

public class PickCards {
   public static void main(String [] args)
   {
      Random generator = new Random();
      Scanner myScan = new Scanner(System.in);
      
      int ptval = 0;
      int ptval1 = generator.nextInt(10) + 1;
      int ptval2 = generator.nextInt(10) + 1;
      int ptval3 = generator.nextInt(10) + 1;
      int ptval4 = generator.nextInt(10) + 1; 
      
      
      
     
      
      String answer = null;
      
      Card Ben = new Card ("Queen", "Hearts", ptval1);
      Card Sam = new Card ("Prince", "Spades", ptval2);
      Card Joe = new Card ("King", "Clubs", ptval3);
      Card Mia = new Card ("Jack", "Diamonds", ptval4);
     
      System.out.println("The objective of the game is to get as close to 35 without going over 35.");
      System.out.println("Would you like to play the game?");
      answer = myScan.nextLine();
      
     
      while(answer.equalsIgnoreCase("yes"))
      {
         int whichCard = generator.nextInt(4) + 1;
         switch(whichCard)
         {
            case 1: ptval = ptval + Ben.pointValue();
               break;
            
            case 2: ptval = ptval + Sam.pointValue();
               break;
            
            case 3: ptval = ptval + Joe.pointValue();
               break;
            
            case 4: ptval = ptval + Mia.pointValue();
               break;
         }
      
         System.out.println("Your total points are " + ptval);
      
         if(ptval >= 35)
         {
            if(ptval > 35)
            {
               System.out.println("GAME OVER: Your points exceeded 35");
               answer = "no";
            }
            
            if(ptval == 35)
            {
               System.out.println("GAME OVER: You have won!");
               answer = "no";
            }
         }
         else{      
            System.out.println("Would you like to pick another card?");
            answer = myScan.nextLine();
            if(answer.equalsIgnoreCase("no"))
               System.out.println("Your total points are " + ptval);  
         }
      }
   
   }
         
}      
            
   
   
   
