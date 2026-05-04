import os
import pandas as pd

itens = {    
    "Chave": [],
    "Desc":   [],
    "setor":  [],
    "regiao": []
}

# LIMPAR TELA (FUNCIONA EM QUALQUER SISTEMA)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# ------------------ LOGO -------------------
def logo():
    VERDE = '\033[92m'
    RESET = '\033[0m'
    print(VERDE + r"""
███╗   ███╗███████╗██████╗ ███████╗████████╗ ██████╗  ██████╗██╗  ██╗
████╗ ████║██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██║ ██╔╝
██╔████╔██║█████╗  ██║  ██║███████╗   ██║   ██║   ██║██║     █████╔╝ 
██║╚██╔╝██║██╔══╝  ██║  ██║╚════██║   ██║   ██║   ██║██║     ██╔═██╗ 
██║ ╚═╝ ██║███████╗██████╔╝███████║   ██║   ╚██████╔╝╚██████╗██║  ██╗
╚═╝     ╚═╝╚══════╝╚═════╝ ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝

              S I S T E M A   D E   E Q U I P A M E N T O S
    """ + RESET)


# ------------------ REGISTRO -------------------
def registro():
    limpar_tela()

    while True:
        try:
            NS = int(input('Número de série: '))
            if NS in itens['Chave']:
                print('Esse número já existe!')
                continue
            break
        except ValueError:
            print('Digite apenas números.')

    descricao = input('Equipamento: ').strip()
    setor = input('Setor: ').strip()
    regiao = input('Hospital: ').strip()

    itens['Chave'].append(NS)
    itens['Desc'].append(descricao)
    itens['setor'].append(setor)
    itens['regiao'].append(regiao)

    print("\nEquipamento registrado com sucesso!")

    mostrar_tabela()


# ------------------ MOSTRAR TABELA -------------------
def mostrar_tabela():
    data = {
        "Num.Série": itens['Chave'],
        "Equipamento": itens['Desc'],
        "Local": itens['setor'],
        "Hospital": itens['regiao']
    }
    df = pd.DataFrame(data)
    print("\n=== TABELA DE EQUIPAMENTOS ===")
    print(df)


# ------------------ ENTRADA -------------------
def conferir_nota_fiscal():
    print("\n=== CONFERÊNCIA ===\n")

    for i in range(len(itens['Chave'])):
        print(f"{i+1}. {itens['Desc'][i]} | Série: {itens['Chave'][i]}")

    while True:
        resposta = input('\nA nota fiscal confere? (sim/nao): ').lower()
        if resposta in ['sim', 's']:
            return True
        elif resposta in ['nao', 'não', 'n']:
            return False
        else:
            print("Resposta inválida.")


def mercadorias():
    limpar_tela()

    if not itens['Chave']:
        print("Nenhum equipamento registrado.")
        return

    if conferir_nota_fiscal():
        print("\n✔ Entrada confirmada no sistema.")
        print("Encaminhando para estoque...")
    else:
        print("\n❌ Nota divergente.")
        print("Contatando fornecedor...")


# ------------------ PESQUISA -------------------
def pesquisar():
    limpar_tela()

    try:
        ns = int(input('Digite o número de série: '))
    except ValueError:
        print("Número inválido.")
        return

    if ns in itens['Chave']:
        index = itens['Chave'].index(ns)

        print("\n=== RESULTADO ===")
        print(f"Número: {itens['Chave'][index]}")
        print(f"Equipamento: {itens['Desc'][index]}")
        print(f"Setor: {itens['setor'][index]}")
        print(f"Hospital: {itens['regiao'][index]}")
    else:
        print("Equipamento não encontrado.")


# ------------------ LISTAR -------------------
def listar():
    limpar_tela()

    if not itens['Chave']:
        print("Nenhum equipamento cadastrado.")
    else:
        mostrar_tabela()


# ------------------ MENU -------------------
def menu():
    while True:
        limpar_tela()
        logo()

        print('''===== MENU =====

1 - Registrar equipamento
2 - Entrada de mercadoria
3 - Pesquisar equipamento
4 - Listar todos
0 - Sair
''')

        op = input('Escolha: ')

        if op == '1':
            registro()
        elif op == '2':
            mercadorias()
        elif op == '3':
            pesquisar()
        elif op == '4':
            listar()
        elif op == '0':
            limpar_tela()
            logo()
            print("Sistema encerrado. Até logo!\n")
            break
        else:
            print("Opção inválida.")

        input("\nPressione ENTER para continuar...")


# EXECUTAR
menu()
