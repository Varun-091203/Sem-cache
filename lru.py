class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None 

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map ={}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_front(self, node):
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def _remove(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return
        node = Node(key, value)
        self.map[key] = node
        self._add_to_front(node)
        if len(self.map) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]


    def get(self, key):
        if key not in self.map:
            return None
        node =self.map[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value