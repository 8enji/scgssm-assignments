import java.util.ArrayList;

public class Inventory {

   Part test1 = new Part("test1", 123);
   ArrayList<Part> partsList = new ArrayList<Part>();
   
   public boolean addParts(Part part, int quantity)  {
      boolean inStock = false;
      for (Part partn : partsList) {
         if (partn.getId() == part.getId())
            inStock = true;
         
         }
      if (inStock) {
         for (int i = 0; i < quantity; i++)
            partsList.add(part);

      }
         
         
         
      return inStock;
   }
   
   
   
   
   
   
}