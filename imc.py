# Escreva seu código aqui
print("|--------------------------|")
print("|--Monitoramento de Saúde--|")
nome = input("|digite seu nome: ")
peso = float(input("|digite seu peso: "))
altura = float(input("|digite sua altura: "))
imc = peso / (altura ** 2)
if imc <18.5:  
    print("você esta abaixo do peso")
elif imc <=24.9:
    print("você esta com o peso bom")
elif imc <=29.9:
    print("você esta ficando acima do peso")
elif imc <=34.9:
    print("obesidade de grau 1")  
elif imc <=39.9:
    print("obesidade de grau 2")
else:
    print("obesidade grau 3, procure ajuda de um especialista")




