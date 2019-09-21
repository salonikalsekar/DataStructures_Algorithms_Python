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



    def get_val(self):
        pass

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = hashTableAlgo(256)
print(hash_table)
hash_table.set_val('saloni@test.com', 'kkk')
hash_table.set_val('saloni@gmail.com', 'kkk')

print(hash_table)