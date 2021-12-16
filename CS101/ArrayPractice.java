import java.util.ArrayList;
public class ArrayPractice
{
   public static void main(String [] args)
   {
      ArrayList<String> colors = new ArrayList<String>();
      System.out.println(colors.size());
      colors.add("red");
      colors.add("green");
      colors.add("pink");
      colors.add("orange");
      int counter = 0;
      
      while (counter < colors.size()) {
         System.out.println(colors.get(counter));
         counter++;
      }
      System.out.println(colors.get(1) + " change to be blue");
      colors.set(1, "blue");
      System.out.println(colors);
      
      colors.remove(0);
      System.out.println(colors);
      
      colors.add("white");
      colors.add("violet");
      colors.add("yellow");
      System.out.println(colors);
      
      int k = 0;
      while (k < colors.size()){
         colors.remove(k);
         k ++;
      }
         
      System.out.println(colors);
      
      
      
   }
   
}