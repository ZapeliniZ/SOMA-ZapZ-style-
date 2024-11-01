a, b, c, d = map(int, input().split(" "))
sumAB = a+b
sumCD = c+d


if b>c and d<a and sumAB<sumCD and c>= 0 and d>= 0 and (a%2) == 0: 
     print("Valores aceitos")
else:
    print("Valores nao aceitos")    