class HashTable:
    """Implement a hashtable using two list."""

    def __init__(self):
        self.size = 21  # The size of the hash table
        self.slots = [None] * self.size  # The number of slots in the table
        # should correspond to the size of the table. This list hold the keys.
        self.values = [None] * self.size  # A parallel list that holds the
        # values for values

    def insert(self, key, data):
        hash_code = self.hash_function(key, len(self.slots))

        if self.slots[hash_code] is None:
            self.slots[hash_code] = key
            self.values[hash_code] = data

        elif self.slots[hash_code] == key:
            self.values[hash_code] = data  # replace

        else:
            next_slot = self.rehash(hash_code, len(self.slots))
            while self.slots[next_slot] is not None and self.slots[next_slot] is not key:
                next_slot = self.rehash(next_slot, len(self.slots))

            if self.slots[next_slot] is None:
                self.slots[next_slot] = key
                self.values[next_slot] = data
            else:
                self.values[next_slot] = data

    def hash_function(self, key, size):
        if type(key) is int:
            return key % size
        elif type(key) is str:
            ordinal_sum = 0
            for char in key:
                ordinal_sum = ordinal_sum + ord(char)
            return ordinal_sum % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.values[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.insert(key, data)


dic = HashTable()
dic[54] = "cat"
dic[25] = "dog"
dic[11] = "parrot"
dic["cart"] = "carrot"
print(dic.slots)
print(dic.values)
