# def fibonacci_sequence(n):
#     if n < 0:
#         print("Please enter a positive")
#         return []
#     fib_array = []
#     for i in range(n):
#         if i == 0:
#             fib_array.append(0)
#         elif i == 1:
#             fib_array.append(1)
#         else:
#             fib_array.append(fib_array[i - 1] + fib_array[i - 2])
#
#     return fib_array
#
#
# print(fibonacci_sequence(20))


def fibonacci_recursive(n):
    if n < 0:
        print("Incorrect input")
        return []
    fib_array = []
    if n == 0:
        return [0]
    elif n == 1 or n == 2:
        return [0, 1]
    else:
        fib_array = fibonacci_recursive(n - 1)
        fib_array.append(fib_array[-1] + fib_array[-2])
        return fib_array


print(fibonacci_recursive(10))


this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict["brand"])
print(this_dict.get('brand'))