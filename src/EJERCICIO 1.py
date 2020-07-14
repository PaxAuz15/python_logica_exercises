#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 

multiplo_a_buscar = 5 #se deja la variable capaz de ser editable 

#Se crea un arreglo para mostrar un ejemplo por medio de un mensaje
multiplos = [
    multiplo_a_buscar*1,
    multiplo_a_buscar*2,
    multiplo_a_buscar*3,
    multiplo_a_buscar*4,
    multiplo_a_buscar*5,'...']

print(f"SUMATORIA DE LOS MULTIPLOS DE ", multiplo_a_buscar)
print("\n")

#mensaje de ayuda utilizando el arreglo de multiplos
print(f"UNA AYUDA... LOS MULTIPLOS DE ",
      multiplo_a_buscar,"son: ", multiplos,". ADEMAS, DEBEN SER UN ENTERO POSITIVO EL QUE INGRESE")

#se declara la variable. Se utiliza None para no tener problemas al aplicar validaciones por tipo de elemento
valorDeEntradaPorUsuario = None

#validaciones para sólo utilizar un valor entero positivo y descartar cualquier otro ingreso del usuario
while True:
    try:
        print("\n")
        print(f"Agregar una cifra. Debe ser múltiplo de ", multiplo_a_buscar,":")
        valorDeEntradaPorUsuario = int(input())
        print("\n")
        if valorDeEntradaPorUsuario > 0 and valorDeEntradaPorUsuario % multiplo_a_buscar == 0:
          print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un múltiplo de ",multiplo_a_buscar, ". Procederemos a continuar.")
          break
        else:
          if valorDeEntradaPorUsuario < 0:
            print("La cifra ingresada es un valor negativo.")
            print(f"UNA AYUDA... LOS MULTIPLOS DE ",
                  multiplo_a_buscar,"son: ", multiplos,". ADEMAS, DEBEN SER UN ENTERO POSITIVO EL QUE INGRESE")
            continue
          print(f"La cifra ingresada no es múltiplo de ",multiplo_a_buscar)
          print("\n")
          print("AYUDA:")
          print(f"UNA AYUDA... LOS MULTIPLOS DE ",
                  multiplo_a_buscar,"son: ", multiplos)
    except:
        print('\n')
        if type(valorDeEntradaPorUsuario) != int:
          print("Revise lo que ha ingresado. No es un múltiplo de ",multiplo_a_buscar, ". Tampoco es un valor entero. Vuelva a introducir un valor correcto para poder continuar.")
        continue
print("\n")


auxiliarParaImprimir = 1 #Sirve
lista_de_numeros = []

for contadorParaImprimir in range(multiplo_a_buscar, valorDeEntradaPorUsuario+auxiliarParaImprimir, multiplo_a_buscar):
#for contadorParaImprimir in range(valorDeEntradaPorUsuario,multiplo_a_buscar-auxiliarParaImprimir, -multiplo_a_buscar):
  lista_de_numeros += [contadorParaImprimir]#
print(f"La lista de números múltiplos de ",multiplo_a_buscar, "disponibles son: ",lista_de_numeros)

numeros_impares = [ lista_de_numeros for lista_de_numeros in lista_de_numeros if lista_de_numeros % 2 == 1]
print(numeros_impares)

lista_de_numeros_impares = np.array(numeros_impares)
cantidad_de_numeros_impares = len(np.where(lista_de_numeros_impares % 2 == 1)[0])
print(cantidad_de_numeros_impares)

suma_multiplos = np.sum(lista_de_numeros)
print(suma_multiplos)


# In[ ]:




