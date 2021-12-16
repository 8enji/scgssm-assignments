import java.util.Random;
import java.util.ArrayList;

/***  The Deck class represents a shuffled deck of cards.
*  It provides several operations including
*  initialize, shuffle, deal, and check if empty.*/

public class Deck {

/**
	 * cards contains all the cards in the deck.
	 */
   private ArrayList<Card> cards;
    /**
	 * size is the number of not-yet-dealt cards.
	 * Cards are dealt from the top (highest index) down.
	 * The next card to be dealt is at size - 1.
	 */
   private int size;


	/**
	 * Creates a new <code>Deck</code> instance.<BR>
	 * It pairs each element of ranks with each element of suits,
	 * and produces one of the corresponding card.
	 * @param ranks is an array containing all of the card ranks.
	 * @param suits is an array containing all of the card suits.
	 * @param values is an array containing all of the card point values.
	 */
    
   public Deck(ArrayList<String> ranks, ArrayList<String> suits, ArrayList<Integer> values)
   {
      cards = new ArrayList<Card>();
      for( int suitIndex = 0; suitIndex < suits.size(); suitIndex++)
      {
         String suit = suits.get(suitIndex);
         
         for( int index = 0; index < ranks.size(); index++)
         {
            String rank = ranks.get(index);
            int value = values.get(index);
            Card myCard = new Card(rank, suit, value);
            cards.add(myCard);
          } // end of inner loop to create 13 cards for each suit
          
       } // get next suit
      
       size = cards.size();
       
   }


	/**
	 * Determines if this deck is empty (no undealt cards).
	 * @return true if this deck is empty, false otherwise.
	 */
   public boolean isEmpty() 
   {
        return size == 0;
   }

	/**
	 * Accesses the number of undealt cards in this deck.
	 * @return the number of undealt cards in this deck.
	 */
   public int size() 
   {
   	 return size;
   }

	/**
	 * Randomly permute the given collection of cards
	 * and reset the size to represent the entire deck.
	 */

 public void shuffle() {  
   Random generator = new Random();     
   for (int top = size-1; top > 0; top--)
   {    
        int randIndex = generator.nextInt(top);           
        Card ranCard = cards.get(randIndex);           
        Card topCard = cards.get(top);
        cards.set(randIndex, topCard);          
        cards.set(top, ranCard);
      }
   }

	/**
	 * Deals a card from this deck.
	 * @return the card just dealt, or null if all the cards have been
	 *         previously dealt.
	 */
   public Card deal() 
   {
   	 Card x;
       if(!this.isEmpty())
         { 
            x = cards.get(size-1);
            size--;
         }
         else
         {
         return null;
         }
         return x;
   }

	/**
	 * Generates and returns a string representation of this deck.
	 * @return a string representation of this deck.
	 */
   @Override
   public String toString() {
      String rtn = "size = " + size + "\nUndealt cards: \n";
   
      for (int k = size - 1; k >= 0; k--) {
         rtn = rtn + cards.get(k);
         if (k != 0) {
            rtn = rtn + ", ";
         }
         if ((size - k) % 2 == 0) {
         	// Insert carriage returns so entire deck is visible on console.
            rtn = rtn + "\n";
         }
      }
   
      rtn = rtn + "\nDealt cards: \n";
      for (int k = cards.size() - 1; k >= size; k--) {
         rtn = rtn + cards.get(k);
         if (k != size) {
            rtn = rtn + ", ";
         }
         if ((k - cards.size()) % 2 == 0) {
         	// Insert carriage returns so entire deck is visible on console.
            rtn = rtn + "\n";
         }
      }
   
      rtn = rtn + "\n";
      return rtn;
   }
}
