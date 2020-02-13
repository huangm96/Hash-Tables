# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

 
    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        pair = LinkedPair(key, value)

        if self.count == self.capacity:
            self.resize()

        index = self._hash_mod(key)
        print(index)
        if self.storage[index] is not None:
            currentNode = self.storage[index]
            while currentNode:
                if currentNode.key == key:
                    currentNode.value = value
                    break
                elif currentNode.next is None:
                    currentNode.next = pair
                    break
                currentNode = currentNode.next

        else: 
            self.storage[index] = pair

        self.count += 1


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            print("Warning: cannot find this key")
        else:
            result = "Cannot find the value for this key"
            currentNode = self.storage[index]
            if currentNode.key == key:
                self.storage[index]=currentNode.next

                result = "removed"
            else:
                while currentNode.next:
                    if currentNode.next.key == key:
                        currentNode.next = currentNode.next.next
                        result = "removed"
                        break
                    else:
                        currentNode = currentNode.next
            print(result)
                
                    

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            print("Warning! Cannot find the value")
        else:
            currentNode = self.storage[index]
            while currentNode:
                if currentNode.key == key:
                    return currentNode.value
                else:
                    currentNode = currentNode.next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        if self.count < self.capacity:
            return
        else:
            old_storage = self.storage
            self.capacity *= 2
            self.storage = [None] * self.capacity
            self.count =0
            for item in old_storage:
                currentNode = item
                while currentNode:
                    self.insert(currentNode.key, currentNode.value)
                    currentNode = currentNode.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    
    print("")
    print(ht.storage)
    for x in ht.storage:
        if x is not None:
            currentNode = x
            while currentNode:
                print(currentNode.value)
                currentNode=currentNode.next

    ht.remove("line_1")
    print(ht.storage)
    for x in ht.storage:
        if x is not None:
            currentNode = x
            while currentNode:
                print(currentNode.value)
                currentNode = currentNode.next


    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
