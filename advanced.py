from typing import List


numbers: List[int] = []

for i in range(10):
    if i % 2 == 0:
        numbers.append(i)

print(numbers)

numbers = [i for i in range(10) if i % 2 == 0]
print(numbers)
