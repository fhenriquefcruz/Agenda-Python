import os
import sqlite3
from sqlite3 import Error

# conexão com o banco


def conexaoBanco():
    caminho = "D:\\Agenda-Python\\Banco_SQLite\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


varcon = conexaoBanco()

# DELETE E UPDATE


def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    
      

# SELECT


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res
   

def menuPrincipal():
    # limpando a tela
    os.system("cls")
    # opcoes do menu
    print("O QUE VOCÊ DESEJA FAZER? \n")
    print("1 - ADICIONAR NOVO CONTATO")
    print("2 - EXCLUIR CONTATO")
    print("3 - CONSULTAR CONTATO")
    print("4 - SAIR\n")


def menuInserir():
    os.system("cls")
    print("PREENCHA AS INFORMAÇÕES \n")
    varnome = input("Nome: ")
    vartelefone = input("Telefone: ")
    varemail = input("E-mail: ")
    sql = "INSERT INTO tb_contatos (TXT_NOMECONTATO, TXT_TELEFONECONTATO, TXT_EMAILCONTATO) VALUES ('" + \
        varnome+"','"+vartelefone+"','"+varemail+"')"
    query(varcon, sql)
    os.system("cls")
    print("CONTATO ADICIONADO COM SUCESSO!")
    os.system("pause")

def menuDeletar():
    os.system("cls")
    varid = input("Digite o ID do contato que você deseja excluir: ")
    sql = "DELETE FROM tb_contatos WHERE NUM_IDCONTATO=" + varid
    query(varcon, sql)
    
    os.system("cls")
    print("O CONTATO FOI DELETADO")
    os.system("pause")


def menuconsultar():
    varsql = "SELECT * FROM tb_contatos"
    res = consultar(varcon, varsql)
    vlimite = 10
    vcont = 0
    for r in res:
        print(
            "Nome: {0:<30} Telefone: {1:<14} E-mail: {2:<30} ID: {3:<3}".format(r[0], r[1], r[2], r[3]))
        vcont += 1
        if(vcont >= vlimite):
            vcont = 0
            os.system("pause")
            os.system("cls")
        print("Fim da lista")
    os.system("pause")


opc = 0
while opc != 5:
    menuPrincipal()
    opc = int(input("ESCOLHA UMA OPÇÃO: "))
    if opc == 1:
        menuInserir()
    elif opc == 2:
        menuDeletar()
    elif opc == 3:
        menuconsultar()
    elif opc == 4:
        os.system("cls")
        print("Você saiu")
        os.system("pause")
    else:
        os.system("cls")
        print("OPÇÃO INVÁLIDA")
        os.system("pause")

varcon.close()
os.system("pause")
