import java.util.ArrayList;

public class PlayerTester
{
   public static void main(String [] args)
   {
      Card one = new Card("King", "Diamonds", 13);
      Card two = new Card("2", "Clubs",2);
      Card three = new Card("6", "Spades", 6);
      Card four = new Card("Jack", "Hearts", 11);
      Card five = new Card("9", "Diamonds", 9);
      Card six = new Card("4", "Spades", 4);
   
      ArrayList<Card> hand = new ArrayList<Card>();
      Player Winner = new Player("Winner", hand );
      System.out.println( Winner.getName());
      Winner.addCardToHand(one);
      System.out.println(Winner.displayHand());
      Winner.addCardToHand(two);
      System.out.println(Winner.displayHand());
      
      ArrayList<Card> SueHand = new ArrayList<Card>();
      Player SuperSue = new Player("Sue", SueHand);
      System.out.println( "\n" + SuperSue.getName());
      SuperSue.addCardToHand(three);
      System.out.println( SuperSue.displayHand());
      
      
      
      
      
    }
   
}