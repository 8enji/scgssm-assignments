import java.util.*;
/**
 * Models a queue which adds new elements to the rear
 * and removes them from the front using a linked list
 * @author Ben Charest
 * @param <E> element data type
 */
public class Queue<E> {
	
   private LinkedList<E> que;	// instance variable
  
   /** instantiates a que with no elements  */
   public Queue (){			

	que = new LinkedList<E>();

   }
   /** places element at the end of the queue */
   public void enqueue(E element) {

	
	que.addLast(element);

   }
  /** if the queue is not empty, removes and returns the first element
      Otherwise throws a no such element exception */
 
   public E dequeue(){
	
	if(que.size() > 0){
	    return que.removeFirst();
	}
	else{
	    throw new NoSuchElementException();
	}



   }
   /** if the que has no elements, returns true. Otherwise returns false */
   public boolean isEmpty(){
	
	return que.isEmpty();
    
   }
   /** debug method returns a string containing all values stored in the que */
   public String toString(){
	

 	return que.toString();
   }
   
}
