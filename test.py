def PularLinhas():
    print("\n==============================\n")



meu_dicionario = {"chave1": "Joao", "chave2": "Pedro", "chave3": "Oliveira", "chave4": "Prestupa"}

for chave, valor in meu_dicionario.items():
    print(chave, valor);

PularLinhas()
minha_tupla = (1,2,3,5,6,7,8,9,10)

for numero in minha_tupla:
    print(numero)

PularLinhas()

meu_arranjo = [20.50 , 55.3 , 1.40, 5.5]

for numero in meu_arranjo:
    print(numero)

print("Alterações")
PularLinhas()

len(minha_tupla)

nova_tupla = (11,22)

for i in range (len(minha_tupla)):
    nova_tupla += (minha_tupla[i],)



print(nova_tupla)

PularLinhas()

novo_dicionario = {12: "Doze", 13: "Treze"}

novo_dicionario.update(meu_dicionario)

print(novo_dicionario)


print("Retorna chave")
novo_dicionario.keys()
PularLinhas()
print("Retorna valor")
PularLinhas()
novo_dicionario.values()
print("Retorna itens")
novo_dicionario.items()




