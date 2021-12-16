import java.util.ArrayList;
import java.util.Scanner;

/*
 * Make some suits and ranks with matching point values to use to make a deck of cards
 */
public class CardGenerator {

   public static void main (String [] args) {
      Scanner scan = new Scanner(System.in);
     
      // Make array list of suits
      ArrayList<String> suits = new ArrayList<String>();
      System.out.print ("Enter the number of the suit to be used ");
      int suitCnt = scan.nextInt();
      for (int s= 0; s < suitCnt; s++) {
         System.out.println("Enter the suit name ");
         String name = scan.next();
         suits.add(name);
      }
      System.out.println("Your suits are " + suits + " \n " );
      
      // Mkae array list of ranks
      ArrayList<String> ranks = new ArrayList<String>();
      System.out.print ("Enter the number of the ranks to be used ");
      int rankCnt = scan.nextInt();
      for (int r= 0; r < rankCnt; r++) {
         System.out.print ("Enter the rank name: ");
         String name = scan.next()
         ranks.add(name);
      }
      System.out.println("Your ranks are " + ranks + " \n " );
   
   // Make array list of pointValues for each rank 
      ArrayList<Integer> points = new ArrayList<Integer>();
      System.out.println("Enter the number of the points to be created: ");
      int pointCnt = scan.nextInt();
      for (int p= 0; p < pointCnt; p++) {
         System.out.print ("Enter the point value for rank of " 
            + ranks.get(p) + " : ");
         Integer pt = scan.nextInt();
         points.add(pt);
      }
      System.out.println("Your points are " + points +  " \n " );
   
   }
   
}