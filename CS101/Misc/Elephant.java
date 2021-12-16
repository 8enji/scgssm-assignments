public class Elephant extends Herbivore {
   
   private int tuskLength;
   
   public Elephant(String n, int tl) {
      super("elephant", n);
      tuskLength = tl;
      }
      
   public String toString()
   {
      String string = super.toString() + " with tusks " + tuskLength + " meters long.";
      return string;
   }
      
      
      
}