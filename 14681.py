x = int(input(""))
y = int(input(""))

def graph(x, y):
    if x > 0:
        if y > 0:
            return 1
        elif y < 0:
            return 4
    elif x < 0:
        if y > 0:
            return 2
        elif y < 0:
            return 3

print(graph(x,y))