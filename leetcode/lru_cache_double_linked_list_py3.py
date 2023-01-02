class DLListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DLList:
    def __init__(self):
        self.head, self.tail = DLListNode(), DLListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def push_to_head(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    def promote_to_head(self, node):
        self.pop(node)
        self.push_to_head(node)

    def pop(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def pop_tail(self):
        node = self.pop(self.tail.prev)
        return node


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.len = 0

        self.nodes = DLList()

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        
        if node is None:
            return -1

        self.nodes.promote_to_head(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        # key is already in cache: upd the val + promote it to the dllist head
        if node is not None:
            node.value = value
            self.nodes.promote_to_head(node)
        # add new key-value to cache; put the key to the dllist head
        else:
            new_node = DLListNode(key, value)
            self.nodes.push_to_head(new_node)

            if self.len >= self.capacity:
                tail_node = self.nodes.pop_tail()
                del self.cache[tail_node.key]
                self.len -= 1

            self.cache[key] = new_node
            self.len += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)