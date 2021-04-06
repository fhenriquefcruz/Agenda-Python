import os
import sqlite3
from sqlite3 import Error

# Conexão com o banco


def ConexaoBanco():
    caminho = "D:\\Agenda-Python\\Banco_SQLite\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = ConexaoBanco()


def menuPrincipal():
    # limpando a tela
    os.system("cls")
    # opcoes do menu
    print("1 - Inserir Novo Contato")
    print("2 - Deletar Contato")
    print("3 - Atualizar Contato")
    print("4 - Consultar por Nome")
    print("5 - Sair")


def menuInserir():
    print()

def menuDeletar():
    print()

def menuAtualizar():
    print()

def menuConsultar():
    print()


opc = 0
while opc != 5:
    menuPrincipal()
    opc = int(input("Digite uma opção: "))
    if opc == 1:
       menuInserir()
    elif opc == 2:
        menuDeletar()
    elif opc == 3:
        menuAtualizar()
    elif opc == 4:
        menuConsultar()
    elif opc == 6:
        os.system("cls")
        print("Você saiu")
    else:
        os.system("cls")
        print("Opção Inválida")
        os.system("pause")

    os.system("pause")
        
