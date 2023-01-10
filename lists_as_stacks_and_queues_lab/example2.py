from _collections import deque

example_deque = []

for i in range(1, 6):
    example_deque.append(i)

print("Deque from list")
while example_deque:
    print(example_deque.pop(0))