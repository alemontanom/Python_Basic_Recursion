#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:32:41 2021

@author: alemontano
"""

def TRIM (a):#a es un string, le quita los espacios al inicio y al final 
    if a[0]==" ":
        a=a[1:]
        TRIM(a)
    elif a[len(a)-1]==" ":
        a=a[:-1]
        TRIM(a)
    else:
        print (a)
    

def funcionBinomial(n,k):
    sum = 0
    if n<k:
        return 0
    elif k==0:
        return 1
    else: 
        return sum + funcionBinomial(n-1, k-1) + funcionBinomial(n-1, k)
    
def imprimirArregloAR(a, n): #necesita pedir el tamaño del arreglo
    if n>=2:
        return str(a[n-1]) + ", " + str(imprimirArregloAR(a, n-1))
    else:
        return str(a[0])

def imprimirArregloAR2(a, i): #iniciar i con 1
    if i<=len(a)-1:
        return str(a[len(a)-i]) + ", " + str(imprimirArregloAR2(a, i+1))
    else:
        return str(a[0])
    
def sumaVec(a, i): #del primero al ultimo, iniciar i en 0
    if i<len(a)-1:
        return a[i] + sumaVec(a, i+1)
    else:
        return a[len(a)-1]

matriz = [[1, 2, 3], [4, 5, 6]]

def imprimeMatriz (matriz):
    for renglon in matriz :
        for elemento in renglon:
            print(elemento, end=" ")
        print()

def imprimeMatrizRec (matriz, i):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()
    if i+1 < len(matriz):
        imprimeMatrizRec (matriz, i+1)

#imprimeMatrizRec(matriz, 0)


def selDirecta(lista):#ordenar lista 
     for i in range(len(lista)-1):
         minimo = i
         for j in range (i+1, len(lista)) :
            min=lista[minimo]
            if lista[j] < lista[minimo]:
                lista[minimo]=lista[j]
                lista[j]=min
                minimo = j
     return lista
 
def selDirectaRec(lista, i):
    minimo = i
    for j in range (i+1, len(lista)) :
        min=lista[minimo]
        if lista[j] < lista[minimo]:
            lista[minimo]=lista[j]
            lista[j]=min
            minimo = j     
    if i+1<len(lista):
        selDirectaRec(lista, i+1)
    #return lista
"""l=[30, 56, 2, 9, 102]       
selDirectaRec(l, 0)
print(l)
#print(selDirectaRec([30, 56, 2, 9, 102], 0))"""

def fibonacciRec (n): #muy malo en terminos de eficiencia 
    if n <= 1 :
        return 1
    return  fibonacciRec(n-1) + fibonacciRec(n-2)

calculados = {0:1, 1:1} 
 
def fibonacciRecM(n): #no vuelve a hacer todas las operaciones
    if n in calculados: 
        return calculados[n]
    calculados[n] = fibonacciRecM(n-1) + fibonacciRecM(n-2)
    return calculados[n]

#for i in range(10):
    #print(fibonacciRecM(i))


def factorialRec (n): 
    if n==0 or n==1:
        return 1
    else :
        return n*factorialRec(n-1)

def imprimeNumeros (n):
    if n<=0:
        print(0)
    else:
        print (n)
        imprimeNumeros(n-1)
        
def iterativoFactorial (x):
    if x == 0 or x == 1:
        return 1
    resultado = 1 
    for i in range (2, x+1):
        resultado *= i 
        i+= 1 
    return resultado

def recursivoFactorial (y):
    if y==0 or y==1:
        return 1
    return y*recursivoFactorial(y-1)



def busBinIter(lista, dato): 
    lista.sort() #pierdes el orden original de los datos
    bajo = 0
    alto = len(lista)-1
    while bajo<=alto:
        centro = int((bajo + alto) /2 )
        if lista[centro] == dato : 
            return centro # regresa el índice de la lista donde esta el dato
        elif lista[centro] < dato :
            bajo = centro + 1
        else :
            alto = centro - 1 
    return "no esta"

def busBinaria (lista, dato) :
    return busRec(lista.sort(), 0, len(lista), dato)

def busRec (lista, bajo, alto, dato):
    lista.sort()
    if bajo > alto: 
        return -1
    centro = (bajo + alto) //2 #indice
    if lista[centro] == dato: 
        return centro 
    elif lista[centro] < dato: 
        return busRec(lista, centro+1, alto, dato)
    else : 
        return busRec(lista, bajo, centro-1, dato)
    
""" 
l = [30, 45, 65, 2, 987, 39]
print(busBinIter(l, 987)) 
print(busRec(l, 0, len(l)-1,  2))

for i in l:
    print(busRec(l, 0, len(l)-1, i)) """
        
""" medir que toma menos tiempo
from time import perf_counter

inicio = perf_counter()
for i in range (100000):
    recursivoFactorial(10)

fin = perf_counter()

inicio1 = perf_counter()
for i in range (100000):
    iterativoFactorial(10)

fin1 = perf_counter()

print("recursivo: ",str(fin-inicio))
print("iterativo: ",str(fin1-inicio1)) """

