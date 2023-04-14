nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#limpio caracteres innecesarios y creo una lista con los nombres de los alumnos
lista_personas = [nom.strip(' \'\n') for nom in nombres.split(',')]

def generar_diccionario(estudiantes, notas1,notas2):
    """Funcion que toma las listas de estudiantes y notas y devuelve un diccionario"""
    
    return {persona:(nota1,nota2) for persona,nota1,nota2 in zip(estudiantes, notas1, notas2)}

def promedio_estudiantes (diccionario_alumnos):
    """Funcion que devuelve un diccionario con los promedios de los estudiantes, usando el diccionario generado por la funcion
    generar_diccionario """
    
    return {persona:promedio for persona,promedio in zip (lista_personas, (sum(dato)/2 for dato in diccionario_alumnos.values()))}

def promedio_general(diccionario_promedios):
    """Funcion que usando el diccionario de promedios, creado con la funcion promedio_estudiantes, devuelve el promedio general"""
    
    return sum(diccionario_promedios.values()) / len(diccionario_promedios)

def alumno_promedio_mas_alto(diccionario_promedios):
    """funcion que usando el diccionario de promedios, creado con la funcion promedio_estudiantes, devuelve el nombre del alumno
    con el promedio mas alto """

    #usa la funcion max con el parametro key con una funcion lambda para que la comparacion la realice con los valores del diccionario
    return (max(diccionario_promedios, key=lambda x: diccionario_promedios[x]))


def alumno_nota_mas_baja(diccionario_alumnos):
    """funcion que usando el diccionario, generado por la funcion generar_diccionario, devuelve el alumno con la nota mas baja """

    #usa la funcion min con el parametro key con una funcion lambda que busca el minimo de las dos notas
    return (min(diccionario_alumnos,key=lambda x:min(diccionario_alumnos[x][0],diccionario_alumnos[x][1])))
    
 
diccionario_alumno_notas = generar_diccionario(lista_personas,notas_1,notas_2)
promedios_alumnos = promedio_estudiantes(diccionario_alumno_notas)

print(f"\n Estructura generada: \n {diccionario_alumno_notas}")
print("\n" + "*" * 100 + "\n")
print (f"Promedio de todos los alumnos: \n {promedios_alumnos}")
print("\n" + "*" * 100 + "\n")
print(f"El promedio general del curso es {promedio_general(promedios_alumnos):.3f}\n")
print(f"El alumno con el mayor promedio es {alumno_promedio_mas_alto(promedios_alumnos)}\n")
print (f"El alumno con la nota mas baja es {alumno_nota_mas_baja(diccionario_alumno_notas)}\n")