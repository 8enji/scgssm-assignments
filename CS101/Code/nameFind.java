/*
#TITLE:  ArrayList Practice
#AUTHOR:  Ben Charest
#CLASS: Advanced Computer Programmed
#DATE: 1/12/2021
#HONOR CODE: I did not give or recieve help on this assignemnt
#DESCRIPTION: In this code, I created an arraylist and learned how to sort through it to find/remove specific things. I used the contained method as well.
*/

import java.util.*;


public class nameFind
{
public static void main(String [] args)
   {    
   ArrayList<String> names = new ArrayList<String>();
   
   Scanner scan = new Scanner(System.in);
   String x = null;
   
   for(int n = 0; n<10; n++)
   {
   System.out.println("Enter a name to add to the list");
   x = scan.nextLine();
   names.add(x);
   }
   
   
   System.out.println("Enter the name you want to find and remove:");
   String targetName = scan.nextLine();
   
  
   System.out.println("name contained in list: " + find(names, targetName));
   
   
   
   removeAll(names, targetName);
   
   System.out.println(names);
   System.exit(0);
   }
   
   public static boolean find(ArrayList<String> names, String targetName)
   {
   if(names.contains(targetName))
   return true;
   else
   return false;
   }
   
  public static void removeAll(ArrayList<String> names, String targetName)
   {
   while(names.contains(targetName) == true)
      names.remove(targetName);
   
   
   }
   
}