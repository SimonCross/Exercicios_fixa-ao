# 1 - Escreva um programa qque escreva Olá Mundo
"""
print(f"Olá Mundo")

"""""

# 2 - Crie um programa que receba o nome do USUARIO, sua IDADE, seu PESO e imprima os dados na tela
'''
nome = input(f"Fvaor fornecer nome do usúario: ")
idade = int(input(f"Favor fornecer idade do usúario: "))
peso = float(input(f"Favor informar o peso do usuario: "))

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")
'''

# 3 - Crie um programa que recebe o valor e imprime seu sucessor e antecessor na tela
"""

numero = int(input("Digite um numero inteiro : "))

sucessor = numero + 1
antecessor = numero - 1

print(f"O numero digitado foi: {numero}")
print(f"O numero sucessor do numero digitado é: {sucessor}")
print(f"O numero antecessor que foi digitado é: {antecessor}")
print(f"A ordem dos numeros anteriores é {antecessor} {numero} {sucessor}")

"""

# 4 - Crie um programa qque receba um valor e mostre seu dobro, seu triplo e sua raiz quadrada
"""
numero = float(input("Digite um numero: "))
calculo = numero ** 2
calculo2 = numero ** 3
calculo3 = math.sqrt(numero)

print(f"O numero que foi digitado é: {numero}")
print(f"O valor dobrado do numero que foi digitado é {calculo}")
print(f"O valor triplo do numero que foi digitado é {calculo2}")
print(f"A raiz quadrada do numero que foi digitado é {calculo3}")

"""

# 5 - Crie um programa que receba o ano de nascimento do usuario e mostre sua idade
"""

nome = input(f"DIgite seu nome: ")
dia = int(input("Digite o dia de seu nascimento: "))
mes = int(input("Digite o mes que voce nasceu: "))
ano = int(input("Digite o ano de seu nascimento: "))

anoatual = 2024
idade = anoatual - ano

print(f"Nome: {nome}")
print(f"Sua data de nascimento é: {dia}/{mes}/{ano}")
print(f"Sua idade atual é de: {idade} anos")

"""

# 6- Crie um programa que receba o preço de um produto e mostre ele com 25% de descono

"""
produto = str(input("Insira o nome do produto: "))
valor = float(input("Favor cadastrar o preço do produto: "))
desconto = float(input("Favor inserir a % de esconto do produto: "))

calculo = (desconto/100) * valor
total = valor - calculo

print(f"O produto selecionado foi {produto} sendo a porcentagem de ")
print(f"desconto dele {desconto}% sendo o valor do desconto dele de R$: {calculo:.2f}")
print(f"partindo do principio que o valor orginal do produto era R$: {valor} ")
print(f"e o valor atual com o desconto é de R$:{total:.2f}")
"""

# 7 - Faça um programa que receba o salário de um funcionário e calcule ele com 75% de aumento

"""

nome = str(input(f"Favor informar o nome do funcionario: "))
RA = str(input(f"Favor fornecer o RA do funcionario: "))
salario = float(input("Favor fornecer o salário do funcionario R$: "))
aumento = float(input("Favor informar a porcentagem do aumento do salario: "))

bonus = (aumento/100) * salario
salarioAtual = bonus + salario

print(f"Nome: {nome}")
print(f"RA: {RA}")
print(f"Salario: {salario}")

print("\nInformações Atualizadas\n")

print(f"Nome: {nome}")
print(f"RA: {RA}")
print(f"Salario original: {salario:.2f}")
print(f"Bonus: {bonus:.2f}")
print(f"Salario original era R$:{salario:.2f} mais com acrescimo do bonus: {bonus:.2f} ")
print(f"Salario atual: {salarioAtual:.2f}")

"""

"""
# 8 - Faça um programa que leia um numero e faça o calcule da tabuada dele

numero = int(input(f"Favor informar um numero: "))

fim = 10

print(f"A tabuda do numero {numero}\n ")

for contador in range (fim + 1):
    calculo = numero * contador

    print(f"{numero} x {contador} = {calculo}")

"""

# 9 -  Faça um programa que receba dois dados e compare se eles são do mesmo tipo

# parte 1
'''
def comparacao_de_codigo (info1,info2):
    data_info1 = type(info1)
    data_info2 = type(info2)

    if data_info1 == data_info2:

        return True

    else:
        return False

     # parte 2
     
def main():

    try:

        info1 = input(f"digite o primeiro valor para ser comparado: ")
        tipo_info1 = input(f"digite o tipo da varivel que sera utilizado na comparação(exemplo float, int , str, etc): ")
        info1 = eval(tipo_info1)(info1)

        info2 = input(f"digite o segundo valor para ser comparado: ")
        tipo_info2 = input(f"digite o tipo da varivel que sera utilizado na comparação(exemplo float, int , str, etc): ")
        info2 = eval(tipo_info2)(info2)

        return info1,info2

    except:
        print(f"Erro ao converter ao tipo selecionado ")

    return None,None

try:
        info1 , info2 = main()

        if info1 is not None and info2 is not None:

            if comparacao_de_codigo(info1, info2):

                print(f"Os dados {info1} e {info2} são do mesmo tipo")

            els
            
            e:
                     print(f"Os dados {info1} e {info2} são de tipos diferentes")

        else:
                print(f"Os dados não puderam ser convertidos corretamente.")
except Exception as e:

    print(f"Ocorreu um erro durante a execução do programa.")
    '''

# 10 - Crie um programa que leia 4 notas e calcule sua média
"""
def calcular_media_total(nota1, nota2, nota3, nota4):
        media = (nota1+nota2+nota3+nota4)/4
        return media

def main():

        nota1 = float(input(f"Digite a primeira nota: "))
        nota2 = float(input(f"Digite a segunda nota: "))
        nota3 = float(input(f"Figite a terceira nota: "))
        nota4 = float(input(f"Figite a terceira nota: "))

        mediatotal = calcular_media_total(nota1, nota2, nota3,nota4)

        print(f"Sua média atual é : {mediatotal}")

if __name__ == "__main__":
        main()
"""
# 11 - faça a formula que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km

"""
def aluguel_carro(Dias_Alugados, Preço_por_KM):

        P_dia = 60
        KM_p = 0.15

        PT = (P_dia * Dias_Alugados) + (KM_p * Preço_por_KM)

        return PT

def main():

        try:
                Km_q_anda = float(input(f"Digite a quantidade de KM percorridos: "))
                D_Alu = int(input(f"Quantidade de dias alugados: "))

                PT = aluguel_carro(D_Alu,Km_q_anda)

                print(f"O preço total a pagar é R$:{PT:.2f}")
        except ValueError:
                print("Favor informar validos para operação! ")

if __name__ == "__main__":

    main()

"""
"""
# 12 - faça um programa que receba a temperatura em graus celsius e apresente-a convertida em graus fahrenheit
# formula F= C*(9/5)+32

def conversao(Temp_cels):

    Temp_fai = Temp_cels*(9/5)+32

    return Temp_fai

def main():

    try:
        Celsios = int(input(f"favor digite a quantidade de Graus Celsius(entre 0 e 100): "))
        Fairen = conversao(Celsios)
        priznt(f"A temperatura convertida para Fairenhait é {Fairen:.2f}:")

    except ValueError:
        print(f"Favor usar valores que correspondem ao que foi solicitado!.")

if __name__ == "__main__":

        main()

def conversao(Temp_cels):

    Temp_fai = Temp_cels*(9/5)+32

    return Temp_fai

def main():

    try:
        Celsios = int(input(f"favor digite a quantidade de Graus Celsius(entre 0 e 100): "))
        Fairen = conversao(Celsios)
        print(f"A temperatura convertida para Fairenhait é {Fairen:.2f}:")

    except ValueError:
        print(f"Favor usar valores que correspondem ao que foi solicitado!.")

if __name__ == "__main__":

        main()
def conversao(Temp_cels):

    Temp_fai = Temp_cels*(9/5)+32

    return Temp_fai

def main():

    try:
        Celsios = int(input(f"favor digite a quantidade de Graus Celsius(entre 0 e 100): "))
        Fairen = conversao(Celsios)
        print(f"A temperatura convertida para Fairenhait é {Fairen:.2f}:")

    except ValueError:
        print(f"Favor usar valores que correspondem ao que foi solicitado!.")

if __name__ == "__main__":

        main()
"""

"""
# 13 - Faça um progrmama que leia largura e a altura de uma parede em metros
#calcule a sua area e a quantidade de tinta necessaria para pinta-la,sabendo que cada litro de tintapinta uma area de 2 metros quadrados

def Area_Total(largura,altura):

    area_Parede = (largura * altura)

    return area_Parede

def calcular_tinta(Area_tinta, eficacia_tinta):

    quantidade_tinta = Area_tinta/eficacia_tinta

    return quantidade_tinta

def main():

    try:

        largura = float(input(f"Digite a quantidade de metros quadrados para largura: "))
        altura = float(input(f"Digite a quantidade de metros quadrados para altura: "))
        tinta = float(input("Digite a quantidade de litros de tinta: "))

        Qto_area = Area_Total(largura,altura)
        Qt_de_tinta = calcular_tinta(Qto_area,tinta)


        print(f"A area total calculada através dos dados coletados é {Qto_area:.2f} metros")
        print(f"A Quantidade de tinta necessária para cobrir a area de {Qto_area:.2f} é {Qt_de_tinta:.2f}")

    except ValueError:

        print(f"Favor informar a medida em metros ou a quantidade de tinta em litros!.")

if __name__ == "__main__":
    main()

"""

# 14 - Crie um progrmama que receba a idade do usuario e imprima na
# tela quantos meses e dias essa pessoa tem de vida

"""
def programa(idade_meses):

    Idade_Anos = idade_meses // 12
    Meses_Restante = idade_meses % 12
    D_P_Mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    D_restan = sum(D_P_Mes[:Meses_Restante])
    An_Bissex = Idade_Anos // 4
    Ida_Dias = Idade_Anos * 365 + D_restan + An_Bissex

    return Idade_Anos, Ida_Dias

def main():

    try:
        idade_meses = int(input(f"Favor informar idade:"))

        Idade_Anos, Ida_Dias = programa(idade_meses)

        print(f"Você tem aproximadamente {Idade_Anos} anos e {Ida_Dias} dias de vida.")

    except ValueError:

        print(f"Favor inserir os dados corretamente!.")

if __name__ == "__main__":
    main()
"""

# 15 - Faça um programa que calcule a importancia de R$ 780,00 sera dividida entre tres ganhardores
# O 1 lugar ganhara 46% do valor
# O 2 lugar 32 %
# O 3 lugar recebera o rsto
# Calcule e imprima a ania ganha por cada um dos ganhadores

"""
def calculo(total):

    P_lugar = total * 0.46
    S_lugar = total * 0.32
    T_lugar = total * 0.22

    return P_lugar,S_lugar,T_lugar

def main():
    try:
        total = 780
        nome1 = str(input(f"Informar o nome do primeiro colocado do sorteio: "))
        nome2 = str(input(f"Informar o nome do segundo colocado do sorteio: "))
        nome3 = str(input(f"Informar o nome do terceiro colocado do sorteio: "))

        first, second, third = calculo(total)

        print(f"O nome do primeiro colocado é: {nome1} com {first:.2f}")
        print(f"O nome do segundo colocado é: {nome2} com {second:.2f}")
        print(f"O nome do terceiro colocado é: {nome3} com {third:.2f}")

    except ValueError:
            print("Valores incorretos!.")

if __name__ == "__main__":
    main()
"""




