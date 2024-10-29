
def logo():
    print("="*40)
    print(f"{"SENAI":^40}")
    print("="*40)

def menu_principal():
    print("="*40)
    print("""
1 - CADASTRAR FUNCIONARIO
2 - FAZER LOGIN
3 - EXCLUIR CADASTRO
0 - SAIR
""")
    print("="*40)

def limpar_tela():
    from Main import os
    os.system("cls||clear")

def verificando_cpf():
    from Main import Usuario, session
    while True:
        cpf = input("Informe seu CPF: ") 
        funcionario = session.query(Usuario).filter(Usuario.cpf == cpf).first()
        if funcionario is None: 
            break
        else:
            print("CPF já cadastrado")
    return cpf

def cadastro():
    from 
    cpf = verificando_cpf()
    funcionario = Usuario(
        cpf = cpf,
        nome = input("Nome: "),
        sobrenome = input("Sobrenome: "),
        senha = input("Senha: ")
    )
    session.add(funcionario)
    session.commit()

def lanche():
    print("="*40)
    print(f"{"LANCHES":^40}")
    print("="*40)
    print("""
1 - CADASTRAR
2 - VENDA
3 - EXCLUIR
0 - SAIR
""")

def cadastro_lanches():
    lanches = Lanche(
        nome = input("Nome: "),
        preco = float(input("Preço: "))
    )
    session.add(lanches)
    session.commit()

def tabela_lanches():
    lanche = session.query(Lanche).all()
    for a in lanche:
        print(f"{lanche.id} {lanche.nome} {lanche.preco}")

while True:
    limpar_tela()
    logo()
    menu_principal()
    while True:
        opcao = int(input(": "))
        if opcao == 1 or 2 or 3 or 0:
            break
    match opcao:
        case 1:
            while True:
                cadastro()
                while True:
                    opcao1 = int(input("DESEJA EFETUAR CADASTRO DE UM NOVO FUNCIONARIO ? \n1-SIM \n2-NÃO"))
                    if opcao1 == 1 or 2:
                        break
                if opcao1 ==  2:
                    break
        case 2:
            limpar_tela()
            print("="*40)
            print(f"{"LOGIN":^40}")
            print("="*40)
            cpf_login = input("CPF PARA LOGING: ")
            funcionario = session.query(Usuario).filter(Usuario.cpf == cpf_login).first()
            senha_login = input("INSIRA SUA SENHA: ")
            if senha_login == funcionario.senha:
                print("="*40)
                print(f"{"LOGIN EFETUADO COM SUCESSO":^40}")
                print("="*40)
                while True:
                    limpar_tela()
                    logo()
                    lanche()
                    while True:
                        opcao2 = int(input(": "))
                        if opcao2 == 1 or 2 or 3 or 0:
                            break
                    match opcao2:
                        case 1:
                            while True:
                                cadastro_lanches()
                                while True:
                                    opcao3 = int(input("DESEJA CADASTRAR UM ITEM NOVO ? \n1-SIM \n2-NÃO"))
                                    if opcao3 == 1 or 2:
                                        break
                                if opcao3 == 2:
                                    break
        case 3:
            limpar_tela
            logo()
            cpf_login = input("INFORME O CPF DO FUNCIONARO QUE DESEJA EXCLUIR: ")
            funcionario = session.query(Usuario).filter(Usuario.cpf == cpf_login).first()
            session.delete(funcionario)
            session.commit()
            print("FUNCIONARIO DELETADO DA BASE DE DADOS!")
        case 0:
            break