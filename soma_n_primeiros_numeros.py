n = int(input("Número: "))

soma = 0

for i in range(1, n+1):
    soma = soma + i

print(soma)


#soma numeros pares
for i in range(1, n+1, 2):
    soma = soma + i

print(soma)