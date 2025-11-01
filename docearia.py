#Projeto Loja de Doce
#Autor: Matheus Ruivo
#01/11/25
#Vou reformar esse código!
print("Seja Bem-vindo(a) a Doces da Vó Zuleide!")
entrada = input("Digite 'entrar':")
BRIGADEIRO = 5.00
BEIJINHO = 5.00
PALHA_ITALIANA = 8.00

if entrada == 'Entrar' or entrada == 'entrar' or entrada == 'ENTRAR':
    print('Ok, vou te mostrar o menu!')
    menu = input("O MENU ESTÁ AQUI!" \
    "1 - Mostrar lista de doces --"  \
    "2 - Ver preços --" \
    "3 - Fazer pedido --" \
    "4 - Sair --" \
    "Escolha um e digite o número correspondente:")
    if menu == '1' or menu == 1 or menu == 'um':
        print("Carregando...")
        print("Aqui está a Lista---" \
        "--" \
        "1 - Beijinho --" \
        "2 - Brigadeiro --" \
        "3 - Palha Italiana --")

    elif menu == '2' or menu == 2 or menu == 'dois':
        print("Carregando...")
        print("Os preços: --" \
        "1 - Beijinho = 5,00 --" \
        "2 - Brigadeiro = 5,00 --" \
        "3 - Palha Italiana = 8,00 --")
    elif menu == '3' or menu == 3 or menu == 'três':
        print("Carregando...")
        pedido = input("Escolha o produto:")
        if pedido == 'beijinho' or menu == 'Beijinho' or menu == 1:
            print('Preparando...')
            print("Pronto! R$5,00")
            deseja_mais = input("Você deseja mais alguma coisa?")
            #ADD
            if deseja_mais == 'sim' or deseja_mais == 'Sim' or deseja_mais == 's':
                qual = input('Qual produto?')
                if qual == 'Brigadeiro' or qual == 'brigadeiro':
                    soma = BRIGADEIRO + BEIJINHO
                    print(f"O total ficou: {soma}")
                    
                elif qual == 'Palha Italiana' or qual == 'palha italiana':
                    soma2 = BEIJINHO + PALHA_ITALIANA
                    print(f'O total ficou:{soma2}')
                    
            elif deseja_mais == 'Não' or deseja_mais == 'não':
                print("Carregando...")
                print('Ficou R$5,00')
        elif pedido == 'brigadeiro' or pedido == 'Brigadeiro' or pedido == 2:
            print('Preparando...')
            print("Pronto! R$5,00")
            deseja_mais2 = input("Você deseja mais alguma coisa?")
            #ADD
            if deseja_mais2 == 'sim' or deseja_mais2 == 'Sim' or deseja_mais2 == 's':
                qual3 = input('Qual produto?')
                if qual3 == 'Brigadeiro' or qual3 == 'brigadeiro':
                    soma3 = BRIGADEIRO + BEIJINHO
                    print(f"O total ficou: {soma3}")
                    
                elif qual3 == 'Palha Italiana' or qual3 == 'palha italiana':
                    soma4 = BRIGADEIRO + PALHA_ITALIANA
                    print(f'O total ficou:{soma4}')
                    
            elif deseja_mais2 == 'Não' or deseja_mais2 == 'não':
                print("Carregando...")
                print('Ficou R$5,00')
            
        elif pedido == 'Palha Italiana' or pedido == 'palha italiana' or pedido == 3:
            print('Preparando...')
            print("Pronto! R$8,00")
            deseja_mais6 = input("Você deseja mais alguma coisa?")
            #ADD
            if deseja_mais6 == 'sim' or deseja_mais6 == 'Sim' or deseja_mais6 == 's':
                qual6 = input('Qual produto?')
                if qual6 == 'Brigadeiro' or qual6 == 'brigadeiro':
                    soma6 = PALHA_ITALIANA + BEIJINHO
                    print(f"O total ficou: {soma6}")
                    
                elif qual6 == 'Palha Italiana' or qual6 == 'palha italiana':
                    soma7 = BRIGADEIRO + PALHA_ITALIANA
                    print(f'O total ficou:{soma7}')
                    
            elif deseja_mais6 == 'Não' or deseja_mais6 == 'não':
                print("Carregando...")
                print('Ficou R$8,00')
           

    elif menu == '4' or menu == 4 or menu == 'quatro' or menu == 'sair':
        print("Saindo da loja...")
else:
    print("Ops, digite entrar!")