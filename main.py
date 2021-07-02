import random
x=random.randint(1,6)
y=random.randint(1,6)
print("What is your name?")
print("> ",end="")
name=input()
print("Hello, %s!"%name)
print(("""Rolling the dice...
Die 1: %d
Die 2: %d
Total value: %d
You %s!""")%(x,y,x+y,"won" if x+y>7 else "lost"))
