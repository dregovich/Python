import random
import datetime
import prettytable
import matplotlib.pyplot as plt

def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

def QuickSort(A, fst, lst):
    if fst >= lst:
        return

    pivot = A[fst]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)

def insertion_sort(A):
    for i in range(1, len(A)):
        t = A[i]
        j = i
        while j > 0 and A[j-1] > t:
            A[j] = A[j-1]
            j -= 1
        A[j] = t

def shaker_sort(A):
    left = 0
    right = len(A) - 1
    while left <= right:
        for i in range(left, right):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
        right -= 1
        for i in range(right, left, -1):
            if A[i-1] > A[i]:
                A[i], A[i-1] = A[i-1], A[i]
        left += 1

array = [5, 2, 10, 1, 7]
insertion_sort(array)
print(array)

table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой", "Время вставкой", "Время Shaker"])
x = []
y1 = []
y2 = []
y3 = []
y4 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random()*(max-min)+min)))

    B = A.copy()

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка " + str(N) + " заняла " + str((t2 - t1).total_seconds()) + "с")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B)-1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая " + str(N) + " заняла " + str((t4 - t3).total_seconds()) + "с")

    C = A.copy()

    t5 = datetime.datetime.now()
    insertion_sort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Сортировка вставкой " + str(N) + " заняла " + str((t6 - t5).total_seconds()) + "с")

    D = A.copy()

    t7 = datetime.datetime.now()
    shaker_sort(D)
    t8 = datetime.datetime.now()
    y4.append((t8 - t7).total_seconds())
    print("Сортировка Shaker " + str(N) + " заняла " + str((t8 - t7).total_seconds()) + "с")

    table.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()), str((t6 - t5).total_seconds()), str((t8 - t7).total_seconds())])

print(table)

plt.plot(x, y1, "C0", label="Пузырьковая сортировка")
plt.plot(x, y2, "C1", label="Быстрая сортировка")
plt.plot(x, y3, "C2", label="Сортировка вставкой")
plt.plot(x, y4, "C3", label="Сортировка Shaker")
plt.legend()
plt.show()