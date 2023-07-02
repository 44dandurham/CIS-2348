#Daniel Durham 1851947

import csv

input1 = input()

uppercase_freq = {}
lowercase_freq = {}

with open(input1, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        for word in row:
            word = word.strip()

            if word.isupper():
                uppercase_freq[word] = uppercase_freq.get(word, 0) + 1
            else:
                lowercase_freq[word] = lowercase_freq.get(word, 0) + 1


for word, frequency in lowercase_freq.items():
    print(f'{word} {frequency}')
for word, frequency in uppercase_freq.items():
    print(f'{word} {frequency}')

