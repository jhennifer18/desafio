def contar_vogais(palavra):
    palavra = palavra.lower()
    vogais = "aeiou"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador
