public class AnimalAP {
   
   private String type;
   private String species;
   private String name;
   
   public AnimalAP(String t, String s, String n){
      type = t;
      species = s;
      name = n;
      }
      
   public String toString()
   {
      String string = name + " the " + species + " is a " + type;
      return string;
   }
   
}
   
   