#sistema para calcular promedio de un alumno
#utilizando sentencia condicional simple (if)

print("sistema para calcular promedio de un alumno")
nombre = input("para comenzar escriba su nombre: ")

matematicas = int(input(nombre + " ¿cual es su calificacion en matematicas?: "))
quimica = int(input(nombre + " ¿cual es su calificacion en quimica?: "))
biologia = int(input(nombre + " ¿cual es su calificacion en biologia?: "))

promedio = (matematicas + quimica + biologia) / 3

#variable para no obtener un numero con decimales

promedio = int(promedio)

#aplicando sentencia condicional

if promedio >= 6:
    print('felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)
print("fin")

