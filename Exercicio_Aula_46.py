""" Exercicio
Peça ao usuario para digitar seu nome
Peça ao usuario para digital sua idade
Se nome e idade forem digitados:
    Exiba :
        Seu nome é {nome}
        Seu nome invertido é {nome}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primira letra do seu nome é {letras}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba"Desculpe,você deixou campos vazio."
"""

nome = input ('Digite seu nome : ')
idade = input ('Digite sua idade : ')
if nome and idade:
    print(f' Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f' A primira letra do seu nome é {nome[0]}')
    print(f' A última letra do seu nome é {nome[-1]}')



else:
    print("Desculpe,você deixou campos vazio.")





