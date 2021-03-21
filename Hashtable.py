class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, elem in enumerate(self.arr[h]):
            if len(elem) == 2 and elem[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for elem in self.arr[h]:
            if elem[0] == key:
                return elem[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, elem in enumerate(self.arr[h]):
            if elem[0] == key:
                del self.arr[h][index]


t = HashTable()
t["march 6"] = 130
t["march 17"] = 450
t['march 8'] = 67
t['march 9'] = 4

print(t.arr)


del t['march 9']
print(t.arr)
# print(t.get_hash("march 6"))
# print(t.get_hash("march 109"))
# print(t.arr)


