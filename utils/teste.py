from falas import carregar_fala as cf

def main():
    lista_de_procura = cf("pesquisar")
    print(lista_de_procura)
    frase = "victor pesquisar por elon musk"

    for procura in lista_de_procura:
        if procura in frase:
            posição = frase.index(procura)

            resultado = frase[posição +len(procura):].split()

            return resultado

    return None
print(main())
