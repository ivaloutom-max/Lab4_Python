# --------------------------------------------------
# Student: Ivan Loufer
# Class: Python
# Professor: David Busch
# Lab 4 - Part 2: Dictionaries
# --------------------------------------------------

# Función que toma dos listas y devuelve un diccionario
def makeDictionary(names, scores):
    scoreDict = {}
    for i in range(len(names)):
        scoreDict[names[i]] = scores[i]
    return scoreDict

# Función para calcular el promedio de las puntuaciones
def calculateAverage(scores_dict):
    values = scores_dict.values()
    return sum(values) / len(values)

# Programa principal
def main():
    # Listas de estudiantes y calificaciones dadas
    names = ['Joe', 'Tom', 'Barb', 'Sue', 'Sally']
    scores = [10, 23, 13, 18, 12]
    
    # Asignar el resultado de makeDictionary a scoreDict
    scoreDict = makeDictionary(names, scores)
    
    # Imprimir scoreDict
    print("Initial scoreDict:", scoreDict)
    
    # Buscar la puntuación de 'Barb' e imprimirla
    print("Score for 'Barb':", scoreDict['Barb'])
    
    # Añadir una puntuación de 19 para 'John' e imprimir el diccionario
    scoreDict['John'] = 19
    print("scoreDict after adding John:", scoreDict)
    
    # Crear una lista ordenada de todas las puntuaciones e imprimirla
    sorted_scores = sorted(scoreDict.values())
    print("Sorted list of scores:", sorted_scores)
    
    # Usar una función para calcular el promedio de las puntuaciones e imprimirlo
    average = calculateAverage(scoreDict)
    print("Average of all scores:", average)
    
    # Actualizar la puntuación de 'Sally' a 13 e imprimir el diccionario
    scoreDict['Sally'] = 13
    print("scoreDict after updating Sally's score:", scoreDict)
    
    # Eliminar a 'Tom' y su puntuación e imprimir el diccionario
    del scoreDict['Tom']
    print("scoreDict after removing Tom:", scoreDict)

# Ejecutar el programa
main()