public class Cat extends Animal {

	private String breed;				  // example calico, persian, etc. 
	private int sleepDaily;     			  // avg is 12 – 16 hours per day

	public Cat (String type, double yrsold, double mass, String breed, int sleep ){
		super(type,  yrsold, mass);
		this.breed = breed;
		this.sleepDaily = sleep;
	}
	public boolean isAdult(){
		return (getWeight() >= 7.9 && getAge() >= 1.0);  
	}

	public boolean enoughSleep(){
		return (sleepDaily > 12);
	}

	public String toString(){
		String amt = "not enough sleep";
		if(enoughSleep()){
			amt= "enough sleep";
		} 
		String message = super.toString();
		message += " breed: "+ breed +  " gets " + amt + " is " ;
		if ( isAdult() ) 
			message += "adult";
		else
			message += "kitten";
		return message;
	}
}
