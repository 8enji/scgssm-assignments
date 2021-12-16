import java.util.Random;
import java.util.Scanner;

public class ExampleSwitch {
   public static void main(String [] args)
   {
      Random generator = new Random();
      String dayOfWeek = null;
      int day = generator.nextInt(7) + 1; // day from 1 to 7
      
      switch(day)
      {
         case 1: dayOfWeek ="Sunday";
         break;
         
         case 2: dayOfWeek = "Monday";
         break;
         
         case 3: dayOfWeek = "Tuesday";
         break;
         
         case 4: dayOfWeek = "Wednesday";
         break;
         
         case 5: dayOfWeek = "Thursday";
         break;
         
         case 6: dayOfWeek = "Friday";
         break;
         
         case 7: dayOfWeek = "Saturday";
         break;
         
         }
         
         System.out.println(dayOfWeek);
         
         int ptva; = generator.nextInt(10) + 1;
         Card sam = new Card("Prince","Clubs", ptval);
         
       }
      }