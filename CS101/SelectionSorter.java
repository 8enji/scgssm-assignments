/* Selection sorter starts with index 0 and looks for the smallest 
   value in the remainder of the list. If smallest is found, then
   swap that value with the one as index 0. Continue this procedure
   by using the next index as the start until all elements have been
   placed.
 */
public class SelectionSorter
{
   private int a[ ];   //instance variable to contain an array to be sorted

    /**  Construct a selection sorter.
      @param anArray the array to sort
      */
     public   SelectionSorter( int [] anArray)
     {
          a = anArray;
     }
    /** 
        Sorts the array managed by this selection sorter
    */
   public void sort() 
  { 
      for(int i = 0; i  < a.length - 1; i++)  // start at index 0
      {
          int minPos = minimumPosition(i);    // find the smallest value in remainder of list
                swap(minPos, i);                         // swap the smallest with the value at current top index
      }
  }

  // Finds the smallest value in the list from current position and returns it
  private int minimumPosition(int from)
  {
     int minPos= from;
     for(int i = from + 1; i < a.length; i++)
            if (a[i] < a[minPos] ) minPos = i;
     return minPos;
   }
   // swaps the element at i with the element at j
   private void swap(int i, int j)
   {
      int temp = a[i];
      a[i] = a[j];
      a[j] = temp;
   }
}