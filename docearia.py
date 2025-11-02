#Projeto Loja de Doce
#Autor: Matheus Ruivo
#02/11/25
#Código atualizado, mais para frente vou atualizando!

print("Bem-vindo(a) a Doces da Vó Zuleide!")
entrada = input("Digite entrar:")

BRIGADEIRO = 5.00
BEIJINHO = 5.00
PALHA_ITALIANA = 8.00

if entrada == 'entrar' or  entrada == 'Entrar':
     print("Carregando...")
     menu = input("Deseja ver o menu?")
     if menu == 'Sim' or menu == 'sim':
         print('Carregando....')
         print("Aqui está o menu --" \
         "1 - Brigadeiro 5.00 --" \
         "2 - Beijinho 5.00 --" \
         "3 - Palha Italiana 8.00 --")
         fazer_pedido = input("Quer fazer um pedido (encomenda)?")
         if fazer_pedido == 'Sim' or fazer_pedido == 'sim':
             print("Carregando...")
             comprar_doce = input("Qual doce deseja comprar?")
             if comprar_doce == 'Brigadeiro' or comprar_doce == 'brigadeiro':
                 print('Analisando...')
                 mais_alguma_coisas = input("Brigadeiro deu R$5.00 deseja mais alguma coisas? digite o produto (beijinho):")
                 if mais_alguma_coisas == 'Beijinho' or mais_alguma_coisas == 'beijinho':
                     print("Calculando..")
                     soma = BRIGADEIRO + BEIJINHO
                     print(f"O resultado ficou {soma:.2f}")
                     adicionando_mais = input("Quer adicionar mais alguma coisas? (coloque o nome do produto: doce)")
                     if adicionando_mais == 'palha italiana' or adicionando_mais == 'Palha Italiana':
                         print("Carregando...")
                         soma3 = soma + PALHA_ITALIANA
                         print(f'O total ficou {soma3:.2f}.')
                     else:
                         print('Obrigado pela compra! 5.00')
                 elif mais_alguma_coisas == 'Palha Italiana' or mais_alguma_coisas == 'palha italiana':
                     print('Calculando...')
                     soma2 = BRIGADEIRO + PALHA_ITALIANA
                     print(F"O total ficou {soma2:.2f}")
                     adicionando_mais2 = input("Deseja algo mais? (o nome do produto: doce).")
                     if adicionando_mais2 == 'Beijinho' or adicionando_mais2 == 'beijinho':
                         print("Calculando...")
                         soma4 = soma2 + BEIJINHO
                         print(f'O total ficou {soma4:.2f}.')
                     elif adicionando_mais2 == 'Não' or adicionando_mais2 == 'não':
                         print(f'Ok, obrigado pela compra! R${soma2}')
                 elif mais_alguma_coisas == 'Não' or mais_alguma_coisas == 'não':
                     print('Obrigado pela presença! total: 5.00')
             elif comprar_doce == 'Beijinho' or comprar_doce == 'beijinho':
                 print('Analisando...')
                 print('Total 5.00')
                 deseja_algo_mais = input('Deseja algo mais? (nome do produto: doce).')
                 if deseja_algo_mais == 'Brigadeiro' or deseja_algo_mais == 'brigadeiro':
                     print('Calculando...')
                     soma5 = BEIJINHO + BRIGADEIRO
                     print(f"O total ficou {soma5:.2f}.")
                     add_mais = input("Deseja mais alguma coisa? (nome do produto: doce).")
                     if add_mais == 'Palha Italiana' or add_mais == 'palha italiana':
                         print('Carregando...')
                         soma6 = soma5 + PALHA_ITALIANA
                         print(f"O total deu R${soma6}. ")
                     elif add_mais == 'Não' or add_mais == 'não':
                         print(f'Obrigado pela compra! R${soma5}') 
                 elif deseja_algo_mais == 'Palha Italiana' or deseja_algo_mais == 'palha italiana':
                     print('Carregando...')
                     soma8 = BEIJINHO + PALHA_ITALIANA
                     print(f'O total deu R${soma8}.')
                     add_mais2 = input("Deseja mais alguma coisas? (nome do produto: doce).")
                     if add_mais2 == 'Brigadeiro' or add_mais2 == 'brigadeiro':
                         print('Carregando...')
                         soma9 = soma8 + BRIGADEIRO
                         print(f'O total deu R${soma9}.')
                     elif add_mais2 == 'Não' or add_mais2 == 'não':
                         print('Carregando..')
                         print('Obrigado por comprar com nois!')
                 elif deseja_algo_mais == 'Não' or deseja_algo_mais == 'não':
                    print(f'Obrigado, o total deu R${BEIJINHO}.')
             elif comprar_doce == 'Palha Italiana' or comprar_doce == 'palha italiana':
                 print('Analisando...')
                 print('O total R$8.00')
                 deseja_algo_mais3 = input('Você deseja adicionar mais algo? (nome do produto: doce).')
                 if deseja_algo_mais3 == 'Beijinho' or deseja_algo_mais3 == 'beijinho':
                     print('Carregando...')
                     soma10 = PALHA_ITALIANA + BEIJINHO
                     print(f'O resultado ficou R${soma10:.2f}')
                     add_mais4 = input("Deseja algo mais? (nome do produto: doce).")
                     if add_mais4 == 'Brigadeiro' or add_mais4 == 'brigadeiro':
                         print('Analisando..')
                         total = soma10 + BRIGADEIRO
                         print(f'O total ficou R${total:.2f}')
                     elif add_mais4 == 'não' or add_mais4 == 'Não':
                         print('Obrigadopor comprar conosco!')
                 elif deseja_algo_mais3 == 'brigadeiro' or deseja_algo_mais3 == 'Brigadeiro':
                     print('Carregando...')
                     soma11 = PALHA_ITALIANA + BRIGADEIRO
                     print(f'O resultado ficou R${soma11:.2f}')
                     add_mais5 = input("Deseja algo mais? (nome do produto: doce).")
                     if add_mais5 == 'Beijinho' or add_mais5 == 'beijinho':
                         print('Analisando..')
                         total1 = soma11 + BEIJINHO
                         print(f'O total ficou R${total1:.2f}')
                     elif add_mais5 == 'não' or add_mais5 == 'Não':
                         print('Obrigadopor comprar conosco!')
                 elif deseja_algo_mais3 == 'Não' or deseja_algo_mais3 == 'não':
                     print("Obrigado por comprar com nois! total R$8.00")
             else:
                 print('Digite qual doce!')
         elif fazer_pedido == 'Não' or fazer_pedido == 'não':
             print('Carregando...')
             print('Volte sempre!')
         else:
             print("Você digitou alguma coisas errada!")
     elif menu == 'Não' or menu == 'não':
         print("Você não verá o menu.")
     else:
          print("Algo errado!")
else:
    print("Ops, você digitou algo errado!")
    #Não ligue pelo código desorganizado! rsrs
