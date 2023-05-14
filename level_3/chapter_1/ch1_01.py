"""
Chapter 1 - Python Advanced (1) : Python Variable Scope
Keywords : scope, global, nonlocal, locals, globals
"""
"""  # =================================================================================================================
- global : usually use for unchanged static values
  - modifying global variables inside local area is not recommended
- local : confined to used for resolving logic inside functions, destroyed after function terminated
"""  # =================================================================================================================

# global, local ========================================================================================================
# Ex 1 -----------------------------------------------------------------------------------------------------------------
a = 10  # global variable


def foo():
    # Read global variable
    print("Ex1 > ", a)


foo()

# Read global variable
print("Ex1 > ", a)
print()
# Ex 2 -----------------------------------------------------------------------------------------------------------------
b = 20


def bar():
    b = 30  # local variable
    print("Ex2 > ", b)  # read local variable


bar()
print("Ex2 > ", b)  # read global variable
print()
# Ex 3 -----------------------------------------------------------------------------------------------------------------
c = 40

""" UnboundLocalError: local variable 'c' referenced before assignment
def foobar():
    c = 10
    c = c + 10
    print("Ex 3 > ", c)


foobar()
"""
# Ex 4 -----------------------------------------------------------------------------------------------------------------
d = 50


def barfoo():
    global d
    d = 60
    d += 100
    print("Ex 4 > ", d)


barfoo()
print("Ex 4 > ", d)
print()
# ----------------------------------------------------------------------------------------------------------------------
# ======================================================================================================================


# NonLocal =============================================================================================================
# Ex 5 (IMPORTANT) -----------------------------------------------------------------------------------------------------
""" UnboundLocalError: local variable 'e' referenced before assignment
def outer():
    e = 70

    def inner():
        e += 10
        print("Ex 5 > ", e)

    return inner


in_test = outer()  # Closure
in_test()
"""


def outer():
    e = 70

    def inner():
        nonlocal e
        e += 10
        print("Ex 5 > ", e)

    return inner


in_test = outer()  # Closure
in_test()
in_test()
in_test()
print()
# ----------------------------------------------------------------------------------------------------------------------
# ======================================================================================================================


# locals, globals ======================================================================================================
# Ex 6 -----------------------------------------------------------------------------------------------------------------
def func(var):
    x = 10

    def printer():
        print("Ex 6 > ", "Print Func Inner")

    print("Func Inner", locals())  # print all local variables


func("Hi")
print()
# Ex 7 -----------------------------------------------------------------------------------------------------------------
print("Ex 7 > ", globals())  # print all global variables
test_variable1 = 100
print("Ex 7 > ", globals())
globals()['test_variable2'] = 200
print("Ex 7 > ", globals())
print()
# Ex 8 -----------------------------------------------------------------------------------------------------------------
# 지역 -> 전역 변수 생성
for i in range(1, 10):
    for k in range(1, 10):
        globals()['plus_{}_{}'.format(i, k)] = i + k
print("Ex 8 > ", globals())
print("Ex 8 > ", plus_5_5)
print("Ex 8 > ", plus_9_9)
# ----------------------------------------------------------------------------------------------------------------------
# ======================================================================================================================