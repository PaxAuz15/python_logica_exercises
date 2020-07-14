#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 

ejemplo_de_valores_aceptables = [ 5 , 6 ]
mensaje_de_ayuda = 'SE DEBE INGRESAR LA CANTIDAD ELEMENTOS A EVALUAR. ESO SE DEBE INGRESAR COMO UN NUMERO ENTERO POSITIVO'

valorDeEntradaPorUsuario = None

while True:
    try:
        print("\n")
        print("¿Cuántos valores quieres evaluar?")
        valorDeEntradaPorUsuario = int(input())
        print("\n")
        if valorDeEntradaPorUsuario > 0:
            print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto. Procederás a evaluar e ingresar", valorDeEntradaPorUsuario,"elementos.")
            break
        else:
            print(f"La cifra ingresada es negativa. La cantidad de elementos a evaluar, en este ejercicio, no es un valor negativo")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            print(f"UN CONSEJO... SE ACEPTAN SOLO ENTEROS QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
            continue
    except:
        print('\n')
        if type(valorDeEntradaPorUsuario) != int:
            print("El valor ingresado no es el correcto. Revise que sea un número entero positivo lo que se encuentre ingresando")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            continue
print("\n")
cantidad_de_numeros_a_ingresar_por_usuario_para_mensajes = int(valorDeEntradaPorUsuario)
cantidad_de_numeros_a_ingresar_por_usuario = int(valorDeEntradaPorUsuario)
contador_de_elementos_ingresados_por_usuario = 1
contenedor_de_elementos_ingresados = []  

while cantidad_de_numeros_a_ingresar_por_usuario > 0:
  try:
    print("\n")
    print("Agrega el valor #", contador_de_elementos_ingresados_por_usuario)
    valorDeEntradaPorUsuario = input()
    print("\n")
    if float(valorDeEntradaPorUsuario) >= 0:
      print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto.")
      contenedor_de_elementos_ingresados.append(valorDeEntradaPorUsuario)
      #print(cantidad_de_numeros_a_ingresar_por_usuario)
      cantidad_de_numeros_a_ingresar_por_usuario -= 1
      contador_de_elementos_ingresados_por_usuario += 1
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
  
arreglo_numpy_contenedor_de_elementos_ingresados = np.asarray(contenedor_de_elementos_ingresados)
convertir_a_enteros_array_numpy = arreglo_numpy_contenedor_de_elementos_ingresados.astype(int)
orden_ascendente = np.sort(convertir_a_enteros_array_numpy)
print(f"El orden ascendente, de menor a mayor, de los", cantidad_de_numeros_a_ingresar_por_usuario_para_mensajes,"ingresados es la siguiente:", orden_ascendente)
eliminar_mayor_numero = np.delete(orden_ascendente, cantidad_de_numeros_a_ingresar_por_usuario-1)
print(eliminar_mayor_numero)
segunda_mayor_cantidad = eliminar_mayor_numero[cantidad_de_numeros_a_ingresar_por_usuario-1]

print("\n")
print(f"La segunda mayor cantidad ingresada por el usuario es:", segunda_mayor_cantidad)


# In[ ]:




