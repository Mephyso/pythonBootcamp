def hello():
    print("Hello World")


hello()


def value():
    return "Hello World"


print(value())
print("------------------------------------------------------------")



def return_float() -> float:
    return 10


print(return_float())


def return_int() -> int:
    return 10.1


print(type(return_int()))
print("------------------------------------------------------------")



def square(n):
    return n*n


print(square(5))
# print(square("asd"))   (TypeError: can't multiply sequence by non-int of type 'str')


def divide(n: int, m: int):
    return n/m


print(divide(5, 2))
print("------------------------------------------------------------")


def summ(a, b=0, c=0):
    return a+b+c


print(summ(2))
print(summ(2, 5))
print(summ(2, 5, 7))
