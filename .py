import sys
#################################################################
print('Bem vindo a Companhia de Logistica Rafael Maia de Assis.')
#################################################################
v_f = False
while True:
    try:
        altura = int(input('Digite a altura (cm) do objeto: '))
        comprimento = int(input('Digite o comprimento (cm) do objeto: '))
        largura = int(input('Digite a largura (cm) do objeto: '))

        volume = altura * largura * comprimento

        valor = 0
        peso = 0
        rota = 0

        print(f'O volume do objeto é: {volume}')

        if volume < 1000:
            valor = 10
        
        elif 1000 <= volume < 10000:
            valor = 20

        elif 10000 <= volume < 30000:
            valor = 30
        
        elif 30000 <= volume < 100000:
            valor = 50

        else:
            print('Não aceitamos objetos com dimensões tão grandes')
            print('Entre com as dimensões desejadas novamente.')
            continue

        v_f = True

    except ValueError:
        print('Você digitou alguma dimensão não númerica')
        print('Por favor entre com as dimensões desejadas novamente.')
        continue
    
    while v_f:
        try:
            qual_peso = int(float(input('Digite o peso do objeto: ')))
            if qual_peso <= 0.1:
                peso = 1

            elif 0.1 <= qual_peso < 1:
                peso = 1.5

            elif 1 <= qual_peso < 10:
                peso = 2

            elif 10 <= qual_peso < 30:
                peso = 3

            else:
                print('Não aceitamos esse peso, tente novamente.')
                continue

            while v_f:
                qual_rota = input(
                    'Selecione a rota:\n'
                    ' BR - De Belo Horizonte para Rio de Janeiro\n'
                    ' BS - De Belo Horizonte para São Paulo\n'
                    ' RB - Do Rio de Janeiro para Belo Horizonte\n'
                    ' RS - Do Rio de Janeiro para São Paulo\n'
                    ' SR - De São Paulo para Rio de janeiro\n'
                    ' SB - De São Paulo para Belo Horizonte\n'
                    '>> '
                    ).lower()
                
                if qual_rota == 'rs':
                    rota = 1
                
                elif qual_rota == 'sr':
                    rota = 1
                
                elif qual_rota == 'bs':
                    rota = 1.2

                elif qual_rota == 'sb':
                    rota = 1.2

                elif qual_rota == 'br':
                    rota = 1.5
                
                elif qual_rota == 'rb':
                    rota = 1.5

                else:
                    print(
                        'Você digitou uma rota que não existe\n'
                        'Por favor entre com a rota desejada novamente'
                    )
                    continue
                
                total = valor * peso * rota
                print(f'Total a pagar(R$): {total}')
                sys.exit()
              

        except ValueError:
            print('Você digitou algum peso do objeto com valor não númerico')
            print('Por favor entre com o peso desejado novamente.')
        
    
