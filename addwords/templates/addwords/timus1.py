names = {
    "A": 1,
    "B": 2,
    "D": 3,
    "G": 3,
    "J": 3,
    "P": 1,
    "O": 1,
    "M": 2,
    "K": 3,
    "P": 1,
    "R": 1,
    "S": 2,
    "T": 3,
    "W": 3
}

n = int(input())
old_position = 1
count = 0

for _ in range(n):
    name = input()[0]
    now_position = names[name]
    count += (abs(now_position - old_position))
    old_position = now_position
print(count)
