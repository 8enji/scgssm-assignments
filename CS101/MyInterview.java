// First inout excercise

import java.util.Scanner;

public class MyInterview
{
   public static void main(String [] args)
   {
   
      Scanner getIn = new Scanner(System.in);
      String name;
      System.out.print("What is your first name? ");
      name = getIn.next();
      System.out.println("Hello, " + name);
      
      System.out.print("What is your last name? ");
      String lastName;
      lastName = getIn.next();
      System.out.println( "Nice to meet you  " + lastName);   
      
      int age;
      System.out.print("How old are you, " + name);
      age = getIn.nextInt();
      System.out.println("You are " + age + " years old");
      
      double money;
      System.out.println("How much money do you earn per day?");
      money = getIn.nextDouble();
      System.out.println("You make " + money + " !! ");
      
      System.out.println("good bye");
   
   
   }
   
}