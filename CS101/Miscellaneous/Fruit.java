// Superclass
abstract public class Fruit {

   // Instance variables
	private String type;
   private String color;
	private double age;
   private double calories;
	
   // Constructor
	public Fruit(String type, String color, double daysold, double calories){
		this.type = type;
      this.color = color;
		age = daysold;
		this.calories = calories;
	}
   
   // Abstract method
   abstract  public boolean isRipe();
	
   // Methods
	public String getType(){
		return type;
	}
   public Double getCalories(){
		return calories;
	}
   public String getColor(){
		return color;
	}
   public void addAge(){
		age++;
	}
	public double getAge() {
		return age;
	}
	public void addSugar (){
		calories = calories + 100;
	}
   public String toString(){
		return color + " " + type + "\n"+ age + " days old\n" + calories + " calories" ;
	}

   
}