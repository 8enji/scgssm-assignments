import java.util.Arrays;
import java.util.Scanner;
import java.util.Random;

/* 
  Generates a list of integers using the ArrayUtil class
  and then calls the SelectionSorter to sort them. 
   Displays the values before and after they are sorted.
*/
public class SelectionSortDemo 
{
  public static void main(String [] args)
  {
     Scanner scan = new Scanner(System.in);
     Random generator= new Random();
     StopWatch timer = new StopWatch();
     
     System.out.println("How many elements?");
     int numElements = scan.nextInt();           // size of the array to be created
     System.out.println("Max range of element values?");   
     int maxRange = scan.nextInt();                // range of values for elements
     
     int[] a = ArrayUtil.randomIntArray(numElements, maxRange);
     //System.out.println("before sort" + Arrays.toString(a));
     
     SelectionSorter sorter = new SelectionSorter(a);
     timer.start();
     sorter.sort();
     timer.stop();
    // System.out.println("after sort: "+ Arrays.toString(a));
     System.out.println(timer.getElapsedTime());
     }
  }

