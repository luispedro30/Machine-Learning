print("Hello")
#%%
#Versão do python
import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

#%%
#dia e hora
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


#%%
#ârea do círculo
from math import pi
r = float(input("Input the radius of the circle : "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
#%%
#nome e apelido na ordem inversa
nome = str(input("Nome próprio"))
apelido = str(input("Apelido"))
print(str(apelido)+" "+str(nome))
#%%
def my_function(a,b,c,d):
    list = []
    tuple = []
    list.extend([a,b,c,d])
    tuple.extend([a,b,c,d])
    print(list)
    print(tuple)

my_function(3,5,7,23)
#%%
programa = str(input("Diga o nome do Programa"));
#linguagem = str(input("Diga a linguagem do Programa"));
#nome = programa+'.'+linguagem
def extensao(a):
    for i in range (len(programa)):
        if programa[i] == '.':
            index = i
            linguagem = a[index+1:]
    return linguagem
print(extensao(programa))

#%%
programa = str(input("Diga o nome do Programa"));
def extensao(a):
    linguagem = a.split(".")
    return linguagem[1]
print(extensao(programa))
#%%
def primeiro_ultimo(color_list):
    primeiro = color_list[0]
    ultimo = color_list[len(color_list)-1]
    print("A primeira cor é "+str(primeiro))
    print("A última cor é "+str(ultimo))

primeiro_ultimo(["Red", "Green", "White","Black"])
#%%
#Escreva um programa para obter o volume de uma esfera com raio 6.
import math
def volumeEsfera(raio):
    volume= (4/3)*math.pi*raio**3 #math.pow(raio,3)
    print(volume)

volumeEsfera(3)
#%%
def parImpar(a):
    if a%2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")


parImpar(a = int(input("Digite um número inteiro")))

#%%
def contarNumero4(a):
    contagem = 0
    for item in a:
        if item == 4:
            contagem += 1
    print(contagem)

contarNumero4([1,2,3,4,4,4])
#%%
def vogais(letra):
    vogal = "aeiou"
    if letra in vogal:
        print("A letra é uma vogal")
    else:
        print("A letra é uma consoante")

vogais(str(input("Digite uma letra")))
#%%
def valorContido(valor):
    lista = [1,5,8,3]
    print(valor in lista)

valorContido(int(input("Digite um valor")))
#%%
def valoresAntes(lista):
    i = 0
    listaFinal = []
    for index in range(len(lista)):
        if lista[index] == 234:
            i = index
    listaFinal = lista[:i]
    print(listaFinal)

valoresAntes([386, 462, 47, 418, 907, 344, 234, 375, 823, 566, 597])

#%%
def somaValores(a,b):
    soma = a+b
    if soma>15 and soma<20:
        soma = 20
    print(soma)

somaValores(int(input("Primeiro valor")),int(input("Primeiro valor")))
#%%
#(x + y) * (x + y).

def equacao(x,y):
    output = (x+y)*(x+y)
    print(output)

equacao(int(input("Valor de x")),int(input("Valor de y")))

#%%
#Distância Euclideana
#(x1,y1) (x2,y2)
import math
def disEuclideana (a,b):
    xDistance = a[0]-b[0]
    yDistance = a[1]-b[1]
    distance = math.sqrt(xDistance**2+yDistance**2)
    print("A distância em x e y é "+str(xDistance)+', '+str(yDistance)+' respetivamente')
    print("Distância euclidean é igual a "+str(distance))

disEuclideana((1,1),(0,0))
#%%
#maior do que certo valor
def maiorLista(lista, valor):
    bool = True
    for item in lista:
        if item < valor:
            bool = False
            break
    return bool

print(maiorLista([2,2,2,2], int(input("Valor:"))))
#%%
def contagemCaracter(caracter, palavra):
    contagem = 0
    for letra in palavra:
        if letra == caracter:
            contagem += 1
    print(contagem)

contagemCaracter("a","aaa")
#%%
"""
Encontre os números que são divisíveis por 7 e 
múltiplos de 5, entre 1500 e 2700 (ambos incluídos)
"""
def encontraNumero():
    for number in range(1500,2700):
        if number%5 == 0:
            print(number)

encontraNumero()
#%%
def inverte(palavra):
    return palavra[::-1]

print(inverte("Hello world!"))
#%%
def contagem(tuplo):
    contagemPar = 0
    contagemImpar = 0
    for item in tuplo:
        if item%2 ==0:
            contagemPar += 1
        else:
            contagemImpar += 1
    print(contagemPar)
    print(contagemImpar)

contagem((1, 2, 3, 4, 5, 6, 7, 8, 9) )
#%%
def contagem(palavra):
    contagemLetra = 0
    contagemNum = 0
    for item in palavra:
        #print(type(item))
        try:
            int(item)
            contagemNum += 1
        except:
            contagemLetra+=1
    print(contagemLetra)
    print(contagemNum)

contagem("Python 3.2")
#%%
"""
Nos primeiros dois anos, 
um ano canino corresponde a 10,5 anos humanos. 
Depois disso, cada ano canino
equivale a 4 anos humanos.
"""
def idadeCanina(idadeCao):
    idadeFinal = 0
    if idadeCao <=2:
        idadeFinal = idadeCao * 10.5
    else:
        idadeFinal = 2 * 10.5 + (idadeCao-2)*4
    return idadeFinal

print(idadeCanina(3))
