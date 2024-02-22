import math

i = 1
def f(x):
    match i:
        case 1: 
            return x**3
        case 2: 
            return -x**3
        case 3: 
            return math.cos(x)
        case 4: 
            return 3*math.cos(x)
        case 5: 
            return math.sin(x)
        case 6: 
            return 5*math.sin(x)
        case 7: 
            return math.tan(x)
        case 8:
            return (math.e)**((-x**2)/2)

inicio = -5
fim = 5
passo = 0.1

while i <= 8:
    with open(f'fsg_data{i}.csv', 'w') as arquivo_csv:
        arquivo_csv.write("x \t f(x)\n")

        x = inicio
        while x <= fim:
            y = f(x)
            linha = "{:.2f} \t {:.2f}\n".format(x, y)
            arquivo_csv.write(linha)
            x += passo
    i+=1
    print(f"Arquivo csv {i} gerado com sucesso!")
