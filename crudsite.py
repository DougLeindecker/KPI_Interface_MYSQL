'''from calendar import leapdays
import tkinter as tk
import mysql.connector as sql
from tkinter import *
import interface

con = sql.connect(host ='localhost',database='teste',user='root',password='1234')

#Edição, Ler add e update
semana = ''
visitantes = ''
nvisitantes =  ''
sessoes = ''
rejeicao = ''
nrejeicao = ''
leads = ''
clientes = ''
custo = ''
cursor = con.cursor()
comando = f'insert into site (semana,visitantes,nvisitantes,sessoes,rejeicao,nrejeicao,leads,clientes,custo) values({semana},{visitantes},{nvisitantes},{sessoes},{rejeicao},{nrejeicao},{leads},{clientes},{custo})'
cursor.execute(comando)
con.commit()

cursor.close()
con.close()'''

import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("KPI")
        #setting window size
        width=900
        height=900
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry('900x600')
        root.resizable(width=False, height=False)
        root.attributes('-alpha',0.9)
        root.iconbitmap(default=r'C:\Users\Dimit\Desktop\interface\Icons8-Ios7-Data-Flow-Chart.ico')
        #logo = PhotoImage(file=r'C:\Users\Dimit\Desktop\interface\logo.png')
        GLabel_732=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_732["font"] = ft
        GLabel_732["fg"] = "#333333"
        GLabel_732["justify"] = "center"
        GLabel_732["text"] = "semana"
        GLabel_732.place(x=100,y=110,width=70,height=25)

        GLineEdit_906=tk.Entry(root)
        GLineEdit_906["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_906["font"] = ft
        GLineEdit_906["fg"] = "#333333"
        GLineEdit_906["justify"] = "center"
        GLineEdit_906["text"] = ""
        GLineEdit_906.place(x=180,y=110,width=70,height=25)

        GLabel_954=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_954["font"] = ft
        GLabel_954["fg"] = "#333333"
        GLabel_954["justify"] = "center"
        GLabel_954["text"] = "visitantes"
        GLabel_954.place(x=100,y=170,width=70,height=25)

        GLineEdit_170=tk.Entry(root)
        GLineEdit_170["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_170["font"] = ft
        GLineEdit_170["fg"] = "#333333"
        GLineEdit_170["justify"] = "center"
        GLineEdit_170["text"] = ""
        GLineEdit_170.place(x=180,y=170,width=70,height=25)

        GLabel_618=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_618["font"] = ft
        GLabel_618["fg"] = "#333333"
        GLabel_618["justify"] = "center"
        GLabel_618["text"] = "Novos visitantes"
        GLabel_618.place(x=100,y=230,width=70,height=25)

        GLineEdit_418=tk.Entry(root)
        GLineEdit_418["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_418["font"] = ft
        GLineEdit_418["fg"] = "#333333"
        GLineEdit_418["justify"] = "center"
        GLineEdit_418["text"] = ""
        GLineEdit_418.place(x=180,y=230,width=70,height=25)

        GLineEdit_627=tk.Entry(root)
        GLineEdit_627["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_627["font"] = ft
        GLineEdit_627["fg"] = "#333333"
        GLineEdit_627["justify"] = "center"
        GLineEdit_627["text"] = ""
        GLineEdit_627.place(x=180,y=290,width=70,height=25)

        GLabel_748=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_748["font"] = ft
        GLabel_748["fg"] = "#333333"
        GLabel_748["justify"] = "center"
        GLabel_748["text"] = "Sessões"
        GLabel_748.place(x=90,y=290,width=70,height=25)

        GLabel_323=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_323["font"] = ft
        GLabel_323["fg"] = "#333333"
        GLabel_323["justify"] = "center"
        GLabel_323["text"] = "Rejeição"
        GLabel_323.place(x=90,y=340,width=70,height=25)

        GLineEdit_44=tk.Entry(root)
        GLineEdit_44["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_44["font"] = ft
        GLineEdit_44["fg"] = "#333333"
        GLineEdit_44["justify"] = "center"
        GLineEdit_44["text"] = ""
        GLineEdit_44.place(x=180,y=340,width=70,height=25)

        GLabel_643=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_643["font"] = ft
        GLabel_643["fg"] = "#333333"
        GLabel_643["justify"] = "center"
        GLabel_643["text"] = "N_Rejeição"
        GLabel_643.place(x=90,y=390,width=70,height=25)

        GLineEdit_722=tk.Entry(root)
        GLineEdit_722["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_722["font"] = ft
        GLineEdit_722["fg"] = "#333333"
        GLineEdit_722["justify"] = "center"
        GLineEdit_722["text"] = ""
        GLineEdit_722.place(x=180,y=390,width=70,height=25)

        GLabel_202=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_202["font"] = ft
        GLabel_202["fg"] = "#333333"
        GLabel_202["justify"] = "center"
        GLabel_202["text"] = "Leads"
        GLabel_202.place(x=90,y=440,width=70,height=25)

        GLabel_979=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_979["font"] = ft
        GLabel_979["fg"] = "#333333"
        GLabel_979["justify"] = "center"
        GLabel_979["text"] = "Clientes"
        GLabel_979.place(x=90,y=490,width=70,height=25)

        GLabel_970=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_970["font"] = ft
        GLabel_970["fg"] = "#333333"
        GLabel_970["justify"] = "center"
        GLabel_970["text"] = "Custo"
        GLabel_970.place(x=90,y=540,width=70,height=25)

        GLineEdit_403=tk.Entry(root)
        GLineEdit_403["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_403["font"] = ft
        GLineEdit_403["fg"] = "#333333"
        GLineEdit_403["justify"] = "center"
        GLineEdit_403["text"] = ""
        GLineEdit_403.place(x=180,y=440,width=70,height=25)

        GLineEdit_83=tk.Entry(root)
        GLineEdit_83["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_83["font"] = ft
        GLineEdit_83["fg"] = "#333333"
        GLineEdit_83["justify"] = "center"
        GLineEdit_83["text"] = ""
        GLineEdit_83.place(x=180,y=490,width=70,height=25)

        GLineEdit_997=tk.Entry(root)
        GLineEdit_997["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_997["font"] = ft
        GLineEdit_997["fg"] = "#333333"
        GLineEdit_997["justify"] = "center"
        GLineEdit_997["text"] = ""
        GLineEdit_997.place(x=180,y=540,width=70,height=25)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
