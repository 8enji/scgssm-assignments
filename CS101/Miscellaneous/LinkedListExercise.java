/**

 * Downsize and Reverse methods applied to LinkedList of staff

 * @Ben Charest

 *

 */

import java.util.LinkedList;
import java.util.Scanner;
import java.util.ListIterator;

public class  LinkedListExercise {

      public static void main(String[] args) {
            LinkedList<String> staff;
           staff = new LinkedList<String>();
           //ListIterator<String> iterator = staff.listIterator();
           Scanner scan = new Scanner(System.in);
           System.out.println("Enter person's name or quit to stop");
          String name =  scan.next();
           while(!name.equalsIgnoreCase("quit")){
                      staff.add(name);
                      System.out.println("Enter person's name or quit to stop");
                      name = scan.next();
            }

           System.out.println(staff);
           downsize(staff);
           rehire(staff);
           System.out.println(staff);
//            System.out.println(staff);
//           reverse(staff);
//           System.out.println(staff);

        }

        /**
         * downsize
         */

        public static void downsize(LinkedList<String> staff) {
        
        ListIterator<String> iterator = staff.listIterator();
        iterator = staff.listIterator();
        iterator.next();
        while(iterator.hasNext())
        {
         iterator.next();
         iterator.remove();
         if(iterator.hasNext())
         iterator.next();
         
         }

          } 

        public static void rehire(LinkedList<String> staff) {
         
        ListIterator<String> iterator = staff.listIterator();
        iterator = staff.listIterator();
        iterator.next();
        iterator.add("Kelly");
        iterator.next();
        iterator.add("Sara");
        iterator.next();
        iterator.add("Zena");

      }

       /**
          * reverse
         */

         public static void reverse(LinkedList<String> staff) {
         int size = staff.size();
         ListIterator<String> iterator = staff.listIterator();

         LinkedList<String> staffReversed = new LinkedList<String>();
         while (iterator.hasNext())
            staffReversed.addFirst(iterator.next());

         staff.clear();

         for (int i = 0; i <= size-1; i++) {
            staff.add(staffReversed.get(i));
        }
    }
                
}