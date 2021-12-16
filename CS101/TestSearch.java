import java.util.Scanner;
import java.util.Arrays;

public class TestSearch
{
   public static void main(String [] args)
   {
   Scanner scan = new Scanner(System.in);
    
   int target = 0;
   String search = null;
   int outcome = 0;
   int[] a = ArrayUtil.randomIntArray(100, 100);
    
   System.out.println("What do you want to search for?");
   target = scan.nextInt();
   scan.nextLine();
   System.out.println("What search do you want to use (linear/binary)");
   search = scan.nextLine();
   

   
   
 
   
   if(search.equals("linear"))
   {
   System.out.println(Arrays.toString(a));
   outcome = linearSearch(target, a);
   System.out.println("Linear Search");
   }
   
   if(search.equals("binary"))
   {
   Arrays.sort(a);
   System.out.println(Arrays.toString(a));
   outcome = binarySearch(target, a);
   System.out.println("Binary Search");
   }
   if(outcome == -1)
   System.out.println("Target not found in array");
   else
   System.out.println("Target found at index: " + outcome);
   
   
   }
   
   public static int linearSearch (int target, int [ ] a )
   {
   
      for(int i = 0 ; i < a.length ; i++) 
      {
         if(a[i]  == target)
         {
            return i;
         }   
      }
   
         return -1;
      
   }
   
   public static int binarySearch (int target, int [ ] a )
   {
      int low = 0;
      int high = a.length - 1;
      while (low <= high)
       {
         int mid = (low + high) / 2;
         int diff = a[mid] - target;
       
         if ( a[mid] == target)
            return mid;
         else if (a[mid] < target )
             low = mid + 1;
         else
             high = mid - 1;         
       }
       return -1;
    } 
  
    private int[] a;
    
    
    
    
 }
 

   
   
   
