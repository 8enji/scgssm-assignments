import java.util.Scanner;
public class Test1
{
   public static void main(String [] args)
   {
     Scanner scan = new Scanner(System.in);
     double rwidth;
     double rlength;
     double rheight;
     double cradius;
     double cheight;
     double rvolume;
     double cvolume;
     
     System.out.println("Your goal is to input values of a rectangular prism and a cylinder so there volume is equal. Good luck!");
     System.out.println("Please input the width, length, and height of the rectangle respectively");
     rwidth = scan.nextDouble();
     rlength = scan.nextDouble();
     rheight = scan.nextDouble();
     
     
     System.out.println("Please input the radius and height of the cylinder respectively");
     cradius = scan.nextDouble();
     cheight = scan.nextDouble();
     
     rvolume = rwidth * rlength * rheight;
     cvolume = Math.pow(cradius,2) * Math.PI * cheight;
     System.out.println("The volume of the rectangle is " + rvolume);
     System.out.println("The volume of the cylinder is " + cvolume);
     
     if (cvolume == rvolume )
     System.out.println("You are the winner!");
     else {
     if (cvolume >= rvolume)
     System.out.println("Cylinder is bigger");
     else {
     System.out.println("Rectangle is bigger");
     
     }
     }
     
     }
     }
     
   
    
    
    
    
    
    
    
    
     
     