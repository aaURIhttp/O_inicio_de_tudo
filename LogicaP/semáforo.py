import time
from colorama import init, Back, Fore, Style

init() #inicia a biblioteca

## Variaveis
sinal1 = ['vermelho', 'amarelo', 'verde']
sinal2 = ['verde', 'amarelo', 'vermelho']
ruas = ['Pinheiro Machado','Xv de Novembro']

## Contadores
i = 0
p = 0

## Entrada para ativar o semaforo
ligar = int(input('''  [1] para ativar o sinal 
  [2] para ativar o alerta
'''))

#Inicio do Loop quando 1
if ligar == 1:
    while True:
        print(ruas[0], sinal1[i], ruas[1], sinal2[p])
        print(Fore.RED + "print1")
        print(Back.GREEN + "print1")
        print(Style.BRIGHT + "print1")
        print(Style.RESET_ALL + "teste")

        p = p + 1
        time.sleep(2)
        print(ruas[0], sinal1[i], ruas[1], sinal2[p])
        print("print2")

        i = i + 2 #verde2
        p = p + 1 #vermelho2
        time.sleep(2)
        print(ruas[0], sinal1[i], ruas[1], sinal2[p])
        print("print3")

        i = i - 1 #amarelo 1
        #p = #vermelho 2
        time.sleep(2)
        print(ruas[0], sinal1[i], ruas[1], sinal2[p])
        print("print4")

        i = 0  # verde2
        p = p - 2  # vermelho2
        time.sleep(2)














