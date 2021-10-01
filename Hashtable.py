
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


# t = HashTable()
# t["march 6"] = 130
# t["march 17"] = 450
# t['march 8'] = 67
# t['march 9'] = 4

# print(t.arr)


# del t['march 9']
# print(t.arr)


###############EXERCISES##################
import csv

nyc_weather = []
with open('nyc_weather.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        temp = line['temperature(F)']
        nyc_weather.append(int(temp))

"""
What was the average temperature in first week of Jan?
"""
first_week_temp = nyc_weather[:6] 
average = sum(first_week_temp)/len(first_week_temp)
print(average)

"""
What was the maximum temperature in first week of Jan?
"""
maximum_temp = max(first_week_temp)
print(maximum_temp)

"""
You have to read this file in python and print every word and its count as show below. 
Think about the best data structure that you can use to solve this problem and figure out
why you selected that specific data structure.
"""
##SOLUTION1-not good#######
word_counter = {}
with open('poem.txt') as file:
    for line in file:
        for word in line.split():
            key = str(word)
            if key in word_counter:
                word_counter[key] += 1
            else:
                word_counter[key] = 1

###SOLUTION2-better#####
with open('poem.txt') as f:
    words = f.read()
    word_counter = {}
    for word in words.replace(',', ' ').split():
        word_counter[word] = word_counter.setdefault(word, 0) + 1
print(word_counter)




