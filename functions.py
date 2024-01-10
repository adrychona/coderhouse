"""
from google.colab import drive
drive.mount("/drive/",force_remount=True)
ruta = "/drive/MyDrive/Colab Notebooks"

"""

def crear_registro(BD):
  username = input("Por favor ingrese un nombre de usuario ")
  contraseña = input("Por favor ingrese una contraseña ")
  BD[username] = contraseña
  print("El usuario ha sido registrado correctamente")
  
def mostrar_registro(BD):
  print("A continuación visualize los usuarios agregados: ")
  for clave, valor in BD.items():
    print(clave, valor)

"""def guardar_datos(BD):

  with open(ruta+"/usuarios.txt", "w") as registro:
    registro.write( '\n' + str(BD) + '\n')
  print("Los usuarios han sido guardados correctamente en el archivo usuarios.txt")"""

def log_in(DB):
  usuario = input("Por favor ingrese su usuario ")
  if usuario in DB.keys():
    contraseña = input("Por favor ingrese su contraseña ")
    if contraseña == DB.get(usuario):
      print("Usted ha iniciado sesión correctamente")
    else:
      print("La contraseña ingresada es incorrecta")
  else:
    print("El nombre de usuario ingresado no existe")

registroUsuarios = {}
crear_registro(registroUsuarios)
mostrar_registro(registroUsuarios)
#guardar_datos(registroUsuarios)
log_in(registroUsuarios)
