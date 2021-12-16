
public class BookListing {

   private int price;
   private Book book;
   
   public BookListing(Book b, int p) {
   price = p;
   book = b;
   }
   
   
   public void printBookInfo() {
      book.printBookInfo();
      System.out.println(", $" + price);
      }
      
      
}