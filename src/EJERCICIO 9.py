#!/usr/bin/env python
# coding: utf-8

# In[28]:


mensaje_de_ayuda = 'SE DEBE INGRESAR EL VALOR A EVALUAR. ESO SE DEBE INGRESAR COMO UN NUMERO ENTERO POSITIVO'

ejemplo_de_valores_aceptables = [2, 4, 6, 32, 45, 69]
print("INGRESE DOS VALORES. SE VA A PROCEDER A MULTIPLICAR LOS VALORES INGRESADOS")
print("\n")
print(f"SE DEBEN INGRESAR VALORES QUE SEAN POSITIVOS:", ejemplo_de_valores_aceptables)

while True:
  try:
    print("\n")
    print("Agrega el primer valor:")
    valorDeEntradaPorUsuario = input()
    print("\n")
    if int(valorDeEntradaPorUsuario) >= 0:
      print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto.")
      break
    else:
      print(f"El ", valorDeEntradaPorUsuario, " no es un valor correcto. Es una cifra negativa.")
      print("\n")
      print("AYUDA:")
      print(f"TE RECUERDO... SE ACEPTAN VALORES ENTEROS QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)

  except:
    print("\n")
    if type(valorDeEntradaPorUsuario) != (int):
      print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")
valor_1 = int(valorDeEntradaPorUsuario)
valor_1_para_mensajes = int(valorDeEntradaPorUsuario)
print('\n')
print('SEGUIMOS CON EL SEGUNDO NUMERO')

while True:
  try:
    print("\n")
    print("Agrega el segundo valor:")
    valorDeEntradaPorUsuario = input()
    print("\n")
    if int(valorDeEntradaPorUsuario) >= 0:
      print(f"Excelente. El ", valorDeEntradaPorUsuario, " si es un valor correcto.")
      break
    else:
      print(f"El ", valorDeEntradaPorUsuario, " no es un valor correcto. Es una cifra negativa.")
      print("\n")
      print("AYUDA:")
      print(f"TE RECUERDO... SE ACEPTAN VALORES ENTEROS QUE SEAN POSITIVOS: ", ejemplo_de_valores_aceptables)

  except:
    print("\n")
    if type(valorDeEntradaPorUsuario) != (int):
      print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")

valor_2_para_mensajes = int(valorDeEntradaPorUsuario)
valor_2 = int(valorDeEntradaPorUsuario)


resultado_de_multiplicacion = 0
while valor_2 != 0:
    resultado_de_multiplicacion = resultado_de_multiplicacion + valor_1
    valor_2 = valor_2 -1


print('\n') 
print(f"El resultado de multplicar",valor_1_para_mensajes,"con",valor_2_para_mensajes,"es:",resultado_de_multiplicacion)


# In[ ]:




