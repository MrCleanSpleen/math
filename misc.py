import skilstak.colors as c
import time as t
import math

def solve_squareroot():
    """Finds the square root of a number"""
    inpu = input("square root what number? >>> ")
    i = int(inpu)
    answer = int
    answer = math.sqrt(i)
    print("square root is",answer)

def solve_percircle():

    b = input("radius >>> ")
    c = int(b)
    a = int
    a = 3.14 * 2 * c
    print(a)
def solve_slope():
    print(""" (x, y) and (x, y)
               ⇩  ⇩       ⇩  ⇩
               x1 y1      x2 y2""")
    xa = input("x1 >>> ")
    ya = input("y1 >>> ")
    xb = input("x2 >>> ")
    yb = input("y2 >>> ")
    x1 = int(xa)
def solve_py():
    print("""
             |\ 
             | \ 
             |  \c
            a|   \ 
             |    \ 
             |     \ 
             |______\ 
                b   """)
    print("What side are you missing?")
    answer = input(">>> ")
    if answer == "a":
        q = input("b value >>> ")
        w = input("c value >>> ")
        b = int(q)
        c = int(w)
        a = int
        b1 = int
        c1 = int
        b1 = b * b
        c1 = c * c
        cb2 = int
        cb2 = c1 - b1
        cb3 = int
        cb3 = math.sqrt(cb2)
        print("a value is",cb3)
    elif answer == "b":
        e = input("a value >>> ")
        r = input("c value >>> ")
        b = int(e)
        c = int(r)
        a = int
        b1 = int
        c1 = int
        b1 = b * b
        c1 = c * c
        cb2 = int
        cb2 = c1 - b1
        cb3 = int
        cb3 = math.sqrt(cb2)
        print("b value is",cb3)
    elif answer == "c":
        t = input("a value >>> ")
        y = input("b value >>> ")
        a = int(t)
        b = int(y)
        a1 = int
        b1 = int
        a1 = a * a
        b1 = b * b
        ab11 = int
        ab11 = a1 + b1
        c = math.sqrt(ab11)
        print("c value is",c)

