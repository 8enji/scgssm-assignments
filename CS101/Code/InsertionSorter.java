import java.util.Arrays;

public class InsertionSorter
{
   private int a[ ];   //instance variable to contain an array to be sorted

    /**  Construct a selection sorter.
      @param anArray the array to sort
      */
     public   InsertionSorter( int [] anArray)
     {
          a = anArray;
     }
    /** 
        Sorts the array managed by this insertion sorter
    */
   public void sort() 
  { 
     int j = a.length;
     for (int i = 1; i < j; i++)
      {
         int current = a[i];
         int n = i - 1;
         
         while (n >= 0 && a[n] > current)
         {
            a[n + 1] = a[n];
            n = n - 1;
         }
         a[n + 1] = current;
      }
  }
  
  public void sorta()
  {
   Arrays.sort(a);
  }   
  }

