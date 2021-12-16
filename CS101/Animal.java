abstract public class Animal {

	private String category;
	private double age;
	private double mass;
	
	public Animal(String type, double yrsold, double size){
		category = type;
		age = yrsold;
		mass = size;
	}
	
	abstract  public boolean isAdult();
	
	public String getCategory(){
		return category;
	}
	public double getAge() {
		return age;
	}
	public double getWeight(){
		return mass;
	}
	public void addAge(){
		age++;
	}
	public void grow (){
		mass = mass * 1.1;
	}
	public String toString(){
		return category + " "+ age + " years old, weight "+ mass;
	}
}
