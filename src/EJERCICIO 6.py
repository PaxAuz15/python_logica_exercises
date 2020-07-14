#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
import math

ejemplo_de_valores_aceptables = [ 5 , 2.4 , 6 , 4.6 ]
print("INGRESE CINCO NUMEROS PARA ORDENAR DE MANERA ASCENDENTE")
print("\n")
print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
print("\n")
print("LA PARTE DECIMAL DE UN NUMERO EMPIEZA DESPUES DE UN PUNTO. NO SE UTILIZAN COMAS")

valorDeEntradaPorUsuario = None

while True:
  try:
    print("\n")
    print("Agrega el valor:")
    valorDeEntradaPorUsuario = input()
    print("\n")
    if float(valorDeEntradaPorUsuario) >= 0:
      print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto.")
      break
    else:
      print(f"El ", valorDeEntradaPorUsuario, " no es un valor correcto. Es una cifra negativa.")
      print("\n")
      print("AYUDA:")
      print(f"TE RECUERDO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)

  except:
    print("\n")
    if type(valorDeEntradaPorUsuario) != (int,float):
      print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")
    continue
print('\n')


separarParteEnteraDeDecimales = str(valorDeEntradaPorUsuario).split(".")

cantidad_de_elementos_separados = len(separarParteEnteraDeDecimales)

acumulador_de_la_suma_NumeroPerfectos = 0
contador_para_suma_NumeroPerfectos = None

if cantidad_de_elementos_separados == 1:
  parte_entera = int(separarParteEnteraDeDecimales[0])
  print(parte_entera)
  separar_digitos = list(map(int,str(parte_entera)))
  ultimo_digito = separar_digitos.pop()
  print(ultimo_digito)
else:
  parte_entera = int(separarParteEnteraDeDecimales[0])
  parte_decimal = int(separarParteEnteraDeDecimales[1])
  print(parte_entera)
  print(parte_decimal)
  separar_digitos = list(map(int,str(parte_decimal)))
  ultimo_digito = separar_digitos.pop()
  print(ultimo_digito)

for contador_para_suma_NumeroPerfectos in range(1,ultimo_digito):
  if ultimo_digito % contador_para_suma_NumeroPerfectos == 0:
    acumulador_de_la_suma_NumeroPerfectos += contador_para_suma_NumeroPerfectos
  
if ultimo_digito == acumulador_de_la_suma_NumeroPerfectos:
  print(f"El último dígito de",valorDeEntradaPorUsuario,"es",ultimo_digito,
        "El", ultimo_digito,"si es un número perfecto" )
else:
  print(f"El último dígito de",valorDeEntradaPorUsuario,"es",ultimo_digito,
        "El", ultimo_digito,"no es un número perfecto" )

