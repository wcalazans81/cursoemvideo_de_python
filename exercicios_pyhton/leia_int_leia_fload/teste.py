try:
    a = int(input('digite um valor'))
    b = int(input('di'))
    r = a / b
except (ValueError, TypeError):
    print('Houve um problema com dados digitados!')
except KeyboardInterrupt:
    print('preferio não continuar')

else:
    print(f'o resultado é {r:.2f:}')
finally:
    print('Volte sempre! Muito obrigado!')

