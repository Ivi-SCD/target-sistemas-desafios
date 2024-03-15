def inverter_texto(string):
    texto_invertido = "" 
    for i in range(len(string) - 1, -1, -1):
        texto_invertido += string[i]
    return texto_invertido 

texto = ".O LOBO AMA O BOLO."
texto_invertido = inverter_texto(texto)
print("String original:", texto)
print("String invertida:", texto_invertido)