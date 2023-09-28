
import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento entre 1922 á 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano inválido.")
        except ValueError:
            print("Digite um número válido.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

nome_completo = input("Digite seu nome completo: ")
ano_nascimento = obter_ano_nascimento()
idade = calcular_idade(ano_nascimento)

print(f"Nome: {nome_completo}")
print(f"Idade em 2022: {idade} anos")