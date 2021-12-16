public class array
{
public static void main(String [] args)
{    
   double [] data = new double[10];

   
   int i = 0;
   while (i<data.length)
   {
   data[i] = i;
   i++;
   }
   System.out.println(data[5]);
   System.out.println(data[8]);

   display(data);
   reverse(data);
   System.out.println();
   display(data);
}

// public static void display(double [] data)
// {
//    for(int i = 0; i < data.length; i++)
//    System.out.print(data[i] + " ");
// 
// }

public static void display(double [] data)
{
   for(double e : data)
   System.out.print((e) + " ");
}

public static void reverse(double [] data)
{
   int i = 0;
   int j = 9;
   double x = 0;
   while(i < data.length/2)
   {
   x = data[i];
   data[i] = data[j];
   data[j] = x;
   
   i++;
   j--;
   
   }
   

}

}