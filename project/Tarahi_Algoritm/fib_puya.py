__author__ = 'alizadeh'


def fib(n):
#takhsis hafeze
    p = (n + 1)
    Array_a = [-1] * p
    Array_a[0] = 0
    Array_a[1] = 1

    return fib1(n, Array_a)


def fib1(n, Array_a):
    if n == 0:
        return Array_a[0]
    if n == 1:
        return Array_a[1]
    else:
        if Array_a[n] >= 0:
            return Array_a[n]
        else:
            x = fib1(n - 1, Array_a)
            y = fib1(n - 2, Array_a)
            Array_a[n] = x + y

            print  Array_a[n]
            return Array_a[n]


a = fib(6)
