import java.util.ArrayList;
import java.util.Scanner;

public class DeckTester {
   public static void main(String [] args)
   {
      ArrayList<String> ranks= new ArrayList<String>();
      ranks.add("2");
      ranks.add("3");
      ranks.add("4");
      ranks.add("5"); 
      ranks.add("6");
      ranks.add("7");
      ranks.add("8");
      ranks.add("9");
      ranks.add("10");
      ranks.add("Jack");
      ranks.add("Queen");
      ranks.add("King");
      ranks.add("Ace");
      
   
    
      ArrayList<String> suits = new ArrayList<String>();
      suits.add("Clubs");
      suits.add("Diamonds");
      suits.add("Hearts");
      suits.add("Spades");
      
   
      
      
      ArrayList<Integer> values = new ArrayList<Integer>();
      values.add(2);
      values.add(3);
      values.add(4);
      values.add(5); 
      values.add(6);
      values.add(7);
      values.add(8);
      values.add(9);
      values.add(10);
      values.add(10);
      values.add(10);
      values.add(10);
      values.add(11);
      
   
      
      Deck mydeck = new Deck (ranks, suits, values);
     
      
      System.out.println(mydeck);
      
      mydeck.shuffle();
      System.out.println(mydeck);
     
   
  
   
//    // This is the game of 21 code
//     //  Scanner myScan = new Scanner(System.in);
//    
//    // create a playerHand and playPoints
//    // create a dealerHand and dealerPoints same idea as playerHand
//    
//       ArrayList<Card> playerHand = new ArrayList<Card> ();
//       int playerPoints = 0;
//    
//       ArrayList<Card> dealerHand = new ArrayList<Card> ();
//       int dealerPoints = 0;
//    
//    // Deal two cards to the player face up and two cards to the dealer, one face up
//    
//       Card card1 = mydeck.deal();
//       Card card2 = mydeck.deal();
//       Card card3 = mydeck.deal();
//       Card card4 = mydeck.deal();
// 
//       
//       int cardNumber = 5;
//    
//       playerHand.add(card1);
//       playerHand.add(card2);
//       playerPoints = playerPoints + card1.pointValue() + card2.pointValue();
//    
//       dealerHand.add(card3);
//       dealerHand.add(card4);
//       dealerPoints = dealerPoints + card3.pointValue() + card4.pointValue();
//    
//       System.out.println("Here are your cards " + playerHand);
//       System.out.println("Points: " + playerPoints);
//       System.out.println("Dealer's first card: " + dealerHand.get(0));
//    
//       if(playerPoints == 21) {
//       System.out.println("You Won!");
//       }
//       
//       else {
//       String answer = "yes";
//       System.out.println("Do you want a card?");
//       answer = myScan.nextLine();
//       
//       while(answer.equalsIgnoreCase("yes"))
//       {
//       switch(cardNumber)
//       {
//       case 5:
//       Card card5 = mydeck.deal();
//       playerHand.add(card5);
//       playerPoints = playerPoints + card5.pointValue();
//       break;
//       
//       case 6:
//       Card card6 = mydeck.deal();
//       playerHand.add(card6);
//       playerPoints = playerPoints + card6.pointValue();
//       break;
//       
//       case 7:
//       Card card7 = mydeck.deal();
//       playerHand.add(card7);
//       playerPoints = playerPoints + card7.pointValue();
//       break;
//       
//       case 8:
//       Card card8 = mydeck.deal();
//       playerHand.add(card8);
//       playerPoints = playerPoints + card8.pointValue();
//       break;
//       
//       case 9:
//       Card card9 = mydeck.deal();
//       playerHand.add(card9);
//       playerPoints = playerPoints + card9.pointValue();
//       break;
//       
//       }
//       
//       System.out.println("Here are your cards " + playerHand);
//       System.out.println("Points: " + playerPoints);
//     
//       if(playerPoints == 21) {
//       answer = "no";
//       System.out.println("You got 21! You win:)");
//       }
//       else {
//       if(playerPoints>21) {
//       System.out.println("You lost:(");
//       answer = "no";
//       }
//       if(playerPoints<21) {
//       System.out.println("Do you want another card?");
//       answer = myScan.nextLine();
//       }
//       }
//       cardNumber++;
//       }
//       }
//       int dcardNumber = 10;
//       
//       while (dealerPoints < 17)
//       {
//       switch(dcardNumber)
//       {
//       case 10:
//       Card card10 = mydeck.deal();
//       dealerHand.add(card10);
//       dealerPoints = dealerPoints + card10.pointValue();
//       break;
//       
//       case 11:
//       Card card11 = mydeck.deal();
//       dealerHand.add(card11);
//       dealerPoints = dealerPoints + card11.pointValue();
//       break;
//       
//       case 12:
//       Card card12 = mydeck.deal();
//       dealerHand.add(card12);
//       dealerPoints = dealerPoints + card12.pointValue();
//       break;
//       }
//       dcardNumber++;
//       }
//       
//       System.out.println("Dealer hand: " + dealerHand);
//       System.out.println("Dealer points: " + dealerPoints);
//       
//       if((playerPoints>dealerPoints && playerPoints <= 21) || (playerPoints <= 21 && dealerPoints > 21) || (playerPoints ==21)) 
//       System.out.println("Player wins!");
//       else
//       System.out.println("Dealer wins!");
//       
//    // while dealerPoints is < 17
//    
//    //deal another card and get its points added to dealerPoints
//    
//    
//    
   }
   
}