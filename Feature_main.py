from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from dataclasses import dataclass
from os import system
from time import sleep

BD = create_engine("sqlite:///bancodedadosvendas.bd")

Session = sessionmaker(bind=BD)
session = Session()

Base = declarative_base()

@dataclass
class Usuario(Base):
    __tablename__ = "vendas"
    cpf = Column(String,primary_key=True)
    nome = Column(String)
    sobrenome = Column(String)
    senha = Column(String)

@dataclass
class Lanche(Base):
    __tablename__ = "lanches"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    preco = Column(Float)

Base.metadata.create_all(bind=BD)
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
    sleep(5)
    system("cls||clear")

def verificando_cpf():
    while True:
        cpf = input("Informe seu CPF: ") 
        funcionaro = session.query(Usuario).filter(Usuario.cpf == cpf).first()
        if funcionaro is None:  
            break
        else:
            print("CPF já cadastrado")
    return cpf

def cadastro():
    cpf = verificando_cpf()
    
    funcionario = Usuario(
        cpf = cpf,
        nome = input("Nome: "),
        sobrenome = input("Sobrenome: "),
        senha = input("Senha: ")
    )
    session.add(funcionario)
    session.commit()

def lanche ():
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
        print(f"{lanche.id} {lanche.nome}           {lanche.preco}")

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