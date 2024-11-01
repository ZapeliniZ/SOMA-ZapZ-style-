a, b, c = map(float, input().split(" "))
delta = (b**2)-4*a*c
if delta<0:
    print("Impossivel calcular")
else:
    A2 = 2*a
    if A2 == 0:
        print("Impossivel calcular")
    else:
        x1 = (-b+delta**0.5)/(A2)
        x2 = (-b-delta**0.5)/(A2)
        print("R1 = {0:.5f}".format(x1))
        print("R2 = {0:.5f}".format(x2))