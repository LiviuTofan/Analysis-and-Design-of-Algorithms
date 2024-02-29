# 6 functions to find fibonacci n-th term
from math import sqrt
import numpy as np
import time
import matplotlib.pyplot as plt
def Fibonacci1(n):
    if n <= 1:
        return n
    else:
        return Fibonacci1(n - 1) + Fibonacci1(n - 2)

def Fibonacci2(n):
    num = [0, 1]

    for i in range(2, n+1):
        num.append(num[i-1] + num[i-2])

    return num[n]

def Fibonacci3(n):
    a = 0
    b = 1

    if n <= 1:
        return n
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b


def Fibonacci4(n):
    F1 = [1, 1,
          1, 0]

    return matrix_power(F1, n)[1]


def matrix_multiply(A, B):
    a, b, c, d = A
    x, y, z, w = B

    return (
        a * x + b * z,
        a * y + b * w,
        c * x + d * z,
        c * y + d * w,
    )
def matrix_power(A, m):
    if m == 0:
        return [1, 0, 0, 1]
    elif m == 1:
        return A
    else:
        B = A
        n = 2
        while n <= m:
            # repeated square B until n = 2^q > m
            B = matrix_multiply(B, B)
            n = n*2
        # add on the remainder
        R = matrix_power(A, m-n//2)
        return matrix_multiply(B, R)

def Fibonacci5(n):
    ans = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    return int(ans)

def Fibonacci6(n):
    F1 = np.array([[1, 1], [1, 0]])
    eigenvalues, eigenvectors = np.linalg.eig(F1)
    Fn = eigenvectors @ np.diag(eigenvalues ** n) @ eigenvectors.T
    return int(np.rint(Fn[0, 1]))

def measure_time(n):
    start_time = time.time()
    result = Fibonacci5(n)
    end_time = time.time()
    final_time = end_time - start_time
    return result, final_time

elements = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 35, 37, 40, 42, 45]
#elements = [500, 650, 800, 1000, 1250, 1500, 2000, 2550, 3150, 4000, 5000, 6350, 8000, 10000, 12500, 16000]
time_values = []

print("n\ttime(s)")
for element in elements:
    result, final_time = measure_time(element)
    time_values.append(final_time)
    print(f"{element}\t{final_time:.6f}")

plt.plot(elements, time_values, marker='o')
plt.xlabel('N-th Fibonacci Term')
plt.ylabel('Time (s)')
plt.title('Fibonacci Binet Formula')
plt.show()