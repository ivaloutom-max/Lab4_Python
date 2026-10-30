# --------------------------------------------------
# Student: Ivan Loufer
# Class: Python
# Professor: David Busch
# Lab 4 - Part 1: Word Counter
# --------------------------------------------------

# Función que recibe una frase y devuelve la cantidad de palabras
def countWords(sentence):
    words = sentence.split()
    return len(words)

# Programa principal
def main():
    # Solicitar la frase al usuario
    user_sentence = input("Enter a sentence: ")
    
    # Llamar a la función y guardar el resultado
    total = countWords(user_sentence)
    
    # Mostrar el resultado en pantalla
    print(f"The number of words in the sentence is: {total}")

# Ejecutar el programa
main()