import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

/**
 * cache capacity
 * cache
 *
 * cap - 4
 * A
 * A B
 * A B C
 * A B C D
 */

class LRUCache {

    Map<Integer, Node> cache;
    int capacity;
    Node head = null;
    Node tail = null;

    public LRUCache(int capacity) {
        this.cache = new HashMap<>(capacity);
        this.capacity = capacity;
    }

    public int get(int key) {
        if(cache.containsKey(key)){
            Node node = cache.get(key);
            Node prev = node.prev;
            prev.next = node.next;
            node.next.prev = prev;
            node.next = head;
            head.prev = node;
            head = node;
            return cache.get(key).val;
        } else return -1;
    }

    public void put(int key, int value) {
        if(cache.containsKey(key)){
            // update the ll
            Node node = cache.get(key);
            Node prev = node.prev;
            prev.next = node.next;
            node.next.prev = prev;
            node.next = head;
            head.prev = node;
            head = node;
        } else {
            if(cache.size() == capacity){
                // decide which to evict then evict & insert
                int keyToRemove = tail.key;
                tail = tail.prev;
                tail.next = null;
                cache.remove(keyToRemove);
                Node node = new Node(key, value);
                cache.put(key, node);
                node.next = head;
                head.prev = node;
                head = node;
            } else {
                // add to cache
                Node node = new Node(key, value);
                if(head == null){
                    head = node;
                    tail = node;
                } else {
                    head.prev = node;
                    node.next = head;
                    head = node;
                }
                cache.put(key, node);
            }
        }
    }
}

class Node{
    int key;
    int val;
    Node prev;
    Node next;
    Node(int key, int val){
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
