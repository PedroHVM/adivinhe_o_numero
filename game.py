import random

numero_secreto = random.randint(1, 100)
tentativas = 0
maximo_tentativas = 10

print("Bem-vindo ao jogo Adivinhe o número!")
print(f"O número secreto está entre 1 e 100. Você tem {maximo_tentativas} tentativas para acertar.")

while tentativas < maximo_tentativas:
    tentativas += 1
    palpite = int(input(f"Tentativa {tentativas}: Qual é o seu palpite? "))
    if palpite == numero_secreto:
        print(f"Parabéns, você acertou o número em {tentativas} tentativa(s)!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior. Tente novamente.")
    else:
        print("O número secreto é menor. Tente novamente.")

if tentativas == maximo_tentativas:
    print(f"Fim de jogo! O número secreto era {numero_secreto}. Tente novamente.")
