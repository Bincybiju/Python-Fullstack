# print("Hello world")

# words = ["cat", "dog", "car"]
# for i in words:
#     if i.startswith('ca'):
#         print(i)

# numbers = []
# while True:
#     num = int(input("Enter number: "))    
#     if num == 0:
#         break   
#     numbers.append(num)
# average = sum(numbers) / len(numbers)
# print(average)
num = "5+74"
operands = num.split('+')
print("Operands:", operands)

import re
num = "5+7-4"
operands = re.split('[+-]', num)
print("Operands:", operands)

import re
sentence = "Hello, world! This is an example sentence."
words = re.findall(r'\w+', sentence)
for i in words:
    print(i)

    
word = "example"
rev = ""
for i in range(len(word) - 1, -1, -1):
    rev += word[i]
print("Original word:", word)
print("Reversed word:", rev)