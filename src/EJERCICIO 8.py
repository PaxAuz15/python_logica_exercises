#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ejemplo_de_valores_aceptables = [ 24 , 40, 66, 75, 69 ]
constante_de_evaluacion_del_problema = 20
constante_de_evaluacion_del_problema_para_mensajes = 20

mensaje_de_ayuda = 'SE DEBE INGRESAR EL VALOR A EVALUAR. ESO SE DEBE INGRESAR COMO UN NUMERO ENTERO POSITIVO Y SER MAYOR A ' + str(constante_de_evaluacion_del_problema)

print("INGRESE UN VALOR. SE VA A PROCEDER A SUMAR LOS NUMEROS PARES COMPRENDIDOS ENTRE", constante_de_evaluacion_del_problema_para_mensajes, "Y EL VALOR QUE VA A INGRESAR")
print("\n")
print(f"UN CONSEJO... SE ACEPTAN VALORES SEAN POSITIVOS Y MAYORES A",constante_de_evaluacion_del_problema_para_mensajes,":", ejemplo_de_valores_aceptables)


valorDeEntradaPorUsuario = None
suma_de_los_numeros_pares = 0
while True:
    try:
        print("\n")
        print(f"Agregar una cifra:")
        valorDeEntradaPorUsuario = int(input())
        print("\n")
        if constante_de_evaluacion_del_problema <= valorDeEntradaPorUsuario:
          print(f"Excelente. El", valorDeEntradaPorUsuario, " si es un valor correcto.")
          break
        else:
          if valorDeEntradaPorUsuario < 0:
            print("La cifra ingresada es un valor negativo.")
            print(f"UNA AYUDA...", mensaje_de_ayuda)
            continue
          print(f"La cifra ingresada no es mayor a", constante_de_evaluacion_del_problema)
          print("\n")
          print("AYUDA:")
          print(f"UNA AYUDA...", mensaje_de_ayuda)
    except:
        print('\n')
        if type(valorDeEntradaPorUsuario) != int:
          print("Revise lo que ha ingresado. No un valor entero positivo. Vuelva a introducir un valor correcto para poder continuar.")
        continue
print("\n")

while constante_de_evaluacion_del_problema <= valorDeEntradaPorUsuario:
  suma_de_los_numeros_pares = suma_de_los_numeros_pares + constante_de_evaluacion_del_problema
  constante_de_evaluacion_del_problema = constante_de_evaluacion_del_problema + 2 

print("LA SUMA DE LOS NUMEROS PARES ENTRE", constante_de_evaluacion_del_problema_para_mensajes,"Y EL",valorDeEntradaPorUsuario,"ES",suma_de_los_numeros_pares)  

