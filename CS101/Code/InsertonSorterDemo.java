import java.util.Arrays;
import java.util.Scanner;
import java.util.Random;

/* 
  Generates a list of integers using the ArrayUtil class
  and then calls the SelectionSorter to sort them. 
   Displays the values before and after they are sorted.
*/
public class InsertonSorterDemo 
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
     System.out.println("Enter 1 random, 2 ascned, descend");
     int dataOrder = scan.nextInt();
     int[] a = null;
     
     if (dataOrder == 1)
     {
      a = ArrayUtil.randomIntArray(numElements, maxRange);
     }
     
     if (dataOrder == 2)
     {
      a = ArrayUtil.ascendIntArray(numElements, maxRange);
     }
     
     if (dataOrder == 3)
     {
      a = ArrayUtil.descendIntArray(numElements, maxRange);
     }
     
     //int[] a = ArrayUtil.randomIntArray(numElements, maxRange);
      System.out.println("before sort" + Arrays.toString(a));
     
     InsertionSorter sorter = new InsertionSorter(a);
     //SelectionSorter sorter = new SelectionSorter(a);
     
     timer.start();
     sorter.sort();
     //sorter.sorta();
     timer.stop();
     
       System.out.println("after sort: "+ Arrays.toString(a));
     System.out.println(timer.getElapsedTime());
     }
  }
