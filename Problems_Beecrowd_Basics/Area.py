A, B, C = map(float, input().split(" "))
pi = 3.14159
areaTriangle = (A*C)/2
areaCirlce = pi*C**2
areaTrapezium = ((A+B)/2)*C
areaSquare = B**2
areaRectangle = A*B
print("TRIANGULO: {0:.3f}".format(areaTriangle))
print("CIRCULO: {0:.3f}".format(areaCirlce))
print("TRAPEZIO: {0:.3f}".format(areaTrapezium))
print("QUADRADO: {0:.3f}".format(areaSquare))
print("RETANGULO: {0:.3f}".format(areaRectangle))