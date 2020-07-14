#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import math

ejemplo_de_valores_aceptables = [ 5 , 2.4 , 6 , 4.6 ]
print("PROGRAMA PARA CALCULAR CONSUMO DE GASOLINA Y VELOCIDAD MEDIA")
print("\n")
mensaje_de_ayuda = 'PARA UN CALCULO EFICIENTE DE LOS DATOS, SE DEBE INGRESAR NUMEROS POSITIVOS'
print(mensaje_de_ayuda)
print("\n")
print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
print("\n")
print('AHORA VA A PROCEDER A DIGITAR LO QUE EL PROGRAMA LE INDIQUE')
print("\n")
print('PRIMERO VA A INGRESAR LA CANTIDAD DE KM RECORRIDOS. LUEGO VA A INGRESAR EL PRECIO DE LA GASOLINA POR LITRO')
print('DESPUES DEBE INGRESAR EL DINERO GASTADO EN GASOLINA DURANTE EL VIAJE Y EL TIEMPO QUE SE HA TARDADO DURANTE EL VIAJE')
print("\n")
print(f"TE RECUERDO QUE", mensaje_de_ayuda)

valorDeEntradaPorUsuario = None

while True:
    try:
        print("\n")
        print("Agrega la cantidad de KM recorridos: ")
        valorDeEntradaPorUsuario = input()
        print("\n")
        if float(valorDeEntradaPorUsuario) >= 0:
            print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto. Procederemos a continuar.")
            break
        else:
            print(f"La cifra ingresada es negativa. La distancia recorrida en km, en este ejercicio, no es un valor negativo")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
            continue
    except:
        print('\n')
        if type(valorDeEntradaPorUsuario) != (int,float):
            print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
        continue
print("\n")

cantidad_de_km_recorridos = float(valorDeEntradaPorUsuario)
print("La cantidad de KM recorridos es de:", cantidad_de_km_recorridos,'km')

while True:
    try:
        print("\n")
        print("Agrega el precio de la gasolina (por litro): ")
        valorDeEntradaPorUsuario = input()
        print("\n")
        if float(valorDeEntradaPorUsuario) >= 0:
            print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto. Procederemos a continuar.")
            break
        else:
            print(f"La cifra ingresada es negativa. El dinero, en este ejercicio, no es un valor negativo")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
            continue
    except:
        print('\n')
        if type(valorDeEntradaPorUsuario) != (int,float):
            print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
        continue
print("\n")

precio_de_gasolina_por_litro = float(valorDeEntradaPorUsuario)
print("El precio de la gasolina por cada litro es de: $", precio_de_gasolina_por_litro)

while True:
    try:
        print("\n")
        print("Agrega el dinero gastado en el viaje: ")
        valorDeEntradaPorUsuario = input()
        print("\n")
        if float(valorDeEntradaPorUsuario) >= 0:
            print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto. Procederemos a continuar.")
            break
        else:
            print(f"La cifra ingresada es negativa. El dinero, en este ejercicio, no es un valor negativo")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
            continue
    except:
        print('\n')
        if type(valorDeEntradaPorUsuario) != (int,float):
            print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
        continue
print("\n")

dinero_gastado_en_el_viaje = float(valorDeEntradaPorUsuario)
print("El dinero gastado en el viaje es de: $",dinero_gastado_en_el_viaje)
print('\n')
print('AHORA AGREGA EL TIEMPO QUE HA DURADO EL VIAJE')
while True:
    try:
        print("\n")
        print("Agrega las horas que ha pasado viajando: ")
        valorDeEntradaPorUsuario = int(input())
        print("\n")
        if valorDeEntradaPorUsuario >= 0:
            print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto. Procederemos a continuar.")
            break
        else:
            print(f"La cifra ingresada es negativa. El tiempo, en este ejercicio, no es un valor negativo")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
            continue
    except:
        print('\n')
        if type(valorDeEntradaPorUsuario) != int:
            print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
        continue
print("\n")

horas_de_viaje = int(valorDeEntradaPorUsuario)
print("La cantidad de horas viajando es de:", horas_de_viaje)

while True:
    try:
        print("\n")
        print("Agrega los minutos que ha pasado viajando: ")
        valorDeEntradaPorUsuario = int(input())
        print("\n")
        if valorDeEntradaPorUsuario >= 0:
            print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto. Procederemos a continuar.")
            break
        else:
            print(f"La cifra ingresada es negativa. El tiempo, en este ejercicio, no es un valor negativo")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
            continue
    except:
        print('\n')
        if type(valorDeEntradaPorUsuario) != int:
            print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            print(f"UN CONSEJO... SE ACEPTAN VALORES NUMERICOS CON DECIMALES Y ENTEROS MAYORES QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)
        continue
print("\n")

minutos_de_viaje = int(valorDeEntradaPorUsuario)
print("La cantidad de horas viajando es de:", minutos_de_viaje)
print("\n")

litros_de_gasolina_consumidos = float
litros_de_gasolina_consumidos = dinero_gastado_en_el_viaje / precio_de_gasolina_por_litro

litros_de_gasolina_por_km = float
litros_de_gasolina_por_km = litros_de_gasolina_consumidos / cantidad_de_km_recorridos

dinero_consumido_por_km = float
dinero_consumido_por_km = dinero_gastado_en_el_viaje / cantidad_de_km_recorridos

tiempo_consumido_en_horas = float
tiempo_consumido_en_horas = horas_de_viaje + (minutos_de_viaje/60)

velocidad_media_en_km_sobre_hora = float
velocidad_media_en_km_sobre_hora = cantidad_de_km_recorridos / tiempo_consumido_en_horas

velocidad_media_en_metros_sobre_segundos = float
velocidad_media_en_metros_sobre_segundos = (cantidad_de_km_recorridos * 1000) / (tiempo_consumido_en_horas * 3600)


valor_de_km_a_evaluar_por_el_ejercicio = 100

consumo_de_litros_de_gasolina_cada_100km = float
consumo_de_litros_de_gasolina_cada_100km = litros_de_gasolina_por_km * valor_de_km_a_evaluar_por_el_ejercicio 

costo_de_gasolina_cada_100km = float
costo_de_gasolina_cada_100km = dinero_consumido_por_km * valor_de_km_a_evaluar_por_el_ejercicio

barra_de_separacion = '================================================================================='
print(barra_de_separacion)
print("CONSUMO DE GASOLINA (EN LITROS Y DOLARES) POR CADA", valor_de_km_a_evaluar_por_el_ejercicio,"km")
print("EN LITROS:", round(consumo_de_litros_de_gasolina_cada_100km,4),"lts")
print("EN DOLARES: $", round(costo_de_gasolina_cada_100km,2))
print("\n")
print(barra_de_separacion)
print("CONSUMO DE GASOLINA (EN LITROS Y DOLARES) POR CADA KM")
print("EN LITROS:", round(litros_de_gasolina_por_km,4),"lts")
print("EN DOLARES: $", round(dinero_consumido_por_km,2))
print("\n")
print(barra_de_separacion)
print("VELOCIDAD MEDIA (EN km/h Y m/s)")
print("EN km/h:", round(velocidad_media_en_km_sobre_hora,2))
print("EN m/s:", round(velocidad_media_en_metros_sobre_segundos,2))
print("\n")


# In[ ]:




