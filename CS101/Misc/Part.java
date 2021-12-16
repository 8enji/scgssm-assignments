public class Part { 
   
   private String name;
   private int id;
   
   public Part(String name, int id) {
      this.name = name;
      this.id = id;
      }
      
   public String getName(){
		return name;
	}
   
   public int getId(){
		return id;
	}
   
   public String toString(){
      return "Part name: " + name + "\nPart id: " + id;
   
   
   }
      
}