#!/usr/bin/env python
# coding: utf-8

# In[16]:


constante_de_evaluacion_1 = 100
constante_de_evaluacion_2 = 1000
rango_valido = [100,100]
while True:
  try:
    print("\n")
    print("Agrega el valor a evaluar:")
    valorDeEntradaPorUsuario = input()
    print("\n")
    if int(valorDeEntradaPorUsuario) >= constante_de_evaluacion_1 and int(valorDeEntradaPorUsuario) < constante_de_evaluacion_2:
      print(f"Excelente. El ", valorDeEntradaPorUsuario, 
            "si es un valor correcto. Se encuentra dentro del rango válido:",
           constante_de_evaluacion_1, "y",constante_de_evaluacion_2)
      break
    else:
      print(f"El ", valorDeEntradaPorUsuario, " no es un valor correcto. No se encuentra dentro del rango válido:",
           constante_de_evaluacion_1, "y",constante_de_evaluacion_2)
      print("\n")
      print("AYUDA:")
      print(f"TE RECUERDO... SE ACEPTAN VALORES ENTEROS QUE SEAN POSITIVOS Y SE ENCUENTREN DENTRO DEL RANGO VALIDO: ",rango_valido)

  except:
    print("\n")
    if type(valorDeEntradaPorUsuario) != (int):
      print("El valor ingresado no es el correcto. Revise que sea un número lo que se encuentre ingresando")

separar_digitos = list(map(int,str(valorDeEntradaPorUsuario)))
primer_digito = separar_digitos[0]
segundo_digito = separar_digitos[1]
tercer_digito = separar_digitos[2]

if primer_digito % 2 == 0 and segundo_digito %2 != 0 and tercer_digito %2 != 0:
    print("El valor ingresado", valorDeEntradaPorUsuario,"es M-alternante")
elif primer_digito % 2 != 0 and segundo_digito %2 == 0 and tercer_digito %2 == 0:
    print("El valor ingresado", valorDeEntradaPorUsuario,"es M-alternante")
else:
    print("El valor ingresado", valorDeEntradaPorUsuario,"NO es M-alternante")


    
    


# In[ ]:




