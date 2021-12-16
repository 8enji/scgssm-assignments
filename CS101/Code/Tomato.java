// Extends superclass
public class Tomato extends Fruit {

   // Instance variables
   private String variety;
   private String ripeColor;
   private double minAge;
   private double mushy;
   private boolean vegetable;
   
   // Constructor
   public Tomato (String type, String color, double daysold, double calories, String variety, String ripeColor, double minAge, double mushy, boolean vegetable){
	   super(type, color, daysold, calories);
      this.variety = variety;
      this.ripeColor = ripeColor;
	   this.minAge = minAge;
      this.mushy = mushy;
      this.vegetable = vegetable;
   }
   
  // Completed abstract method
  public boolean isRipe(){
	 return (getAge() > minAge && getColor() == ripeColor );
  }
  
  // Methods
  public boolean isMushy(){
    return mushy > 5;
  }
	
  public String toString(){ 
	 String message = super.toString();
	 message += "\nVariety: "+ variety  + "\nis " ;
	 if ( isRipe() ) 
		message += "ripe";
	 else
		message += "not ripe";
    if ( isMushy() )
      message += "\nbe careful, the tomato is mushy!";
    if ( vegetable )
      message += "\nthe tomato is a vegetable!";
    else
      message += "\nthe tomato is not a vegetable! It is a fruit!";
    
	 return message;
	}

}
