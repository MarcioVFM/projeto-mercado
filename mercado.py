from typing import List, Dict
from time import sleep

from models.produto import Produto
from util.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    return menu()

def menu() -> None:
    print('================Bem vindo(a) ao SuperMercado==============')

    print('Selecione uma opcao abaixo:')  
    print('1- Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Finalizar pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5: 
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção invalida!')
        menu()



def cadastrar_produto() -> None:
    print('Cadastro de produto')
    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preco do produto: '))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'O produto {nome} com o preco {formata_float_str_moeda(preco)} foi cadastrado!')
    sleep(2)
    menu()

def listar_produtos() -> None:
    print('Lista de produtos:\n=====================')
    if len(produtos) > 0:
        for produto in produtos:
            print(produto)
            print('------------------')
    else:
        print('Ainda nao existem produtos listados')
    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o codigo o produto que deseja adicionar ao carrinho:')
        print('===============Produtos disponivei===============')
        for produto in produtos:
            print(produto)
            print('-----------------------------')
            sleep(1)
        codigo: int = int(input())
        produto: Produto = pegar_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produtod comm o codigo {codigo} nao foi encontrado')
            sleep(2)
            menu()
    else: 
        print('Ainda nao ha produtos cadastrados')
        sleep(2)
        menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho:')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('------------------------')
                sleep(1)
        menu()        

    else:
        print('Ainda nao existem produtos no carrinho')
        sleep(2)
        menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos no carrinho:')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('=================')
                sleep(1)
        print(f'Sua fatura é : {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!') 
        carrinho.clear()
        sleep(3)    
    else: 
        print('Ainda nao ha produtos no carrinho')
        sleep(2)
        menu()


def pegar_produto() -> None:
    pass

def pegar_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()

