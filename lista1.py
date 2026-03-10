# Lista de Exercícios (Python) – if e try

# 1.
# Faça uma função em Python que solicite a digitação de dois valores quaisquer,
# informando-os em seguida em ordem crescente.

def ordenar2numerosemcerscente():
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    if num1 < num2:
        print(f"Valores em ordem crescente: {num1}, {num2}")
    else:
        print(f"Valores em ordem crescente: {num2}, {num1}")
# 2.
# Faça uma função em Python que solicite a digitação de três valores quaisquer,
# informando-os em seguida em ordem crescente.

# 3.
# Faça uma função em Python que solicite a digitação de quatro valores quaisquer,
# informando-os em seguida em ordem crescente.

# Conversões de temperatura

# 4.
# Faça uma função em Python que converta temperaturas de Celsius para Fahrenheit.
# A função deve solicitar o valor em Celsius (C).
# Fórmula:
# F = C / 1.8 + 32
# Menor temperatura possível em Celsius: -273.15

# 5.
# Faça uma função em Python que converta temperaturas de Fahrenheit para Celsius.
# A função deve solicitar o valor em Fahrenheit (F).
# Fórmula:
# C = 1.8 × (F − 32)
# Menor temperatura possível em Fahrenheit: -459.67

# 6.
# Faça uma função em Python que converta temperaturas de Celsius para Kelvin.
# Fórmula:
# K = C + 273.15
# Menor temperatura possível em Celsius: -273.15

# 7.
# Faça uma função em Python que converta temperaturas de Kelvin para Celsius.
# Fórmula:
# C = K − 273.15
# Menor temperatura possível em Kelvin: 0

# 8.
# Faça uma função em Python que converta temperaturas de Celsius para Rankine.
# Fórmula:
# R = (C + 491.67) × 1.8
# Menor temperatura possível em Celsius: -273.15

# 9.
# Faça uma função em Python que converta temperaturas de Rankine para Celsius.
# Fórmula:
# C = (R / 1.8) − 491.67
# Menor temperatura possível em Rankine: 0

# 10.
# Faça uma função em Python que converta temperaturas de Fahrenheit para Kelvin.
# Menor temperatura possível em Fahrenheit: -459.67

# 11.
# Faça uma função em Python que converta temperaturas de Kelvin para Fahrenheit.
# Menor temperatura possível em Kelvin: 0

# 12.
# Faça uma função em Python que converta temperaturas de Fahrenheit para Rankine.
# Menor temperatura possível em Fahrenheit: -459.67

# 13.
# Faça uma função em Python que converta temperaturas de Rankine para Fahrenheit.
# Menor temperatura possível em Rankine: 0

# 14.
# Faça uma função em Python que converta temperaturas de Kelvin para Rankine.
# Menor temperatura possível em Kelvin: 0

# 15.
# Faça uma função em Python que converta temperaturas de Rankine para Kelvin.
# Menor temperatura possível em Rankine: 0

# Perímetros

# 16.
# Faça uma função em Python que calcule o perímetro de um triângulo.
# Entradas: lado A, lado B, lado C

# 17.
# Faça uma função em Python que calcule o perímetro de um quadrado/losango.
# Entrada: lado L

# 18.
# Faça uma função em Python que calcule o perímetro de um retângulo/paralelogramo.
# Entradas: lado menor (m) e lado maior (M)

# 19.
# Faça uma função em Python que calcule o perímetro de um trapézio.
# Entradas: lado paralelo menor (m), lado paralelo maior (M) e outro lado (O)

# 20.
# Faça uma função em Python que calcule o perímetro de um polígono regular.
# Entradas: quantidade de lados (Q) e tamanho do lado

# 21.
# Faça uma função em Python que calcule o perímetro de um círculo.
# Entrada: raio (R)
# Fórmula: Perímetro = 2 × π × R
# π ≈ 3.1415

# Áreas

# 22.
# Área de um triângulo
# Entradas: base (B) e altura (A)
# Fórmula: Área = (B × A) / 2

# 23.
# Área de um quadrado
# Entrada: lado (L)
# Fórmula: Área = L²

# 24.
# Área de um retângulo
# Entradas: lado menor (m) e lado maior (M)
# Fórmula: Área = m × M

# 25.
# Área de um losango
# Entradas: diagonal menor (d) e diagonal maior (D)
# Fórmula: Área = (d × D) / 2

# 26.
# Área de um trapézio
# Entradas: base menor (b), base maior (B) e altura (A)
# Fórmula: Área = ((b + B) × A) / 2

# 27.
# Área de um polígono regular
# Entradas: número de lados (Q), base (B) e apótema (A)
# Fórmula: Área = (Q × B × A) / 2

# 28.
# Área de um círculo
# Entrada: raio (R)
# Fórmula: Área = π × R²

# Outros exercícios

# 29.
# Faça uma função que calcule o IMC (Índice de Massa Corporal).
# Entradas: peso (kg) e altura (m)
# Fórmula: IMC = peso / altura²

# 30.
# Faça uma função que resolva uma equação do 1º grau.
# Forma: AX + B = 0
# Entradas: A e B

# Programas com menu

# 31.
# Faça uma função com menu que reúna os exercícios 4 a 15 (conversões de temperatura).

# 32.
# Faça uma função com menu que reúna os exercícios 16 a 21 (perímetros).

# 33.
# Faça uma função com menu que reúna os exercícios 22 a 28 (áreas).

# Validações

# 34.
# Crie uma função que receba horas, minutos e segundos
# e verifique se formam um horário válido.

# 35.
# Crie uma função que receba 3 segmentos de reta
# e verifique se podem formar um triângulo.

# 36.
# Se puder formar um triângulo, classifique:
# Equilátero (3 lados iguais)
# Isósceles (2 lados iguais)
# Escaleno (todos diferentes)

# 37.
# Verifique se 3 ângulos podem formar um triângulo.

# 38.
# Classifique o triângulo pelos ângulos:
# Acutângulo (todos < 90°)
# Retângulo (um = 90°)
# Obtusângulo (um > 90°)

# 39.
# Resolva uma equação do 2º grau:
# ax² + bx + c = 0
# Informar:
# nenhuma raiz
# uma raiz
# duas raízes

# 40.
# Crie uma função que verifique se uma data é válida.
# Entradas: dia, mês, ano
# Considerar meses de 30 e 31 dias, fevereiro e anos bissextos.

# 41.
# Receba um número até 9 e escreva por extenso.
# Exemplo: 5 → cinco

# 42.
# Receba um número até 99 e escreva por extenso.
def n99ToExtenso():
    from num2words import num2words #before, you need to install num2words with pip install num2words
    numero = int(input("Digite um número até 99: "))  
    print(num2words(numero, lang='pt_BR'))
    
# 43.
# Receba um número até 999 e escreva por extenso.
def n999ToExtenso():
    from num2words import num2words 
    numero = int(input("Digite um número até 999: "))  
    print(num2words(numero, lang='pt_BR'))
    
# 44.
# Faça uma função em Python que solicite a digitação de um número natural entre -9 e 9,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.

# 45.
# Faça uma função em Python que solicite a digitação de um número natural entre -99 e 99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.

# 46.
# Faça uma função em Python que solicite a digitação de um número natural entre -999 e 999,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.

# 47.
# Faça uma função em Python que solicite a digitação de um valor monetário entre R$ -9,99 e R$ 9,99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.
# Usar as palavras “real”, “reais”, “centavo” e “centavos” de forma apropriada.
# Não escrever “zero reais” e nem “zero centavos”, exceto no caso do saldo ser igual a zero.

# 48.
# Faça uma função em Python que solicite a digitação de um valor monetário entre R$ -99,99 e R$ 99,99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.
# Usar as palavras “real”, “reais”, “centavo” e “centavos” de forma apropriada.
# Não escrever “zero reais” e nem “zero centavos”, exceto no caso do saldo ser igual a zero.

# 49.
# Faça uma função em Python que solicite a digitação de um valor monetário entre R$ -999,99 e R$ 999,99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.
# Usar as palavras “real”, “reais”, “centavo” e “centavos” de forma apropriada.
# Não escrever “zero reais” e nem “zero centavos”, exceto no caso do saldo ser igual a zero.