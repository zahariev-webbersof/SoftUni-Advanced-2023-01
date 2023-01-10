data = input()
indexes = []

for i in range(len(data)):
    ch = data[i]

    if ch == '(':
        indexes.append(i)
    elif ch == ')':
        l = indexes.pop()
        print(data[l:i + 1])

