star = 0

for i in range (1,20,1,):
    if i < 10:
        star = star + 1
        space = - 1
        print (" " * space + "*" * star)

    elif i == 10:
        space = 0
        print (" " * space + "*" * 20)

    elif  i > 20:
        space = 10
        print (" " * space + "*" * star)
        star = star - 1

