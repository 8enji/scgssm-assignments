public class Fish extends Animal{
	
   private String variety;
   private double minAge;
   
   public Fish (String type, double yrsold, double size, String variety, double minAge){
	   super(type, yrsold, size);
	   this.minAge = minAge;
	   this.variety = variety;
   }
   
  public boolean isAdult(){
	 return (getAge() > minAge && getWeight() > 0.02 );
  }
	
  public String toString(){ 
	 String message = super.toString();
	 message += " Variety: "+ variety  + " is " ;
	 if ( isAdult() ) 
		message += "adult";
	 else
		message += "fry";
	 return message;
	}

}
