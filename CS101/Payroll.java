public class Payroll
{
private int[] itemsSold; // number of items sold by each employee
private double[] wages; // wages to be computed in part (b)
 
public Payroll()
{

itemsSold = new int[] {48, 50, 37, 62, 38, 70, 55, 37, 64, 60};

wages = new double[10];
}
/** Returns the bonus threshold as described in part (a).
*/
public double computeBonusThreshold()
{
	int total = 0;
	int max = 0;
	int min = 10000000;
   double bonus = 0;
   
   for(int item : itemsSold) {
   total = total + item;
   
   if( item > max)
      max = item;
      
   if( item < min)
      min = item;
   }
   
   
   bonus = ((double)(total - min - max)) / ((double)(itemsSold.length - 2));
   
   return bonus;
}
 
/** Computes employee wages as described in part (b)
* and stores them in wages.
* The parameter fixedWage represents the fixed amount each employee
* is paid per day.
* The parameter perItemWage represents the amount each employee
* is paid per item sold.
*/
public void computeWages(double fixedWage, double perItemWage)
{

   for(int i = 0; i < itemsSold.length ; i++) {
      double wage = (itemsSold[i] * perItemWage) + fixedWage;
      
      if (itemsSold[i] > computeBonusThreshold()) 
         wage = wage * 1.1;
         
      wages[i] = wage;
   
   }
   
}

public void printWages()

{

for (int i = 0; i < wages.length ; i++)

{

System.out.printf("Employee =% d , ItemsSold = %d, Wage = %.2f\n",i,itemsSold[i], wages[i]);

}

}
 

}
