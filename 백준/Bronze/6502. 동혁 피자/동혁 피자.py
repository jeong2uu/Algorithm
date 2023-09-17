from sys import stdin

i = 1
while 1:
    pizza = list(map(int, stdin.readline().split()))
    if pizza[0] == 0:
        break
    r, w, l = pizza

    table = r * 2
    pizza = (w**2 + l**2) ** 0.5

    if table >= pizza :
      print("Pizza {} fits on the table.".format(i))
    else :
      print("Pizza {} does not fit on the table.".format(i))
    
    i += 1
