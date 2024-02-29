import random
import time
import matplotlib.pyplot as plt

def quicksort(numbers, low, high):
    if low < high:
        pi = partition(numbers, low, high)
        quicksort(numbers, low, pi - 1)
        quicksort(numbers, pi + 1, high)

# Function to find the partition position
def partition(numbers, low, high):
    pivot = numbers[high]
    i = low - 1

    for j in range(low, high):
        if numbers[j] <= pivot:
            i = i + 1
            (numbers[i], numbers[j]) = (numbers[j], numbers[i])

    (numbers[i + 1], numbers[high]) = (numbers[high], numbers[i + 1])
    return i + 1


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def heapify(arr, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < N and arr[largest] < arr[l]:
        largest = l
        
    if r < N and arr[largest] < arr[r]:
        largest = r
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, N, largest)

def heapsort(arr):
    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if (swapped == False):
            break
def generate_random_num_list(n, data_type='integer'):
    if data_type == 'integer':
        return [random.randint(0, n) for _ in range(n)]
    elif data_type == 'float':
        return [random.uniform(0, n) for _ in range(n)]
    elif data_type == 'negative':
        return [random.randint(-n, 0) for _ in range(n)]

def measure_time(sort, numbers):
    start_time = time.time()
    sort(numbers)
    end_time = time.time()

    return end_time - start_time


def measure_sort(sort, sort_name):
    n_values = []
    time_values_integer = []
    time_values_float = []
    time_values_negative = []

    n_int_values = [1000, 100000, 1000000]
    print(f"{sort_name} Performance:")
    for n in n_int_values:
        numbers_integer = generate_random_num_list(n, 'integer')
        exec_time_integer = measure_time(sort, numbers_integer)
        print("For array with length", n, "time execution: ", exec_time_integer)


    for n in range(5000, 100000, 5000):
        # Measure time for integer data type
        numbers_integer = generate_random_num_list(n, 'integer')
        n_values.append(n)
        exec_time_integer = measure_time(sort, numbers_integer)
        time_values_integer.append(exec_time_integer)

        # Measure time for float data type
        numbers_float = generate_random_num_list(n, 'float')
        exec_time_float = measure_time(sort, numbers_float)
        time_values_float.append(exec_time_float)

        # Measure time for negative data type
        numbers_negative = generate_random_num_list(n, 'negative')
        exec_time_negative = measure_time(sort, numbers_negative)
        time_values_negative.append(exec_time_negative)

    plt.plot(n_values, time_values_integer, label='Integer')
    plt.plot(n_values, time_values_float, label='Float')
    plt.plot(n_values, time_values_negative, label='Negative')

    plt.xlabel("Array length")
    plt.ylabel("Time (s)")
    plt.title(f"{sort_name} Performance for Different Data Types")
    plt.legend()
    plt.show()

measure_sort(quicksort, 'Quick Sort')
