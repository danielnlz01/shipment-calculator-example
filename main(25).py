tipo_de_envio=int(input())
ancho=0
largo=0
peso=0
tipo_de_carga=""
costo=0

def envio1(ancho,largo,peso,tipo_de_carga):
  ancho=int(input())
  largo=int(input())
  peso=int(input())
  tipo_de_carga=input()
  if (tipo_de_carga=="Pesada" or "Delicada"):
    return ancho*largo*peso/12
  elif (tipo_de_carga!="Pesada" or "Delicada"):
    return ancho*largo*peso/10

def envio2(ancho,largo,peso,tipo_de_carga):
  ancho=int(input())
  largo=int(input())
  peso=int(input())
  tipo_de_carga=input()
  if (tipo_de_carga=="Pesada" or "Delicada"):
    return ancho*largo*peso/10
  elif (tipo_de_carga!="Pesada" or "Delicada"):
    return ancho*largo*peso/8

def envio3(ancho,largo,peso,tipo_de_carga):
  ancho=int(input())
  largo=int(input())
  peso=int(input())
  tipo_de_carga=input()
  if (tipo_de_carga=="Delicada"):
    return ancho*largo*peso/5
  elif (tipo_de_carga!="Pesada" or "Delicada"):
    return ancho*largo*peso/3

if (tipo_de_envio==1):
  costo=envio1(ancho,largo,peso,tipo_de_carga)
  print('{0:.2f}'.format(costo))
elif (tipo_de_envio==2):
  costo=envio2(ancho,largo,peso,tipo_de_carga)
  print('{0:.2f}'.format(costo))
elif (tipo_de_envio==3):
  costo=envio3(ancho,largo,peso,tipo_de_carga)
  print('{0:.2f}'.format(costo))
else:
  print("El tipo de envío no existe")
