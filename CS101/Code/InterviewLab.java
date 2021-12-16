// Interview Lab - Ben Charest

import java.util.Scanner;

public class InterviewLab
{
   public static void main(String [] args)
   {
      
      Scanner myScan = new Scanner(System.in);
      String name;
      System.out.print("What is your first name? ");
      name = myScan.next();
      
     
      int familyMembers;
      System.out.print("How many people are in your family? ");
      familyMembers = myScan.nextInt();

   
    
      double grade;
      System.out.println("What is your grade in AP Comp Sci?");
      grade = myScan.nextDouble();
      
      
      System.out.println("Hey " + name + "! You have " + familyMembers + " people in your family, and your grade in AP Comp Sci is a " + grade + ".");

      System.out.println("Cya later!");
      
   }
     
}

