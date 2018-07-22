# Taylor-Series-Python-Implementation
![Equation of Taylor series](http://www.sciweavers.org/upload/Tex2Img_1532266287/render.png)
## Why Taylor Series is important

---

* Calculate approximate values of almost every important function on calculators and computers
* Computing transcendental functions such as e^x, sinx, and cosx.
* Taylor series is used to expand the functions. For example you want to know the expansion of sin(x), you can use Taylor series to implement it. 

---

### How single, double and triple differentiations are calculated
For this please look at these functions which I have created in the code
```
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
```
#### Limitation of this code
This code is used to find the approximate value till 4 terms. This is only for sin(x) expansion.
#### How to run this file
Just run the file taylor_series.py using python taylor_series.py and enter the value of variable which is x in the taylor series.
