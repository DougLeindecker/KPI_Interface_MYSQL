import tkinter as tk
import mysql.connector as sql
from tkinter import *
import tentativa1

con = sql.connect(host ='localhost',database='teste',user='root',password=tentativa1.PassEntry.get())

#Conexão do banco de dados
def Conexao(database):
     cursor = con.cursor()
     cursor.execute(f"use {database}")
     print('Conectado com sucesso.')
    


#Criar tabela
def Create(table,entrada):
    cursor = con.cursor()
    cursor.execute(f"create table if not  exists {table}({entrada})")



#dado = Create('teste1','nome varchar(100),cpf char(11)')


#Apagar uma tabela inteira
def Apagar(table):
    cursor = con.cursor()
    cursor.execute(f'drop table {table}')


#Apagar uma linha especifica.
def Apagar_col(table,condicao):
    cursor = con.cursor()
    cursor.execute(f'drop table {table} {condicao}')


#selecionar
def Select(table):
    cursor = con.cursor()
    cursor.execute(f'select * from {table}')


