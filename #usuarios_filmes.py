#usuario_filmes
usuario_filmes = {'joao': 'matrix', 'mario': 'malevola', 'cleber': 'deadpool'}
for a, b in usuario_filmes.items():
    print (f'{a}: {b}')

while True:
    try:
        menu = int(input('1-adicionar filme\n2-Remover filme\n3-ver filmes de um usuario\n4-ver todos os usuarios\n0-sair\nDigite a opcao: '))

        if menu > 4:
            print ('Digite uma opção válida: ')
            break
    except: 
        print (menu)
        
#uso do menu
        match menu:
            case 1:
                us1 = input('digite um nome: ')
                fi1 = input('Digite um filme: ')
                usuario_filmes[(us1)] = (fi1)
                print (usuario_filmes.get(us1))
                print (usuario_filmes)

    

            case 2:
                us2 = input('digite um nome: ')
                if us2 in usuario_filmes:
                    del usuario_filmes[us2]
                    print (usuario_filmes)
    
    
            case 3:
                us3 = input('digite um nome: ')
                print (usuario_filmes.get(us3))

            case 4:
                 print (usuario_filmes.items())
        
            case 0: 
                print ("Encerrando...")  