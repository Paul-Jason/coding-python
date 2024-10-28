class LRUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
    
    def put(self, key, value):
        if key in self.cache:
            #update ll
            # if not only one node 
            if(self.head != self.tail):
                node = self.cache[key]
                prev = node.prev 
                next = node.next
                node.prev = None
                node.next = None
                prev.next = next
                if next != None: 
                    next.prev = prev
                node.next = self.head
                self.head.prev = node
                self.head = node   
                print("cache", self.cache)
                self.printLL()         
        else:   
            if len(self.cache) == self.capacity:
                #remove tail from ll
                prev = self.tail.prev
                prev.next = None
                self.tail = prev
                #remove the item from cache 
                del self.cache[key]
                #add this new node to head 
                node = Node(key, value)
                node.next = self.head
                self.head.prev = node
                self.head = node
                #add this item to cache
                self.cache[key] = node
            else:
                #add to cache 
                node = Node(key, value)
                self.cache[key] = node
                #add to head of ll
                if self.head is not None:
                    node.next = self.head
                    self.head.prev = node
                    self.head = node
                else :
                    pass

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            prev = node.prev 
            next = node.next
            node.prev = None
            node.next = None
            prev.next = next
            if next != None: 
                next.prev = prev
            node.next = self.head
            self.head.prev = node
            self.head = node
            return node.val
        else: 
            return -1

    def printLL(self):
        node = self.head
        while(node is not None):
            print(node.key)
            node = node.next

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        pass

cache = LRUCache(2)
print(cache.put(1,1))
print(cache.put(2,2))
print(cache.get(1))
print(cache.put(3,3))
print(cache.get(2))
print(cache.put(4,4))
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))