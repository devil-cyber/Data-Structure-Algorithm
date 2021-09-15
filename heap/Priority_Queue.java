import java.util.Collection;
import java.util.Collections;
import java.util.PriorityQueue;

class Priority_Queue{
    public static void main(String args[]){
        // priority Queue by deafault implement min heap
        // For max heap write Collections.reverseOrder
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        pq.add(10);
        pq.add(20);
        pq.add(15);

        System.out.println(pq.peek());
        System.out.println(pq.poll());
        System.out.println(pq.peek());
    }
}