#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np 
import math

ciudad = 'MANTA'
locacion_de_parqueo_segun_la_ciudad = 'EL CENTRO'

print(f"PROGRAMA PARA CALCULAR EL MONTO A PAGAR POR SERVICIO DE ESTACIONAMIENTO AUTOMATICO EN", 
      locacion_de_parqueo_segun_la_ciudad,
      'DENTRO DE LA CIUDAD DE', 
      ciudad)
print("\n")
mensaje_de_ayuda = 'PARA UN CALCULO EFICIENTE DE LOS DATOS, SE DEBE INGRESAR LOS VALORES EN ENTEROS POSITIVOS'
print(mensaje_de_ayuda)
print("\n")
print('AHORA VA A PROCEDER A DIGITAR EL TIEMPO QUE HA CONSUMIDO EL SERVIDO DE ESTACIONAMIENTO')
print("\n")
print('PRIMERO VA A INGRESAR LA CANTIDAD DE HORAS. LUEGO VA A INGRESAR LA CANTIDAD DE MINUTOS')
print("\n")
print(f"TE RECUERDO QUE", mensaje_de_ayuda)

valorDeEntradaPorUsuario = None

while True:
    try:
        print("\n")
        print("Agrega las horas que ha pasado estacionado: ")
        valorDeEntradaPorUsuario = int(input())
        print("\n")
        if valorDeEntradaPorUsuario >= 0:
            print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto. Procederemos a continuar.")
            break
        else:
            print(f"La cifra ingresada es un entero pero es negativo. El tiempo, en este ejercicio, no es un valor negativo")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            continue
    except:
        print('\n')
        if type(valorDeEntradaPorUsuario) != int:
            print("Revise lo que ha ingresado. No es un entero")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
        continue
print("\n")

horas_de_estacionamiento = valorDeEntradaPorUsuario
print("La cantidad de horas en el estacionamiento es de:", horas_de_estacionamiento)

while True:
    try:
        print("\n")
        print("Agrega los minutos que ha pasado estacionado: ")
        valorDeEntradaPorUsuario = int(input())
        print("\n")
        if valorDeEntradaPorUsuario >= 0:
            print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto. Procederemos a continuar.")
            break
        else:
            print(f"La cifra ingresada es un entero pero es negativo. El tiempo, en este ejercicio, no es un valor negativo")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            continue
    except:
        print('\n')
        if type(valorDeEntradaPorUsuario) != int:
            print("Revise lo que ha ingresado. No es un entero")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
        continue
print("\n")

minutos_de_estacionamiento = valorDeEntradaPorUsuario
print("La cantidad de minutos en el estacionamiento es de:", minutos_de_estacionamiento)
print("\n")
print("Se procederá a calcular el valor a pagar")
print("\n")
convertir_horas_a_minutos = horas_de_estacionamiento * 60

total_minutos_estacionado = convertir_horas_a_minutos + minutos_de_estacionamiento


cuanto_pagar = float

costo_base_de_estacionamiento = 0.50
costo_de_cada_cuarto_de_hora_fuera_de_la_hora_base = 0.10
minutos_a_cobrar_fuera_de_la_hora_base = 15


if total_minutos_estacionado > 60:
    minutos_de_estacionamiento_fuera_de_la_hora_base = total_minutos_estacionado - 60
    cantidadDeCuartosDeHoraCumplidos = minutos_de_estacionamiento_fuera_de_la_hora_base / minutos_a_cobrar_fuera_de_la_hora_base
    parte_decimal, parte_entera = math.modf(cantidadDeCuartosDeHoraCumplidos)
    if parte_decimal > 0:
        cantidadDeCuartosDeHoraCumplidos = parte_entera + 1
        cuanto_pagar = costo_base_de_estacionamiento + (int(cantidadDeCuartosDeHoraCumplidos) * costo_de_cada_cuarto_de_hora_fuera_de_la_hora_base)
else:
    cuanto_pagar = costo_base_de_estacionamiento

print(f"Usted estuvo utilizando", 
      horas_de_estacionamiento,
      "horas con", 
      minutos_de_estacionamiento, 
      "minutos el estacionamiento. El valor a cancelar del servicio es de $", round(cuanto_pagar,2))


# In[ ]:





# In[ ]:




