//import java.util.Arrays;

public class board
{
public static void main(String [] args)
{    
   final int ROWS = 3; 
   final int COLUMNS = 3; 
  String[][] board = new String[ROWS][COLUMNS]; 
  
 
  for (int i = 0; i < ROWS; i++) 
     for (int j = 0; j < COLUMNS; j++)   
        if (board[i][j] == null) 
        board[i][j] = "-";
        
        
  
  
  board[0][0] = "x";
  board[1][1] = "x";
  board[2][2] = "x";
  
    for (int i = 0; i < ROWS; i++) 
    {
    System.out.print("\n");
     for (int j = 0; j < COLUMNS; j++)  
        System.out.print(board[i][j]);
    }
  
//   System.out.print(board[0][0]);
//   System.out.print(board[0][1]);
//   System.out.println(board[0][2]);
//   
//   System.out.print(board[1][0]);
//   System.out.print(board[1][1]);
//   System.out.println(board[1][2]);
//   
//   System.out.print(board[2][0]);
   System.out.print(board[1][1]);
//   System.out.print(board[2][2]);
}

// public static void display(double [][] board)
// {
//    for(int i = 0; i < board[][].length; i++)
//    System.out.print(board[i][i] + " ");
// 
// }


}

