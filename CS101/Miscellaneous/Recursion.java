import java.util.*;


public class Recursion {

public int recur(int n)
{
if (n<=10)
return n * 2;
else
return recur(recur(n / 3));
}

public void run(){

System.out.println(recur(27));

}
}