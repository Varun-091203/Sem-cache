import time 
import heapq

class Node:
    def __init__(self, key, value, expires_at=None):
        self.key = key
        self.value = value
        self.expires_at = expires_at
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity, clock=time.time):
        self.capacity = capacity
        self.map ={}
        self.heap = []
        self.clock = clock
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

    def put(self, key, value, ttl=None):
        self._purge_expired()
        expires_at = None
        if ttl is not None:
            expires_at = self.clock() + ttl
        if key in self.map:
            node = self.map[key]
            node.value = value
            node.expires_at = expires_at
            self._remove(node)
            self._add_to_front(node)
            if expires_at is not None:                        
                heapq.heappush(self.heap, (expires_at, key))  
            return
        node = Node(key, value, expires_at)
        self.map[key] = node
        self._add_to_front(node)
        if expires_at is not None:                            
            heapq.heappush(self.heap, (expires_at, key))      
        if len(self.map) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]


    def get(self, key):
        self._purge_expired()
        if key not in self.map:
            return None
        node =self.map[key]
        if node.expires_at is not None and self.clock() > node.expires_at:
            self._remove(node)
            del self.map[key]
            return None 
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def _purge_expired(self):
        now = self.clock()
        while self.heap and self.heap[0][0] < now:
            expires_at, key = heapq.heappop(self.heap)
            node = self.map.get(key)
            if node is None:
                continue
            if node.expires_at != expires_at:
                continue
            self._remove(node)
            del self.map[key]