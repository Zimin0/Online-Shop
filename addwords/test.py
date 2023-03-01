import time

times = []


def timer(func):
    def wrapper(arrange):
        global times
        start = time.time()
        func(arrange)
        end = time.time() - start
        times.append(end)
        #print(f"Время выполнения функции {func.__name__} = {end} сек.")
    return wrapper


lister = [i*i for i in range(120_500_000)][::-1]

@timer
def max1(arrange):
    sorted_arr = sorted(arrange)
    max_el = -1
    last = -1
    for i in sorted_arr:
        if i > last:
            max_el = i
        last = i
    print(max_el) 

@timer
def max2(arrange):
    sorted_arr1 = arrange
    max_el1 = -1
    last1 = -1
    for j in sorted(sorted_arr1):
        if j > last1:
            max_el1 = j
        last1 = j
    print(max_el1) 

for i in range(25):
    max1(lister)
    print(i)

print(times)
print("Среднее время из 25 вызовов:", sum(times)/len(times))


# на 900_500_000 на 40 вызовов
# max1 = 6.0400981366634365
# max2 = 5.881551313400268

# на 120_500_000 на 25 вызовов
# max1 = 15.68435242652893
# max2 = 16.270937299728395