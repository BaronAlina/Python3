partial_sum = 0
partial_sum_squares = 0
x_i = int(input())
n = 0
while x_i != 0:
    n += 1
    partial_sum += x_i
    partial_sum_squares += x_i ** 2
    x_i = int(input())
print(((partial_sum_squares - partial_sum ** 2 / n) / (n - 1))**0.5)
