// make a player class

import java.util.ArrayList;

public class Player
{
   //instance variables
   private String name;
   private ArrayList<Card> hand;
   
   //constructor
   public Player (String name, ArrayList<Card> hand)
   {
      this.name = name;
      this.hand = hand;
   }
   
   // methods
   public String getName()
   {  
      return this.name;
   }
   
   public void addCardToHand(Card oneCard)
   {
      hand.add(oneCard);
   }
   
   public ArrayList<Card> displayHand()
   {
      return hand;
   }

}