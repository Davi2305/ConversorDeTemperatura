from ConversorDeTemperatura import fahrenheit, celsius
while True:
# Conversor de Temperatura entre C° e F°

    print('\n\t\t\t ----Conversor de Temperatura entre C° e F°----  \n')

    print('1.Fahrenheit')
    print('2.Celsius')
    print('3.Sair')
    op = int(input('\n\tOpção: '))
    if op == 1:
        print('\nFahrenheit\n')

        v1 = int(input('Informe o valor da temperatura em C° : '))

        total = fahrenheit(v1)

        print(f'\n{v1}C° = {total}F°\n')

    elif op == 2:
        print('\nCelsius\n')

        v1 = int(input('Informe o valor da temperatura em F°: '))

        total = celsius(v1)

        print(f'\n{v1}F° = {total}C°\n')

    elif op == 3:
        # Sair do sistema
        print('\nObrigado pela preferência!\n')
        break
    else:
        print(f'\nOpção {op} inválida! \n')