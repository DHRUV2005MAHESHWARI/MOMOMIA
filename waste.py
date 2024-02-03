import tkinter
import os
import platform

def sum(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def mul(a,b):
    c=a*b
    print(c)
def div(a,b):
    c=a/b
    print(c)

while ch=='y':
    choose=input("enter the choise from (+,-,*,/)")
    a=int(input("enter a"))
    b=int(input("enter b"))
    match(choose):
        case '+':
            sum(a,b)
        case '-':
            sub(a,b)
        case '*':
            mul(a,b)
        case '/':
            div(a,b)
    ch=input("do you want more or not if you more colaculation then press y other wise press n")
# def sum():
#     a=6
#     b=0 
#     sum=a+b
#     return sum
# a=sum()
# print(a)
