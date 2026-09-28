def par_impar(x):
    if x % 2 == 0:
        return True
    else:
        return False

while True:
    try:    
        num = int(input("\nDigite um número: "))
        if par_impar(num):
            print("\nO número %d é par." % num)
            break
        else:
            print("\nO número %d é ímpar." % num)
            break
    except:
        print("Número inválido")
        
####################################

def area(r):
   return 3.14 * r**2

def perimetro(r):
   return 3.14 * 2 * r


while True:
    try: 
        raio = int(input("\nDigite o raio do círculo: "))
        area_raio = area(raio)
        perimetro_raio = perimetro(raio)
    
        print("\nA área do círuculo é: %.2f" % area(raio))
        print("\nO perímetro do círculo é %.2f: " % perimetro(raio))
        break

    except:
       print("Raio inválido")
       
########################################


def equacao(N):
    S = 0
    for t in range(1, N + 1):
        S = S + ((t ** 2) + 1) / (t + 3)
    return S

while True:
    try:
        numero = int(input("Digite um valor inteiro e positivo: "))
        if numero <= 0:
            print("Erro: O número deve ser um número inteiro positivo maior que zero.")
        else:
            resultado = equacao(numero)
            print(f"\nO valor de S para N = {numero} é: {resultado:.4f}")
            break

    except:
        print("Erro: Por favor, digite um número inteiro válido.")
        
        
#############################################
def calcular_fatorial(numero):
    fat = 1
    for i in range(1, numero + 1):
        fat *= i
    return fat


def equacao(N):
    S = 1
    fatorial = 1

    for i in range(1, N + 1):
        fatorial = fatorial * i
        S = S + (1 / fatorial)

    return S

while True:
    try:
        numero = int(input("Digite um valor inteiro e positivo: "))
        if numero <= 0:
            print("Erro: O número deve ser um número inteiro positivo maior que zero.")
        else:
            resultado = equacao(numero)
            print(f"\nO valor de S para N = {numero} é: {resultado:.4f}")
            break

    except:
        print("Erro: Por favor, digite um número inteiro válido.")
        
        
        
##############################################


def somatorio(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

while True:
    try:
        numero = int(input("Digite um número inteiro e positivo: "))

        if numero <= 0:
            print("Erro: O valor digitado deve ser um número positivo maior que zero.")
        else:
            resultado = somatorio(numero)
            print(f"O somatório de 1 até {numero} é: {resultado}")

    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")
        

def analisar_poligono(lados, medida_lado):
    if lados == 3:
        perimetro = lados * medida_lado
        return "TRIÂNGULO | O perímetro é de %d cm." % perimetro

    elif lados == 4:
        area = medida_lado ** 2
        return "QUADRADO | A área é de %.2f cm²." % area
        
    elif lados == 5:
        return "PENTÁGONO"


def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

        
###############################################

def quantidade_divisores(numero):
    contador = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1

    return contador


while True:
    try:
        n = int(input("Digite um número inteiro positivo: "))

        if n > 0:
            print(f"O número {n} possui {quantidade_divisores(n)} divisores.")
            break
        else:
            print("Digite um número inteiro positivo.")
            
    except:
        print("Erro: Digite apenas valores numéricos válidos.")
        
        
#####################


def max(a, b):
    if a > b:
        return a
    else:
        return b


while True:
    try: 
        for i in range(4):
            print(f"\nSérie {i + 1}")

            n1 = int(input("Digite o 1º número: "))
            n2 = int(input("Digite o 2º número: "))
            n3 = int(input("Digite o 3º número: "))
            n4 = int(input("Digite o 4º número: "))

            maior = max(max(n1, n2), max(n3, n4))

            print(f"O maior número é: {maior}")
            break
    except:
        print("\nErro: Digite apenas valores numéricos válidos.")
        
        
###############################


def soma_intervalo(a,b):
    soma = 0
    for i in range(a,b+1):
        soma += i
        return soma

while True:
    try:
        n1 = int(input("\nDigite o primeiro número: "))
        n2 = int(input("\nDigite o segundo número: "))
        if n1 <= n2:
            print("\nA soma do intervalo informado é ", soma_intervalo(n1,n2))
            break
        else:
            print("\nn2 deve ser maior que n1. Digite novamente!")
    except:
        print("\nValor inválido. Digite novamente!")
        
        
###############################

def calcular_cubo(numero):
    return numero ** 3


def ler_caractere():
    while True:
        caractere = input("Deseja continuar? (S/N): ").strip().upper()

        if caractere == 'S' or caractere == 'N':
            return caractere

        print("Caractere inválido. Digite novamente.")


while True:
    try:
        num = float(input("\nDigite um número: "))
        print(f"O cubo de {num} é {calcular_cubo(num):.2f}\n")

        opcao = ler_caractere()

        if opcao == 'N':
            print("Programa encerrado. Até mais!")
            break

    except ValueError:
        print("Erro: Digite apenas números válidos.")


