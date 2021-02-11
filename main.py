print("Bienvenido. ¿En qué te puedo ayudar?")

print("Cuento con estas funciones: \n")
print("1. Menú")
print("2. Promociones")
print("3. Horario \n")
print("¿Qué opción deseas? (Elige el núm)")

### Datos ###

menu  = ["Quesadillas","Torta de Jamón", "Hot Cakes", "Huevo con chorizo", "Spaguetti"]

promociones = ["Martes 2x1", "Viernes de HotCakes", "Lunes de 3x2"]

horario = {

"Lunes": "9am a 1pm",
"Martes": "9am a 12pm",
"Miercoles": "9am a 2pm",
"Jueves": "9am a 3pm",
"Viernes": "9am a 1pm",

}

### Opción almacenada elegida por el usuario ###

opcion = int(input()) 

### Funciones ###

def mostrar_mensaje (lista):
    contador = 1
    for dato in lista:
        print(f"{contador} - {dato}")
        contador+=1

def mostrar_mensaje2 (lista):
    for dia, hora in lista.items():
        print(f"{dia} - {hora}")
            
def texto_menu():
    print("Elegiste el servicio de Menú")

def texto_promociones():
    print("Elegiste el servicio de Promociones")

def texto_horario():
    print("Elegiste el servicio de Horarios")
    print("Nuestro horario es:")

def elegir_opcion(option):
    while option > 3: # Si es mayor a 3, significa que no es ni la opción de 1, 2 o 3.
        print("Elige nuevamente una opción del 1 al 3")
        option = int(input())
        if option == 1:
            texto_menu()
            mostrar_mensaje(menu)
        elif option == 2:
            texto_promociones()
            mostrar_mensaje(promociones)
        elif option == 3:
            texto_horario()
            mostrar_mensaje2(horario)

### Bloque condicional ###

if opcion == 1:
    texto_menu()
    mostrar_mensaje(menu)
elif opcion == 2:
    texto_promociones()
    mostrar_mensaje(promociones)
elif opcion == 3:
    texto_horario()
    mostrar_mensaje2(horario)
else:
    elegir_opcion(opcion)




