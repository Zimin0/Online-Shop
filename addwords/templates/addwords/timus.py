n = int(input())


results = []

for i in range(n):
    number = int(input())

    if number == 1:
        results.append(1)
        continue

    if ((-1 + (8*number - 7)**(0.5)) / 2 ) == int((-1 + (8*number - 7)**(0.5)) / 2 ):
        results.append(1)
    else:
        results.append(0)
    

print(*results)
