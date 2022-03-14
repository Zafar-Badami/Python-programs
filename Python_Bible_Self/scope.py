# There are two types of scopes  GLOBAL and LOCAL
# Python functions create local variables
# But LOOPs and IF statements don't.

# ---------------------------- def for variables -----------------------------------------
a=250 # global vartiable 
print(a)

def f1():

    global a  # To can't override a global variable in a function until you define them as global.
    
    a=100 # global
    print(a)

def f2():
    a=50 # local
    print(a)

f1()
f2()
print(a)

# ----------------------------------------- def for lists ------------------------------------
l = [1,2,3]
print(l)

def g1():
    l[0]=5  # You can override small little pieces in list without defining them as global. But you
                # can't change the whole list.
    print(l)

def g2():
     l=50
     print(l)

g1()
g2()
print(l)
