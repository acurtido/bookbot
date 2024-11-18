from collections import Counter

def contar_palabras(texto):
    """Cuenta la cantidad de palabras en el texto proporcionado."""
    palabras = texto.split()
    return len(palabras)

def contar_caracteres_alfabeticos(texto):
    """Cuenta el número de veces que aparece cada carácter alfabético en el texto."""
    texto = texto.lower()  # Convertir todo a minúsculas
    contador = Counter(c for c in texto if c.isalpha())  # Filtrar solo caracteres alfabéticos
    return dict(contador)

def main():
    # Ruta al archivo frankenstein.txt
    path_to_file = "books/frankenstein.txt"
    
    # Leer y procesar el contenido del archivo
    try:
        with open(path_to_file, "r") as f:
            file_contents = f.read()
            
            # Contar palabras
            cantidad_palabras = contar_palabras(file_contents)
            
            # Contar caracteres alfabéticos
            cantidad_caracteres = contar_caracteres_alfabeticos(file_contents)
            
            # Generar el reporte
            print(f"--- Begin report of {path_to_file} ---")
            print(f"{cantidad_palabras} words found in the document")
            print("\nCharacter frequencies (alphabet only):")
            for caracter, frecuencia in sorted(cantidad_caracteres.items()):
                print(f"The '{caracter}' character was found {frecuencia} times")
            print("--- End report ---")
    except FileNotFoundError:
        print(f"El archivo '{path_to_file}' no se encontró. Asegúrate de que está en la ubicación correcta.")

# Llamar a la función main
if __name__ == "__main__":
    main()

