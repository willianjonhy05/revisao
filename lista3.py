def remover_vogais(s):
    vogais = "aeiouAEIOU"
    s2 = ""
    for i in range(len(s)):
        if s[i] not in vogais:
            s2 += s[i]
        return s2

while True:
    try:
        string = input("Digite a palavra: ")
        print(f"A {string} sem vogais é: {remover_vogais(string)} ")
        break
    except:
        print("Tente novamente!")
        
        
############################



from random import *
max_lista = 10

l= list(range(max_lista))

def grava_lista():
    for i in range(max_lista):
        l[i] = randint(1, 10)

def encontrar_elemento_repetido():
    dic = {}
    for i in l:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    maior_quant = 0
    valor = 0
    for i in dic:
        if dic[i] > maior_quant:
            maior_quant = dic[i]
            valor = i
    return valor, maior_quant



###############################


def quadrado_perfeito(n):
    for i in range(1, n):
        if i * i == n:
            return True
    return False

while True:
    try:
        num = int(input("Digite um número: "))
        if quadrado_perfeito(num):
            print("O número é um quadrado perfeito")
        else:
            print("O número não é um quadrado perfeito")
            break

    except:
        print("Número inválido. Digite novamente")        