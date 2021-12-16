public class ConcatenateThis
{
   public static void main(String [] args)
   {
      String name;
      name = "lady";
      String insect = "bug";
      
      System.out.println("Here is a " + name + insect);
      
      System.out.println(insect + " meet " + name);
      
      int numberOfBugs = 12;
      
      name = name + insect;
      
      System.out.println( numberOfBugs + " " + name + "s are in my garden");
      
      
   }
   
}