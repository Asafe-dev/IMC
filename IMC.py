import os
import time
while True:
    os.system("clear")
    peso = input("Qual o seu peso?\n")
    if peso == "":
        print("PREENCHER É OBRIGATÓRIO!")
        time.sleep(2)
        continue
    try:
        peso = float(peso)
        break
    except:
        print("\nDIGITE APENAS NÚMEROS!")
        time.sleep(2)
        continue
while True:
    os.system("clear")
    alt = input("Qual a sua altura?\n")
    if alt == "":
        print("PRRENCHER É OBRIGATÓRIO!")
        time.sleep(2)
        continue
    try:
        alt = float(alt)
        break
    except:
        print("\nDIGITE APENAS NÚMEROS!")
        time.sleep(2)
        continue
IMC = peso / (alt ** 2)
print(f"\nSeu IMC é: {IMC:.2f}")
if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 25:
    print("Peso normal")
elif IMC < 30:
    print("Sobrepeso")
elif IMC < 35:
    print("Obesidade grau 1")
elif IMC < 40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")