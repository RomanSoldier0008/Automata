import re
import url

def main():
   while True:
      print("Bienvenidos, seleccione una opción")
      print("Opción 1 URL")
      print("Opción 2 SALIR\n")
      opcion = int(input("Opción: "))
      if (opcion == 1):
         url.dir()
         input("\nPresione enter para continuar ")
      elif (opcion == 2):
         exit(print("""Gracias por visitar nuestra app,vuelva pronto"""))
      else:
         print("La opcion ingresada es incorrecta")

main()