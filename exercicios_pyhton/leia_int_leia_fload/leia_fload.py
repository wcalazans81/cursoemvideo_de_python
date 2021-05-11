def leia_Int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferio não digitar esse número.\033[n')
            return 0
        else:
            return n


def leia_Fload(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferio não digitar esse número.\033[n')
            return 0
        else:
            return n


n1 = leia_Int('Digite um Inteiro: ')
n2 = leia_Fload('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
