import numpy as np
import random
#MULTIPLICACION DE DOS MATRICES CON DIMENSIONES DEFINIDAS POR EL USUARIOS
#PRIMERA MATRIZ
print("\tMULTIPLICACION DE MATRICES")
print()
valor1=int (input ("Por favor ingrese la dimension en x de su primera matriz: "))
valor2=int (input ("Por favor ingrese la dimension en y de su primera matriz: "))
dim=(valor1,valor2)
print()
print("\tSU PRIMERA MATRIZ ES: ")
print()
matriz1=np.random.randint(1,25,dim)
print(matriz1)
print()

#SEGUNDA MATRIZ
valor3=int (input ("Por favor ingrese la dimension en x de su segunda matriz: "))
valor4=int (input ("Por favor ingrese la dimension en y de su segunda matriz: "))
dim2=(valor3,valor4)
print()
print("\tSU SEGUNDA MATRIZ ES: ")
print()
matriz2=np.random.randint(1,25,dim)
print(matriz2)
print()

#MULTIPLICACION DE MATRICES
matriz_mult=np.dot(matriz1,matriz2)
print("\tLA MULTIPLICACION DE LAS 2 MATRICES ES: ")
print ()
print (matriz_mult)