import os

def finalizar_app():
    os.system('clear')
    print('Finalizando o app\n')


def exibir_nome_do_programa():
    print(''' 

        EXERCÍCIOS
          


    ''')

def exibir_opcoes():
    print('1. Validar se número que foi inserido é par ou ímpar \n')
    print('2. Descubra a classificação de uma idade \n')


def numero_par_ou_impar():
    numero_digitado = int(input('Digite um número e pressione enter: '))

    if numero_digitado % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar') 


def classificacao_etaria():
    idade_digitada = int(input('Digite a idade que deseja classificar: '))

    if idade_digitada <= 12:
        print('Criança')
    elif idade_digitada >= 18:
        print('Adulto')
    else:
        print('Adolescente')


def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        numero_par_ou_impar()
    elif opcao_escolhida == 2:
        classificacao_etaria()
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
    
if __name__ == '__main__':
    main()
