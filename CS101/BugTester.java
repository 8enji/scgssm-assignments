// Ben Charest
// I did this work myself

import java.util.Scanner;
public class BugTester
{
   public static void main(String [] args)
   {
   Scanner myScan = new Scanner(System.in);

    int position = 0;
    int direction = 0;
    int counter = 0;
    int moveCount = 0;
    
    System.out.println("Input the position of the bug");
    position = myScan.nextInt();
    System.out.println("Input the position of the bug (-1 is left and 1 is right)");
    direction = myScan.nextInt();
    System.out.println("Input how many times you want to move the bug");
    moveCount = myScan.nextInt();
    
    Bug userBug = new Bug(position, direction); //User input bug
    
   while (counter < moveCount)
   {
   userBug.moveOne();
   counter = counter + 1;
    }
    
    System.out.println("The position of the bug is " + userBug.getPosition());
    System.out.println("The direction of the bug is " + userBug.getDirection() + " (-1 = left and 1 = right)");





   }
   
}