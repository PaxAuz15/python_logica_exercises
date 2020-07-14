#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math 
ejemplo_de_valores_aceptables = [ 5 , 6 ]
print("PROGRAMA PARA CALCULAR EL VALOR DE LA CONSTANTE e UTILIZANDO UN VALOR INGRESADO POR EL USUARIO PARA LLEGAR A UN VALOR APROXIMADO")
print("\n")
print("AHORA, TE PUEDES FIJAR, HE HECHO UNA PEQUEÑA MODIFICACION AL PROGRAMA QUE SE PIDE. PARA PODER APLICAR CAJA BLANCA Y NEGRA DE MANERA SENCILLA")
print("\n")

mensaje_de_ayuda = 'SE DEBE INGRESAR LA CANTIDAD ELEMENTOS A EVALUAR. ESO SE DEBE INGRESAR COMO UN NUMERO ENTERO POSITIVO'

recomendacion = "SE DEBE INGRESAR UN VALOR ENTRE 4 Y 18 PARA OBSERVAR LAS APROXIMACIONES MAS CERCANAS AL VALOR DE EULER"
print(recomendacion)

valorDeEntradaPorUsuario = None

while True:
    try:
        print("\n")
        print("Ingrese un valor")
        valorDeEntradaPorUsuario = int(input())
        print("\n")
        if valorDeEntradaPorUsuario > 0 and valorDeEntradaPorUsuario < 19:
            print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto. Procederás a evaluar e ingresar", valorDeEntradaPorUsuario,"elementos.")
            break
        elif valorDeEntradaPorUsuario >= 19:
            print(f"TE RECOMENDÉ USAR NUMEROS ENTRE 4 Y 18. El ", valorDeEntradaPorUsuario, " NO SE ENCUENTRA EN ESE RANGO. TE VAS A DAR CUENTA EL MOTIVO DE MI RECOMENDACION")
            break
        else:
            print(f"La cifra ingresada es negativa. La cantidad de elementos a evaluar, en este ejercicio, no es un valor negativo")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            continue
    except:
        print('\n')
        if type(valorDeEntradaPorUsuario) != int:
            print("El valor ingresado no es el correcto. Revise que sea un número entero positivo lo que se encuentre ingresando")
            print(f"TE RECUERDO QUE", mensaje_de_ayuda)
            print("\n")
            continue
print("\n")


valor_de_euler = math.e
print("El valor de la constante de Euler es", valor_de_euler)
print('\n')

formula_para_calcular_euler = '1/0! + 1/1! + 1/2! + 1/3! + ... + 1/n!'
print("Se procederá a calcular el valor de la constante matemática e con la siguiente serie:", formula_para_calcular_euler)
print("\n")


print("=====================================================================")
print('{0:^25}{1:^25}'.format('Numero de elemento', 'Valor De Euler Calculado'))
print("=====================================================================")
valor_aproximado_euler_calculado = None
contenedor_para_suma = 0
for contador_de_elementos_para_la_serie in range(0,valorDeEntradaPorUsuario):
  valor_aproximado_euler_calculado = 1/math.factorial(contador_de_elementos_para_la_serie)
  contenedor_para_suma += valor_aproximado_euler_calculado
  print('{0:<25}{1:<25}'.format(contador_de_elementos_para_la_serie, contenedor_para_suma))

if valorDeEntradaPorUsuario >=19:
  print('\n')
  print(f"TE RECOMENDÉ USAR NUMEROS ENTRE 4 Y 18. El ", valorDeEntradaPorUsuario, " NO SE ENCUENTRA EN ESE RANGO.")
  print("SI TE FIJAS, LOS VALORES NO VARIAN POR LA CANTIDAD LIMITADA DE DECIMALES QUE SE ESTA UTILIZANDO")
  print('\n')
  print("PUDE VALIDAR QUE EL CICLO SOLO CONTINUE HASTA QUE EL VALOR SE PAREZCA AL REGISTRADO POR LA LIBRERIA MATH. PERO QUERIA SABER SI ERES NECIO O NO!")

