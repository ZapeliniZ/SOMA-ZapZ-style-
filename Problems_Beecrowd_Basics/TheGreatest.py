def scr1():
    a, b, c = map(int, input().split(" "))
    majorAB = (a+b+abs(a-b))/2
    majorABC = (majorAB+c+abs(majorAB-c))/2
    print (int(majorABC), "eh o maior")

'''
def scr2():
     linha = input().split(" ") 
     a = int(linha[0]) 
     b = int(linha[1]) 
     c = int(linha[2]) 
     maiorAB = (a + b + abs(a - b))/2 
     maiorABC = (maiorAB + c + abs(maiorAB - c))/2 
     print(int(maiorABC), 'eh o maior') 
'''

if __name__ == "__main__":
     scr1()