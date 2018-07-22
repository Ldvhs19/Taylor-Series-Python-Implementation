# ******************This code is for adding first four terms in the taylor series*******************************
# f(x)= f(0) + f'(0)*x/1! + f''(0)*x**2/2! + f'''(0)*x**3/3!
# *******************************************************************************************************************
# The math module implements many of the IEEE functions that would normally be found in the native platform C libraries
# for complex mathematical operations using floating point values, including logarithms and trigonometric operations.
import math
#defining the function of taylor series and setting various parameters
def taylor_series(fun,deri,doubleder,triple,y):
    value1 = fun(y)
   #this paramter is used to input the value of variable in the taylor series equation
    a=float(input("Enter the value of x: "))
    value2 = deri(y)*a/math.factorial(1)
    value3 = doubleder(y)*a**2/math.factorial(2)
    value4 = triple(y)*a**3/math.factorial(3)
    output= value1 + value2 + value3 + value4;
    return output
#this is for function f(x)
def fun(y):
    return math.sin(y)
#this is for first derivative of function f(x)
def deri(y):
    return math.cos(y)
#this is for second derivative of function f(x)
def doubleder(y):
    return -math.sin(y)
#this is for third derivative of function f(x)
def triple(y):
    return -math.cos(y)
out = taylor_series(fun,deri,doubleder,triple,y=0)
print ("Result after sum of four terms in taylor series is:",out)
