// Ben Charest
// I did this work myself

public class Bug
{

   private int position;
   private int direction;
   
   public Bug(int initialPosition, int initialDirection)
   {
   position = initialPosition;
   direction = initialDirection;
   }
   
   public Bug()
   {
   position = 0;
   direction = 1;
   }
   
   public void moveOne()
   {
   position = position + (1 * direction);
   }
   
   public void turnAround()
   {
   direction = direction * -1;
   }
   
   public int getPosition()
   {
   return position;
   }
   
   public int getDirection()
   {
   return direction;
   }
   
   public void setPosition(int p)
   {
   position = p;
   }
   
}
   