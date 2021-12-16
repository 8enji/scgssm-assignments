public class NumberSystem
{
/** Precondition: a and b are positive integers.
* Returns the greatest common factor of a and b, as described in part (a).
*/
public static int gcf(int a, int b)
{ 
      if (b == 0)
         return a;
         
      else
         return gcf(b,a%b);

}
 
/** Precondition: numerator and denominator are positive integers.
* Reduces the fraction numerator / denominator
* and prints the result, as described in part (b).
*/
public static void reduceFraction(int numerator, int denominator)
{ 
   if (numerator % denominator == 0){
      numerator = numerator / denominator;
      denominator = 1;
      }
   else {
      int gcf = gcf(numerator, denominator);
      numerator = numerator / gcf;
      denominator = denominator / gcf;
      }
   if (denominator == 1)
   System.out.println(numerator);
   else
   System.out.println(numerator + "/" + denominator);

}
public static void main(String[] args) {
System.out.println(gcf(10, 25));
reduceFraction(30, 3);
}
}
