import random

lister = sorted([random.randint(1,300) for _ in range(6_000_000)])


value = random.choice(lister)
print(value)

low = 0
high = len(lister) - 1

while low <= high:
    mid = (low + high) // 2
    guess = lister[mid]
    if guess == value:
        print("Элемент найден. Его индекс:", mid)
        break
    if guess > value:
        high = mid - 1
    else:
        low = mid + 1
