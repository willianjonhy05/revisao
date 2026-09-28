from random import randint

max_lista = 100
l = list(range(max_lista))
lista_pares = []
lista_impares = []

def criar_lista():
    for i in range(max_lista):
        l[i] = randint(-100, 100)
        
        
def quantidade_pares_impares():
    pares = 0
    impares = 0
    for i in range(max_lista):
        if l[i] % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    return pares, impares

def gerar_listas_pares_impares():
    for i in range(max_lista):
        if l[i] % 2 == 0:
            lista_pares.append(l[i])
        else:
            lista_impares.append(l[i])
    
    return lista_pares, lista_impares

def maior_elemento():
    maior = l[0]
    for i in range(1, max_lista):
        if l[i] > maior:
            maior = l[i]
    
    return maior

##################################



from random import randint

max_lista = 10
l = list(range(max_lista))

def gravar_lista():
    for i in range(max_lista):
        l[i] = randint(-100, 100)
        
def inverter_lista():
    lista_invertida = []
    for i in range(max_lista):
        lista_invertida.insert(0, l[i])
    return lista_invertida


########################

import random, string


max_lista = 10
caractere = 'A'
l = list(range(max_lista))


def criar_lista():
    global l
    l = random.choices(string.ascii_uppercase, k=max_lista)
        
        
def quantidade_caracteres(caractere):
    quantidade = 0
    for i in range(max_lista):
        if l[i] == caractere:
            quantidade += 1
    return quantidade
        
criar_lista()
print("Lista original:", l)
print(f"Quantidade de '{caractere}': {quantidade_caracteres(caractere)}")


###############################


from random import randint

max_lista = 15
l = list(range(max_lista))

def gravar_lista():
    for i in range(max_lista):
        l[i] = randint(-100, 100)
        
        
def maior_da_lista_e_posicao():
    maior = l[0]
    posicao = 0
    for i in range(max_lista):
        if l[i] > maior:
            maior = l[i]
            posicao = i
            
    return maior, posicao

def menor_da_lista_e_posicao():
    menor = l[0]
    posicao = 0
    for i in range(max_lista):
        if l[i] < menor:
            menor = l[i]
            posicao = i
            
    return menor, posicao
