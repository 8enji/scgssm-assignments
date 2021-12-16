// Extends superclass
public class Apple extends Fruit{
	
   // Instance Variables
   private String variety;
   private String ripeColor;
   private double minAge;
   
   // Constructor
   public Apple (String type, String color, double daysold, double calories, String variety, String ripeColor, double minAge){
	   super(type, color, daysold, calories);
      this.variety = variety;
      this.ripeColor = ripeColor;
	   this.minAge = minAge;
   }
   
  // Completed abstract method
  public boolean isRipe(){
	 return (getAge() > minAge && getColor() == ripeColor );
  }
	
  // Methods
  public String toString(){ 
	 String message = super.toString();
	 message += "\nVariety: "+ variety  + "\nis " ;
	 if ( isRipe() ) 
		message += "ripe";
	 else
		message += "not ripe";
	 return message;
	}

}