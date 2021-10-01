
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX


    def find_slot(self, array):
        for elem in array:
            if elem is None:
                return array.index(elem)
        raise Exception("Hashmap full")


    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            empty_ind = self.find_slot(self.arr)
            self.arr[empty_ind]=(key,val)
        print(self.arr)


    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            raise KeyError("Such key doesn't exist")
        return self.arr[h][1]


    def __delitem__(self, key):
        h = self.get_hash(key)
        
        if self.arr[h]:
            self.arr[h] = None
        elif self.arr[h] is None:
            raise Exception("Index is already empty") 
        else:
            raise Exception("No such key in a dictionary")


t = HashTable()
t["march 6"] = 130
t['march 8'] = 67
t['march 9'] = 4
t["march 17"] = 450
# print(t["march 6"])
del t['march 9']
print(t.arr)