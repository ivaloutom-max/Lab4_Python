# --------------------------------------------------
# Student: Ivan Loufer
# Class: Python
# Professor: David Busch
# Lab 4 - Part 3: Pirate Translator
# --------------------------------------------------

# Función que toma una frase en inglés y devuelve su traducción pirata
def toPirate(sentence):
    # Diccionario con traducciones básicas al estilo pirata
    pirate_dict = {
        "hello": "ahoy",
        "hi": "ahoy",
        "friend": "matey",
        "sir": "matey",
        "my": "me",
        "is": "be",
        "are": "be",
        "where": "wherebe",
        "the": "th'",
        "you": "ye"
    }
    
    words = sentence.split()
    pirate_words = []
    
    # Traducir palabra por palabra manteniendo minúsculas/mayúsculas básicas
    for word in words:
        clean_word = word.lower()
        if clean_word in pirate_dict:
            pirate_words.append(pirate_dict[clean_word])
        else:
            pirate_words.append(word)
            
    return " ".join(pirate_words)

# Programa principal
def main():
    # Solicitar frase y mostrar el resultado traducido
    user_sentence = input("Enter an English sentence: ")
    translated = toPirate(user_sentence)
    print("Pirate translation:", translated)

# Ejecutar el programa
main()