import string

def descifrar_cesar(texto, k):
    alfabeto = string.ascii_lowercase
    descifrado = ""
    for c in texto:
        if c in alfabeto:
            idx = (alfabeto.index(c) - k) % 26
            descifrado += alfabeto[idx]
        else:
            descifrado += c
    return descifrado

def detectar_espanol(texto, palabras_comunes):
    texto_lower = texto.lower()
    score = 0
    for palabra in palabras_comunes:
        if palabra in texto_lower:
            score += 1
    return score

def detectar_ingles(texto, palabras_comunes_eng):
    texto_lower = texto.lower()
    score = 0
    for palabra in palabras_comunes_eng:
        if palabra in texto_lower:
            score += 1
    return score

def main():
    texto = """pm fvb aopur aljouvsvnf jhu zvscl fvby zljbypaf
    wyvisltz, aolu fvb kvua buklyzahuk aol wyvisltz
    huk fvb kvua buklyzahuk aol aljouvsvnf.
    --iybjl zjoulply"""

    palabras_comunes = [
        "que", "los", "las", "una", "para", 
        "con", "de", "el", "la", "y", "un", "por"
    ]

    palabras_comunes_eng = [
        "the", "and", "to", "of", "in", "you", "that", "for", "with", "as",
        "be", "on", "is", "are", "this", "it", "was", "he", "she"
    ]

    mejor_k = None
    mejor_score = -1
    mejor_texto = ""
	
    '''
    La respuesta el ejercicio es probar los 26 desplazamientos posibles
    '''
    for k in range(26):
        candidato = descifrar_cesar(texto, k)
        score = detectar_espanol(candidato, palabras_comunes)
        score += detectar_ingles(candidato, palabras_comunes_eng)

        if score > mejor_score:
            mejor_score = score
            mejor_k = k
            mejor_texto = candidato

    print("Mejor desplazamiento encontrado:", mejor_k)
    print("\nTexto probable:\n")
    print(mejor_texto)

if __name__ == '__main__':
    main()

