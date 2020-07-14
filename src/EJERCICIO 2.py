#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 

ejemplo_de_valores_aceptables = [ 5 , 2.4 , 6 , 4.6 ]
print("INGRESE CINCO NUMEROS PARA ORDENAR DE MANERA ASCENDENTE")
print("\n")
print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
print("\n")
print("LA PARTE DECIMAL DE UN NUMERO EMPIEZA DESPUES DE UN PUNTO. NO SE UTILIZAN COMAS")

while True:
  try:
    print("\n")
    print("Agrega el valor:")
    valorDeEntradaPorUsuario_1 = input()
    print("\n")
    if float(valorDeEntradaPorUsuario_1) >= 0:
      print(f"Excelente. El ", valorDeEntradaPorUsuario_1, " si es un valor correcto.")
      break
    else:
      print(f"El ", valorDeEntradaPorUsuario_1, " no es un valor correcto. Es una cifra negativa.")
      print("\n")
      print("AYUDA:")
      print(f"TE RECUERDO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)

  except:
    print("\n")
    if type(valorDeEntradaPorUsuario_1) != (int,float):
      print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")

print('\n')
print('SEGUIMOS CON EL SEGUNDO NUMERO')

while True:
  try:
    print("\n")
    print("Agrega el valor:")
    valorDeEntradaPorUsuario_2 = input()
    print("\n")
    if float(valorDeEntradaPorUsuario_2) >= 0:
      print(f"Excelente. El ", valorDeEntradaPorUsuario_2, " si es un valor correcto.")
      break
    else:
      print(f"El ", valorDeEntradaPorUsuario_2, " no es un valor correcto. Es una cifra negativa.")
      print("\n")
      print("AYUDA:")
      print(f"TE RECUERDO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)

  except:
    print("\n")
    if type(valorDeEntradaPorUsuario_2) != (int,float):
      print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")

print('\n')
print('SEGUIMOS CON EL TERCER NUMERO')

while True:
  try:
    print("\n")
    print("Agrega el valor:")
    valorDeEntradaPorUsuario_3 = input()
    print("\n")
    if float(valorDeEntradaPorUsuario_3) >= 0:
      print(f"Excelente. El ", valorDeEntradaPorUsuario_3, " si es un valor correcto.")
      break
    else:
      print(f"El ", valorDeEntradaPorUsuario_3, " no es un valor correcto. Es una cifra negativa.")
      print("\n")
      print("AYUDA:")
      print(f"TE RECUERDO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)

  except:
    print("\n")
    if type(valorDeEntradaPorUsuario_3) != (int,float):
      print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")

print('\n')
print('SEGUIMOS CON EL CUARTO NUMERO')

while True:
  try:
    print("\n")
    print("Agrega el valor:")
    valorDeEntradaPorUsuario_4 = input()
    print("\n")
    if float(valorDeEntradaPorUsuario_4) >= 0:
      print(f"Excelente. El ", valorDeEntradaPorUsuario_4, " si es un valor correcto.")
      break
    else:
      print(f"El ", valorDeEntradaPorUsuario_4, " no es un valor correcto. Es una cifra negativa.")
      print("\n")
      print("AYUDA:")
      print(f"TE RECUERDO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)

  except:
    print("\n")
    if type(valorDeEntradaPorUsuario_4) != (int,float):
     print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")

print('\n')
print('SEGUIMOS CON EL ULTIMO NUMERO')

while True:
  try:
    print("\n")
    print("Agrega el valor:")
    valorDeEntradaPorUsuario_5 = input()
    print("\n")
    if float(valorDeEntradaPorUsuario_5) >= 0:
      print(f"Excelente. El ", valorDeEntradaPorUsuario_5, " si es un valor correcto.")
      break
    else:
      print(f"El ", valorDeEntradaPorUsuario_5, " no es un valor correcto. Es una cifra negativa.")
      print("\n")
      print("AYUDA:")
      print(f"TE RECUERDO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
      
  except:
    print("\n")
    if type(valorDeEntradaPorUsuario_5) != (int,float):
      print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")
    #continue
print('\n')
print('EXCELENTE! HAS INGRESADO LOS CINCO NUMEROS. AHORA PROCEDEREMOS A ORDENARLOS DE MENOR A MAYOR')
print('\n')

agrupar_valores_recibidos = np.array([
                                      valorDeEntradaPorUsuario_1,
                                      valorDeEntradaPorUsuario_2,
                                      valorDeEntradaPorUsuario_3,
                                      valorDeEntradaPorUsuario_4,
                                      valorDeEntradaPorUsuario_5
                                      ])

#se debe tener cuidado con los tipo de datos dentro de los numpy arrays.
#Por eso se hace la conversion a enteros. De esta manera, el orden de los numeros se hace de manera correcta
convertir_a_enteros_array_numpy = agrupar_valores_recibidos.astype(float)

orden_ascendente = np.sort(convertir_a_enteros_array_numpy)
print(f"EL ORDEN, DE MENOR A MAYOR, DE LOS VALORES INGRESADOS, ES EL SIGUIENTE: ", orden_ascendente)


# In[ ]:




