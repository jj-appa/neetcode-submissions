class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        #Create a prev and next "pointers" aka a doubly linked list
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        #Left = LRU , right = most recent or current
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    #simple removing node from linked list
    def remove(self, node):
        prevToDo, nextToDo = node.prev, node.next
        prevToDo.next, nextToDo.prev = nextToDo, prevToDo

    #inserting node into a linked list from all the way to the right
    def insert(self, node):
        prevToDo, nextToDo = self.right.prev, self.right
        prevToDo.next , nextToDo.prev = node, node
        node.next, node.prev = nextToDo, prevToDo
         

    def get(self, key: int) -> int:
        if key in self.cache:
            #sort the list
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #checks capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
