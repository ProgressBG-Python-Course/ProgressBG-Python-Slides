def number_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1


for num in number_generator(1, 5):
    print(num, end=",")


# def fibonacci_generator(n):
#     a = 0
#     b = 1

#     for _ in range(n):
#         yield a
#         a, b = b, a + b


# for number in fibonacci_generator(10):
#     print(number, end="")
