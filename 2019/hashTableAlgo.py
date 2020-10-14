class hashTableAlgo:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_bucket()

    def create_bucket(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        found = False
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        for index, record in enumerate(bucket):
            recordkey, recordvalue = record
            if recordkey == key:
                found = True
                break;
        if found:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        found = False
        bucket = self.hash_table[hashed_key]
        for index, record in enumerate(bucket):
            recordkey, recordvalue = record
            if recordkey == key:
                found = True
                break;
        if found:
            return recordvalue
        else:
            return "Not found"

    def delete(self, key):
        hashed_key = hash(key) % self.size
        found = False
        bucket = self.hash_table[hashed_key]
        for index, record in enumerate(bucket):
            recordkey, recordvalue = record
            if recordkey == key:
                found = True
                break;
        if found:
            bucket.pop(index)
            return "Deleted"
        else:
            return "Not found"


    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = hashTableAlgo(256)
hash_table.set_val('saloni@test.com', 'kkk')
hash_table.set_val('s@test.com', 'aaa')
hash_table.set_val('a@test.com', 'sss')
hash_table.set_val('d@test.com', 'ddd')
result = hash_table.get_val('h@test.com')

print(result)
print(hash_table)

delrec = hash_table.delete('saloni@test.com')
print(delrec)
print(hash_table)
