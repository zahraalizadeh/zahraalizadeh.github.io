__author__ = 'alizadeh'

def fib(n):
 x,y,i=0,1,2

 while i<=n:
     z=x+y
     print z
     x=y
     y=z
     i += 1

 return z

fib(5)