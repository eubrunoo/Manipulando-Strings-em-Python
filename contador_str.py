import os

def limpeza():
    os.system('cls')

def obter_inputs():
    limpeza() 
    s = input("Digite uma palavra: ")
    limpeza()
    letra = input("Digite a letra que deseja remover: ")
    return s, letra

def troca(s, letra):
    limpeza()
    novo_s = s.replace(letra, '')
    return novo_s

palavra, letra = obter_inputs()
novo_s = troca(palavra, letra)

def contar_letra(novo_s):
    quantidade_de_letras = 0
    for letra in novo_s:
        if letra.isalpha():
            quantidade_de_letras += 1
    print(f'A nova palavra é {novo_s} e possui {quantidade_de_letras} letras.')

contar_letra(novo_s)
print()