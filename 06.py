star = 0
space = 10

for i in range(1,20,1):
    if i<10:
        star = star + 1
        space = 10

    elif  i == 10:
        star = 20
        space = 0

    elif  i > 10:
        star = 20 - i
        space = space + 1

    print(" " * space + "*" * star)