tabuada = [1,2,3,4,5,6,7,8,9,10]
valores_multiplicados = []
for num in tabuada:
    for i in range(1,11):
        valores = num * i
        valores_multiplicados.append([valores])
        
print(valores_multiplicados)