/**
 * This is a class that tests the Card class.
 * Author - Ben Charest and rest of cs101 class
 */
public class CardTester {

	/**
	 * The main method in this class checks the Card operations for consistency.
	 *	@param args is not used.
	 */
   public static void main(String[] args) 
   {
      Card mycard = new Card ( "Queen", "Hearts", 10);
      System.out.println(mycard.toString());
      System.out.println(mycard.rank());     
      System.out.println(mycard.suit());   
      System.out.println(mycard.pointValue());   
      
      Card yourcard = new Card ("2", "Clubs",2);
      System.out.println(yourcard.toString());
      System.out.println(yourcard.rank());     
      System.out.println(yourcard.suit());   
      System.out.println(yourcard.pointValue());  
      
      Card other = new Card("Queen","Hearts",10);
      System.out.println(other.toString());
      System.out.println(other.rank());     
      System.out.println(other.suit());   
      System.out.println(other.pointValue());  
     
     
     
      if (mycard.matches(other))
      {
         System.out.println("They are the same");
      }
      else
      {
         System.out.println("They don't match");
      }
      
                  
   }

}