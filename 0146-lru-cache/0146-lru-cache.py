class Node():
    def __init__(self,key,value) -> None:
        self.key, self.value = key, value
         
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity #given limit
        # it's better to have two links both sides of the node
        # so that it's easy to access
        self.left = Node(0,0) 
        self.right = Node(0,0)

        #to store the key and value relationship
        self.cache = {}

        #at first the left and right nodes should be connected this way
        self.left.next =self.right
        self.right.prev = self.left
    

    #add two helper functions so that to easily add and remove the nodes
    def remove(self,node):
        prevv, nextt = node.prev , node.next
        prevv.next , nextt.prev = nextt , prevv
    
    def insert(self,node):
        prev , next = self.right.prev, self.right
        prev.next = node
        next.prev = node
        node.prev , node.next = prev , next



    #now we can easily operate the following

    def get(self, key: int) -> int:
        #if the key is already there
        #we need to put it at the other end of the linked list - most recently use
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        #otherwise -1
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])  #if it's there, remove it and add it again 

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:  #check the limit 
            least_recently_used = self.left.next    #now remove this
            self.remove(least_recently_used)
            del self.cache[least_recently_used.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)