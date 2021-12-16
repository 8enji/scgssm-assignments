
import java.util.Random;
// this is a utility class to manipulate arrays


public class ArrayUtil
{
   /*
    Creates an array of size length and randomly generates integers 
    with values from 0 to n - 1
   */
   private static Random generator = new Random();
   
   public static int[] randomIntArray(int length, int n)
   {
      int []a = new int[length];
      for (int i = 0; i < a.length; i++)
      {
         a[i] = generator.nextInt(n);
      }
      return a;
      }
      
   public static int[] ascendIntArray(int length, int n)
   {
      int []a = new int[length];
      for (int i = 0; i  < a.length; i++)
      {
         a[i] = i;
      }
      return a;
      
   }
   
   public static int[] descendIntArray(int length, int n)
   {
     int []a = new int[length];
     int top = a[length - 1];
     for (int i = a.length - 1; i >= 0; i--)
     {
      a[i] = top;
      top++;
      }
      return a;
   }
  }