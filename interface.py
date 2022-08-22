from distutils.core import setup
import py2exe
from queue import Full
import tkinter as Tk
from tkinter.ttk import Treeview
from turtle import width
import mysql.connector as sql
from tkinter import *
from tkinter import messagebox
import webbrowser
 
#Criação da janela
 
jan = Tk()
jan.title('KPI')
jan.geometry("600x500")
jan.configure(background="black")
jan.resizable(width=False,height=False)
jan.attributes('-alpha',0.9)
jan.iconbitmap(default=r'C:\Users\Dimit\Desktop\interface\Icons8-Ios7-Data-Flow-Chart.ico')
#logo
 
logo = PhotoImage(file=r'C:\Users\Dimit\Desktop\interface\logo.png')
 
# Barra verde
LeftFrame = Frame(jan, width=200, height=600, bg='green',relief='raise')
LeftFrame.pack(side=LEFT)
 
 
LogoLabel = Label(width=450, height=400,image=logo,bg='black')
LogoLabel.place(x=200,y=5)
def Lertudo():
   
    cols = ['semana','visitantes','nvisitantes','sessoes','rejeicao','nrejeicao','leads','clientes','custo','display','novo_display','organico','novo_organico','pago','novo_pago','direta','novo_direta' ,'social','novo_social' ,'email','novo_email','ref','nref','ebook', 'antecipacao','materia','consultoria','contato','ctr','cpc','impressao','conversao','nome']
    root = Toplevel()
    root.geometry('700x700')
    root.title('Dados site')
    tree = Treeview(root,columns=cols,show='headings')
    tree.pack(fill='both',expand=True)
    sbarr = Scrollbar(tree,orient='vertical',command=tree.yview)
    sbarr.pack(side ='right',fill='y')
    hbarr = Scrollbar(tree,orient='horizontal',command=tree.xview)
    hbarr.pack(side ='bottom',fill='x')
    tree.configure(xscrollcommand=sbarr.set)
    tree.configure(yscrollcommand=hbarr.set)

       
    for i in cols:
        tree.column(i,minwidth=0,width=50,anchor='center')
        tree.heading(i,text=i)
        
            
       
    conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
            
    cursor = conexao.cursor()
    comando = f"""select semana,visitantes,nvisitantes,sessoes,rejeicao,nrejeicao,leads,clientes,custo,display,novo_display,organico,novo_organico,pago,novo_pago,direta,novo_direta ,social,novo_social,email,novo_email,ref,nref,ebook, antecipacao,materia,consultoria,contato,ctr,cpc,impressao,conversao,nome  from site

inner join trafego_total
on semana = semana1

inner join trafego_novo
on semana = semana2

inner join conversoes
on semana= semana3

inner join medidas_google
on semana = semana8;"""
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for i in resultado:
        tree.insert("",'end',values=i)
        
        
        
       
        cursor.close()
        conexao.close()
     
# Aba do site 
def Jan_Site():
   
    jan2 = Toplevel(jan)
    jan2.title('Site KPi')
    jan2.geometry('800x600')
    jan2.configure(background="grey")
    jan2.resizable(width=False,height=False)
   
    SemanaLabel = Label(jan2,text='Semana')
    SemanaLabel.place(x = 50, y = 20)
   
    SemanaEntry = Entry(jan2,width=30)
    SemanaEntry.place(x=170,y=20)
 
    VisitantesLabel = Label(jan2,text='Visitantes')
    VisitantesLabel.place(x = 50, y = 50)
 
    VisitantesEntry = Entry(jan2,width=30)
    VisitantesEntry.place(x=170,y=50)
 
    NVisitantesLabel = Label(jan2,text='NVisitantes')
    NVisitantesLabel.place(x = 50, y = 80)
 
    NVisitantesEntry = Entry(jan2,width=30)
    NVisitantesEntry.place(x=170,y=80)
 
 
    SessoesLabel = Label(jan2,text='Sessões')
    SessoesLabel.place(x = 50, y = 110)
 
    SessoesEntry = Entry(jan2,width=30)
    SessoesEntry.place(x=170,y=110)
 
    RejeicaoLabel = Label(jan2,text='Rejeição')
    RejeicaoLabel.place(x = 50, y = 140)
 
    RejeicaoEntry = Entry(jan2,width=30)
    RejeicaoEntry.place(x=170,y=140)
 
    NrejeicaoLabel = Label(jan2,text='Novos users Rejeição')
    NrejeicaoLabel.place(x = 50, y = 170)
 
    NrejeicaoEntry = Entry(jan2,width=30)
    NrejeicaoEntry.place(x=170,y=170)
 
    LeadsLabel = Label(jan2,text='Leads')
    LeadsLabel.place(x = 50, y = 200)
 
    LeadsEntry = Entry(jan2,width=30)
    LeadsEntry.place(x=170,y=200)
 
    ClienteLabel = Label(jan2,text='Clientes')
    ClienteLabel.place(x = 50, y = 230)
 
    ClienteEntry = Entry(jan2,width=30)
    ClienteEntry.place(x=170,y=230)
   
    CustoLabel = Label(jan2,text='Custo')
    CustoLabel.place(x = 50, y = 260)
 
    CustoEntry = Entry(jan2,width=30)
    CustoEntry.place(x=170,y=260)
    
    # Concetar 
    def LerSite():
        cols = ['ID','Semana','Visitantes','Novos visitantes','Sessões','Rejeição','Rejeição novos usuários','Leads','Clientes','Custo']
        root = Toplevel(jan2)
        root.geometry('800x800')
        root.title('Dados site')
        tree = Treeview(root,columns=cols,show='headings')
        tree.pack(fill='both',expand=True)
        sbarr = Scrollbar(tree,orient='vertical',command=tree.yview)
        sbarr.pack(side ='right',fill='both')
        hbarr = Scrollbar(tree,orient='horizontal',command=tree.xview)
        hbarr.pack(side ='bottom',fill='x')
        tree.configure(yscrollcommand=sbarr.set)
        tree.configure(xscrollcommand=hbarr.set)
        
       
        for i in cols:
            tree.column(i,minwidth=0,width=50,anchor='center')
            tree.heading(i,text=i)
        
            
       
        conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
            
        cursor = conexao.cursor()
        comando = f"""select * from site"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            tree.insert("",'end',values=i)
        
        
        
       
        cursor.close()
        conexao.close()
        
        
    
    def jan_UPsite():
        jan_up = Toplevel(jan2)
        jan_up.title('Atualizar - Site')
        jan_up.geometry('800x600')
        jan_up.configure(background="grey")
        jan_up.resizable(width=False,height=False)
 
        SelLabel = Label(jan_up,text='Informe um campo a ser alterado')
        SelLabel.place(x = 50, y = 20)
         
        SelEntry = Entry(jan_up,width=15)
        SelEntry.place(x=50,y=50)
        
        avLabel =  Label(jan_up,text='Informe o ID')
        avLabel.place(x=300,y=20)
        
        avEntry = Entry(jan_up,width=15)
        avEntry.place(x=300,y=50)
       
        nvLabel = Label(jan_up,text='Informe o novo valor')
        nvLabel.place(x=500,y=20)
        nvEntry = Entry(jan_up,width=15)
        nvEntry.place(x=500,y=50)

        
 
        l = Listbox(jan_up,selectmode='single')
       
        l.place(x=50,y=150,width=200,height=200)
        yscrollbar = Scrollbar(l)
        yscrollbar.pack(side = RIGHT, fill = Y)
        selecao =['semana','visitantes','nvisitantes','sessoes','rejeicao','nrejeicao','leads','clientes','custo']
        for i in selecao:
            l.insert(END,i)
        
        def Apagar():
            conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
            
            id = avEntry.get()
            cursor = conexao.cursor()
            comando = f"""delete from site  where  IDsite = "{id}"; """
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo('ok','Apagado com sucesso!')
       
            cursor.close()
            conexao.close()



        def Comando():   
            conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
            Selecionado = SelEntry.get()
            Novo = nvEntry.get()
            id = avEntry.get()
           
            cursor = conexao.cursor()
            comando = f"""update  site set {Selecionado} = "{Novo}" where  IDsite = "{id}"; """
            cursor.execute(comando)
            conexao.commit()

            messagebox.showinfo('ok','Atualizado com sucesso')
       
            cursor.close()
            conexao.close()

            
 
       
       
        bt = Button(jan_up,text='Alterar dados',font={'century gothic',20} , bg='grey',fg='black',command=Comando)
        bt.place(x=250,y=100)

        bt2 = Button(jan_up,text='Apagar(Informe somente o ID)',font={'century gothic',20} , bg='grey',fg='black',command=Apagar)
        bt2.place(x=400,y=100)

        
           
           
 
   
 
    # Adicionar dados no site
    def Add_site():
        conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
        semana = SemanaEntry.get()
        visitantes = VisitantesEntry.get()
        nvisitantes = NVisitantesEntry.get()
        sessoes = SessoesEntry.get()
        rejeicao = RejeicaoEntry.get()
        nrejeicao = NrejeicaoEntry.get()
        leads = LeadsEntry.get()
        clientes = ClienteEntry.get()
        custo = CustoEntry.get()
 
        cursor = conexao.cursor()
        comando = f"""insert into  site (semana,visitantes,nvisitantes,sessoes,rejeicao,nrejeicao,leads,clientes,custo) values("{semana}","{visitantes}","{nvisitantes}","{sessoes}","{rejeicao}","{nrejeicao}","{leads}","{clientes}","{custo}")"""
        cursor.execute(comando)
        conexao.commit()

        messagebox.showinfo('Informação','Dados inseridos com sucesso!')
       
        cursor.close()
        conexao.close()
   
       
 
 
   
   
   
    AddButton = Button(jan2,text='Inserir',font={'century gothic',20} , bg='grey',fg='black',command=Add_site)
    AddButton.place(x=200,y=300)
 
    UpButton = Button(jan2,text='Alterar dados',font={'century gothic',20} , bg='grey',fg='black',command=jan_UPsite)
    UpButton.place(x=300,y=300)

    LerButton = Button(jan2,text='Ler dados',font={'century gothic',20} , bg='grey',fg='black',command=LerSite)
    LerButton.place(x=450,y=300)
 

def Jan_Lik():
    jan3 = Toplevel()
    jan3.title('Linkedin - KPi')
    jan3.geometry('800x600')
    jan3.configure(background="grey")
    jan3.resizable(width=False,height=False)
   
    SemanaLabel = Label(jan3,text='Semana')
    SemanaLabel.place(x = 50, y = 20)
   
    SemanaEntry = Entry(jan3,width=30)
    SemanaEntry.place(x=170,y=20)
 
    VisitantesLabel = Label(jan3,text='Visitantes')
    VisitantesLabel.place(x = 50, y = 50)
 
    VisitantesEntry = Entry(jan3,width=30)
    VisitantesEntry.place(x=170,y=50)
 
    NVisitantesLabel = Label(jan3,text='Novos Visitantes')
    NVisitantesLabel.place(x = 50, y = 80)
 
    NVisitantesEntry = Entry(jan3,width=30)
    NVisitantesEntry.place(x=170,y=80)
 
    GrupoLabel = Label(jan3,text='Grupos')
    GrupoLabel.place(x = 50, y = 110)
 
    GrupoEntry = Entry(jan3,width=30)
    GrupoEntry.place(x=170,y=110)
 
    SegLabel = Label(jan3,text='Seguidores')
    SegLabel.place(x=50,y=140)
   
    SegEntry = Entry(jan3,width=30,)
    SegEntry.place(x=170,y=140)
 
    SiteLabel = Label(jan3,text='Botão site')
    SiteLabel.place(x=50,y=170)
 
    SiteEntry = Entry(jan3,width=30)
    SiteEntry.place(x=170,y=170)
 
 
    GastoLabel = Label(jan3,text='Gastos')
    GastoLabel.place(x=50,y=200)
 
    GastoEntry = Entry(jan3,width=30)
    GastoEntry.place(x=170,y=200)
 
    LeadsLabel = Label(jan3,text='Leads')
    LeadsLabel.place(x=50,y=230)
 
    LeadsEntry = Entry(jan3,width=30)
    LeadsEntry.place(x=170,y=230)

    def LerLink():
        cols = ['ID','semana5','visitas','novos_visitantes','novos_gurpos','novos_seguidores','botao_site','gastos','leads']
        root = Toplevel(jan3)
        root.geometry('800x800')
        root.title('Dados site')
        tree = Treeview(root,columns=cols,show='headings')
        tree.pack(fill='both',expand=True)
        sbarr = Scrollbar(tree,orient='vertical',command=tree.yview)
        sbarr.pack(side ='right',fill='both')
        hbarr = Scrollbar(tree,orient='horizontal',command=tree.xview)
        hbarr.pack(side ='bottom',fill='x')
        tree.configure(yscrollcommand=sbarr.set)
        tree.configure(xscrollcommand=hbarr.set)
        
       
        for i in cols:
            tree.column(i,minwidth=0,width=50,anchor='center')
            tree.heading(i,text=i)
        
            
       
        conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
            
        cursor = conexao.cursor()
        comando = f"""select * from linkedin"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            tree.insert("",'end',values=i)
        
        
        
       
        cursor.close()
        conexao.close()
    
    def jan_UPLink():
        jan_upLink = Toplevel(jan3)
        jan_upLink.title('Atualizar - Linkedin')
        jan_upLink.geometry('800x600')
        jan_upLink.configure(background="grey")
        jan_upLink.resizable(width=False,height=False)
 
        SelLabel = Label(jan_upLink,text='Informe um campo a ser alterado')
        SelLabel.place(x = 50, y = 20)
         
        SelEntry = Entry(jan_upLink,width=15)
        SelEntry.place(x=50,y=50)
        
        avLabel =  Label(jan_upLink,text='Informe o ID')
        avLabel.place(x=300,y=20)
        
        avEntry = Entry(jan_upLink,width=15)
        avEntry.place(x=300,y=50)
       
        nvLabel = Label(jan_upLink,text='Informe o novo valor')
        nvLabel.place(x=500,y=20)
        nvEntry = Entry(jan_upLink,width=15)
        nvEntry.place(x=500,y=50)

        
 
        l = Listbox(jan_upLink,selectmode='single')
       
        l.place(x=50,y=150,width=200,height=200)
        yscrollbar = Scrollbar(l)
        yscrollbar.pack(side = RIGHT, fill = Y)
        selecao =['semana5','visitas,novos_visitantes','novos_gurpos','novos_seguidores','botao_site','gastos','leads']
        for i in selecao:
            l.insert(END,i)
        
        def Apagar():
            conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
            
            id = avEntry.get()
            cursor = conexao.cursor()
            comando = f"""delete from site  where  IDsite = "{id}"; """
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo('ok','Apagado com sucesso!')
       
            cursor.close()
            conexao.close()

          
        def Comando():   
            conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
            Selecionado = SelEntry.get()
            Novo = nvEntry.get()
            id = avEntry.get()
           
            cursor = conexao.cursor()
            comando = f"""update  linkedin set {Selecionado} = "{Novo}" where  IDlink = "{id}"; """
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo('ok','Atualizado com sucesso!')

       
            cursor.close()
            conexao.close()
        bt = Button(jan_upLink,text='Alterar dados',font={'century gothic',20} , bg='grey',fg='black',command=Comando)
        bt.place(x=250,y=100)

        bt2 = Button(jan_upLink,text='Apagar(Informe somente o ID)',font={'century gothic',20} , bg='grey',fg='black',command=Apagar)
        bt2.place(x=400,y=100)
        
           
 
 
    def Add_Link():
        conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
        semana = SemanaEntry.get()
        visitantes = VisitantesEntry.get()
        novos_visitantes = NVisitantesEntry.get()
        novos_grupos = GrupoEntry.get()
        seguidores = SegEntry.get()
        botao_site = SiteEntry.get()
        gastos = GastoEntry.get()
        leads = LeadsEntry.get()
 
        cursor = conexao.cursor()
        comando = f"""insert into linkedin (semana5,visitas,novos_visitantes,novos_gurpos,novos_seguidores,botao_site,gastos,leads) values("{semana}","{visitantes}","{novos_visitantes}","{novos_grupos}","{seguidores}","{botao_site}","{gastos}","{leads}");"""
        cursor.execute(comando)
        conexao.commit()
        messagebox.showinfo('ok','Atualizado com sucesso!')
       
        cursor.close()
        conexao.close()
 
 
 
    AddButton = Button(jan3,text='Inserir',font={'century gothic',20} , bg='grey',fg='black',command=Add_Link)
    AddButton.place(x=200,y=300)

    UpButton = Button(jan3,text='Alterar dados',font={'century gothic',20} , bg='grey',fg='black',command=jan_UPLink)
    UpButton.place(x=300,y=300)

    Lerbt3 = Button(jan3,text='Ler dados do Linkedin',font={'century gothic',20},bg='grey',fg='black',command=LerLink)
    Lerbt3.place(x=450,y=300)
 

def Jan_Insta():
    jan4 = Toplevel()
    jan4.title('Instagra - KPi')
    jan4.geometry('800x600')
    jan4.configure(background="grey")
    jan4.resizable(width=False,height=False)
    #semana4,curtidas,compartilhar,novos_seguidores,visitas_perfil,custo2
 
    SemanaLabel = Label(jan4,text='Semana')
    SemanaLabel.place(x = 50, y = 20)
   
    SemanaEntry = Entry(jan4,width=30)
    SemanaEntry.place(x=170,y=20)
 
    CurtidasLabel = Label(jan4,text='Curtidas')
    CurtidasLabel.place(x = 50, y = 50)
 
    CurtidasEntry = Entry(jan4,width=30)
    CurtidasEntry.place(x=170,y=50)
 
    CompLabel = Label(jan4,text='Compartilhar')
    CompLabel.place(x = 50, y = 80)
 
    CompEntry = Entry(jan4,width=30)
    CompEntry.place(x=170,y=80)
 
    SegLabel = Label(jan4,text='Seguidores')
    SegLabel.place(x = 50, y = 110)
 
    SegEntry = Entry(jan4,width=30)
    SegEntry.place(x=170,y=110)
 
    PerfLabel = Label(jan4,text='Visitas ao perfil')
    PerfLabel.place(x=50,y=140)
   
    PerfEntry = Entry(jan4,width=30,)
    PerfEntry.place(x=170,y=140)
 
    CustoLabel = Label(jan4,text='Custo')
    CustoLabel.place(x=50,y=170)
   
    CustoEntry = Entry(jan4,width=30,)
    CustoEntry.place(x=170,y=170)

    def LerInsta():
        cols = ['ID','semana4','curtidas','compartilhar','novos_seguidores','visitas_perfil','custo2']
        root = Toplevel(jan4)
        root.geometry('800x800')
        root.title('Dados site')
        tree = Treeview(root,columns=cols,show='headings')
        tree.pack(fill='both',expand=True)
        sbarr = Scrollbar(tree,orient='vertical',command=tree.yview)
        sbarr.pack(side ='right',fill='both')
        hbarr = Scrollbar(tree,orient='horizontal',command=tree.xview)
        hbarr.pack(side ='bottom',fill='x')
        tree.configure(yscrollcommand=sbarr.set)
        tree.configure(xscrollcommand=hbarr.set)
        
       
        for i in cols:
            tree.column(i,minwidth=0,width=50,anchor='center')
            tree.heading(i,text=i)
        
            
       
        conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
            
        cursor = conexao.cursor()
        comando = f"""select * from instagram"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            tree.insert("",'end',values=i)
        
        
        
       
        cursor.close()
        conexao.close()

   
    
    def UpInsta():
        jan_upinsta = Toplevel(jan4)
        jan_upinsta.title('Atualizar - Instagram')
        jan_upinsta.geometry('800x600')
        jan_upinsta.configure(background="grey")
        jan_upinsta.resizable(width=False,height=False)
 
        SelLabel = Label(jan_upinsta,text='Informe um campo a ser alterado')
        SelLabel.place(x = 50, y = 20)
         
        SelEntry = Entry(jan_upinsta,width=15)
        SelEntry.place(x=50,y=50)
        
        avLabel =  Label(jan_upinsta,text='Informe o ID')
        avLabel.place(x=300,y=20)
        
        avEntry = Entry(jan_upinsta,width=15)
        avEntry.place(x=300,y=50)
       
        nvLabel = Label(jan_upinsta,text='Informe o novo valor')
        nvLabel.place(x=500,y=20)
        nvEntry = Entry(jan_upinsta,width=15)
        nvEntry.place(x=500,y=50)

        
 
        l = Listbox(jan_upinsta,selectmode='single')
       
        l.place(x=50,y=150,width=200,height=200)
        yscrollbar = Scrollbar(l)
        yscrollbar.pack(side = RIGHT, fill = Y)
        selecao =['semana4','curtidas','compartilhar','novos_seguidores','visitas_perfil','custo2']
        for i in selecao:
            l.insert(END,i)
        

        def Apagar():
            conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
            
            id = avEntry.get()
            cursor = conexao.cursor()
            comando = f"""delete from instagram  where  IDinsta = "{id}"; """
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo('ok','Apagado com sucesso!')
       
            cursor.close()

        def Comando():   
            conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
            Selecionado = SelEntry.get()
            Novo = nvEntry.get()
            id = avEntry.get()
           
            cursor = conexao.cursor()
            comando = f"""update  instagram set {Selecionado} = "{Novo}" where  IDinsta = "{id}"; """
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo('ok','Atualizado com sucesso!')
       
            cursor.close()
            conexao.close()

        
        bt = Button(jan_upinsta,text='Alterar dados',font={'century gothic',20} , bg='grey',fg='black',command=Comando)
        bt.place(x=250,y=100)
        
        bt2 = Button(jan_upinsta,text='Apagar(Informe somente o ID)',font={'century gothic',20} , bg='grey',fg='black',command=Apagar)
        bt2.place(x=400,y=100)
           
 
    
    
    def Add_insta():
       
        conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
        semana = SemanaEntry.get()
        curtidas= CurtidasEntry.get()
        comp = CompEntry.get()
        seguidores = SegEntry.get()
        perfil = PerfEntry.get()
        custo = CustoEntry.get()
       
 
        cursor = conexao.cursor()
        comando = f"""insert into instagram (semana4,curtidas,compartilhar,novos_seguidores,visitas_perfil,custo2 ) values("{semana}","{curtidas}","{comp}","{seguidores}","{perfil}","{custo}");"""
        cursor.execute(comando)
        conexao.commit()
        messagebox.showinfo('Inserido com sucesso!')
       
        cursor.close()
        conexao.close()
 
    AddButton = Button(jan4,text='Inserir',font={'century gothic',20} , bg='grey',fg='black',command=Add_insta)
    AddButton.place(x=200,y=300)

    UpButton = Button(jan4,text='Alterar dados',font={'century gothic',20} , bg='grey',fg='black',command=UpInsta)
    UpButton.place(x=300,y=300)
    Lerbt3 = Button(jan4,text='Ler dados do Instagram',font={'century gothic',20},bg='grey',fg='black',command=LerInsta)
    Lerbt3.place(x=450,y=300)   
 
 
def Jan_Goo():
    jan5 = Toplevel()
    jan5.title('Google - KPi')
    jan5.geometry('800x600')
    jan5.configure(background="grey")
    jan5.resizable(width=False,height=False)
 
   
    SemanaLabel = Label(jan5,text='Semana')
    SemanaLabel.place(x = 50, y = 20)
   
    SemanaEntry = Entry(jan5,width=30)
    SemanaEntry.place(x=170,y=20)
 
    CtrLabel = Label(jan5,text='CTR')
    CtrLabel.place(x = 50, y = 50)
 
    CtrEntry = Entry(jan5,width=30)
    CtrEntry.place(x=170,y=50)
 
    CPCLabel = Label(jan5,text='CPC')
    CPCLabel.place(x = 50, y = 80)
 
    CPCEntry = Entry(jan5,width=30)
    CPCEntry.place(x=170,y=80)
 
    CustoLabel = Label(jan5,text='Custo')
    CustoLabel.place(x = 50, y = 110)
   
    CustoEntry = Entry(jan5,width=30)
    CustoEntry.place(x=170,y=110)
 
    ImpLabel = Label(jan5,text='Impressão')
    ImpLabel.place(x = 50, y = 140)
   
    ImpEntry = Entry(jan5,width=30)
    ImpEntry.place(x=170,y=140)
 
    ConversaoLabel = Label(jan5,text='Conversao')
    ConversaoLabel.place(x = 50, y = 170)
 
    ConversaoEntry = Entry(jan5,width=30)
    ConversaoEntry.place(x=170,y=170)
 
    NomeLabel = Label(jan5,text='Nome')
    NomeLabel.place(x = 50, y = 200)
 
    NomeEntry = Entry(jan5,width=30)
    NomeEntry.place(x=170,y=200)

    def LerGo():
        cols = ['ID','semana8','ctr','cpc','custo3','impressao','conversao','nome']
        root = Toplevel(jan5)
        root.geometry('800x800')
        root.title('Dados site')
        tree = Treeview(root,columns=cols,show='headings')
        tree.pack(fill='both',expand=True)
        sbarr = Scrollbar(tree,orient='vertical',command=tree.yview)
        sbarr.pack(side ='right',fill='both')
        hbarr = Scrollbar(tree,orient='horizontal',command=tree.xview)
        hbarr.pack(side ='bottom',fill='x')
        tree.configure(yscrollcommand=sbarr.set)
        tree.configure(xscrollcommand=hbarr.set)
        
       
        for i in cols:
            tree.column(i,minwidth=0,width=50,anchor='center')
            tree.heading(i,text=i)
        
            
       
        conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
            
        cursor = conexao.cursor()
        comando = f"""select * from medidas_google"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            tree.insert("",'end',values=i)
        
        
        
       
        cursor.close()
        conexao.close()


 
    def Upgoo():
        jan_upgo = Toplevel(jan5)
        jan_upgo.title('Atualizar - Google')
        jan_upgo.geometry('800x600')
        jan_upgo.configure(background="grey")
        jan_upgo.resizable(width=False,height=False)
 
        SelLabel = Label(jan_upgo,text='Informe um campo a ser alterado')
        SelLabel.place(x = 50, y = 20)
         
        SelEntry = Entry(jan_upgo,width=15)
        SelEntry.place(x=50,y=50)
        
        avLabel =  Label(jan_upgo,text='Informe o ID')
        avLabel.place(x=300,y=20)
        
        avEntry = Entry(jan_upgo,width=15)
        avEntry.place(x=300,y=50)
       
        nvLabel = Label(jan_upgo,text='Informe o novo valor')
        nvLabel.place(x=500,y=20)
        nvEntry = Entry(jan_upgo,width=15)
        nvEntry.place(x=500,y=50)

        
 
        l = Listbox(jan_upgo,selectmode='single')
       
        l.place(x=50,y=150,width=200,height=200)
        yscrollbar = Scrollbar(l)
        yscrollbar.pack(side = RIGHT, fill = Y)
        selecao =['semana8','ctr','cpc','custo3','impressao','conversao','nome']
        for i in selecao:
            l.insert(END,i)
          
        def Apagar():
            conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
            
            id = avEntry.get()
            cursor = conexao.cursor()
            comando = f"""delete from medidas_google  where  IDmg = "{id}"; """
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo('ok','Apagado com sucesso!')
       
            cursor.close()
            conexao.close()

        def Comando():   
            conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
            Selecionado = SelEntry.get()
            Novo = nvEntry.get()
            id = avEntry.get()
           
            cursor = conexao.cursor()
            comando = f"""update  medidas_google set {Selecionado} = "{Novo}" where  IDmg = "{id}"; """
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo('ok','Atualizado com sucesso!')
       
            cursor.close()
            conexao.close()

        bt = Button(jan_upgo,text='Alterar dados',font={'century gothic',20} , bg='grey',fg='black',command=Comando)
        bt.place(x=250,y=100)

        bt2 = Button(jan_upgo,text='Apagar(Informe somente o ID)',font={'century gothic',20} , bg='grey',fg='black',command=Apagar)
        bt2.place(x=400,y=100)
           
 
    
    def Add_google():
        conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
        semana = SemanaEntry.get()
        ctr = CtrEntry.get()
        cpc= CPCEntry.get()
        custo = CustoEntry.get()
        impressao = ImpEntry.get()
        conversao   = ConversaoEntry.get()
        nome = NomeEntry.get()
       
 
        cursor = conexao.cursor()
        comando = f"""insert into medidas_google (semana8,ctr,cpc,custo3,impressao,conversao,nome) values("{semana}","{ctr}","{cpc}","{custo}","{impressao}","{conversao}","{nome}");"""
        cursor.execute(comando)
        conexao.commit()
        messagebox.showinfo('ok','Inserido com sucesso!')
       
        cursor.close()
        conexao.close()


  



    AddButton = Button(jan5,text='Inserir',font={'century gothic',20} , bg='grey',fg='black',command=Add_google)
    AddButton.place(x=200,y=300)
    UpButton = Button(jan5,text='Alterar dados',font={'century gothic',20} , bg='grey',fg='black',command=Upgoo)
    UpButton.place(x=300,y=300)
    Lergobt3 = Button(jan5,text='Ler dados do Google',font={'century gothic',20},bg='grey',fg='black',command=LerGo)
    Lergobt3.place(x=450,y=300)   

def jan_tt():
   
    jantf = Toplevel(jan)
    jantf.title('Trafego Total - KPi')
    jantf.geometry('800x600')
    jantf.configure(background="grey")
    jantf.resizable(width=False,height=False)
   
    SemanaLabel = Label(jantf,text='Semana')
    SemanaLabel.place(x = 50, y = 20)
   
    SemanaEntry = Entry(jantf,width=30)
    SemanaEntry.place(x=170,y=20)
 
    DisplayLabel = Label(jantf,text='Display')
    DisplayLabel.place(x = 50, y = 50)
 
    DisplayEntry = Entry(jantf,width=30)
    DisplayEntry.place(x=170,y=50)

    OrganicaLabel = Label(jantf,text='Organico')
    OrganicaLabel.place(x = 50, y = 80)
 
    OrganicaEntry = Entry(jantf,width=30)
    OrganicaEntry.place(x=170,y=80)
 
    PagaLabel = Label(jantf,text='Paga')
    PagaLabel.place(x = 50, y = 110)
 
    PagaEntry = Entry(jantf,width=30)
    PagaEntry.place(x=170,y=110)
 
 
    DiretaLabel = Label(jantf,text='Direta')
    DiretaLabel.place(x = 50, y = 140)
 
    DiretaEntry = Entry(jantf,width=30)
    DiretaEntry.place(x=170,y=140)
 
    SocialLabel = Label(jantf,text='Social')
    SocialLabel.place(x = 50, y = 170)
 
    SocialEntry = Entry(jantf,width=30)
    SocialEntry.place(x=170,y=170)
 
    EmailLabel = Label(jantf,text='Email')
    EmailLabel.place(x = 50, y = 200)
 
    EmailEntry = Entry(jantf,width=30)
    EmailEntry.place(x=170,y=200)
 
    RefLabel = Label(jantf,text='Referência')
    RefLabel.place(x = 50, y = 230)

    RefEntry = Entry(jantf,width=30)
    RefEntry.place(x = 170,y=230)
 
    
    
    # Concetar 
    def LerTf():
        cols = ['ID','Semana','display','organico' ,'pago','direta' ,'social' ,'email','ref']
        root = Toplevel(jantf)
        root.geometry('800x800')
        root.title('Dados site')
        tree = Treeview(root,columns=cols,show='headings')
        tree.pack(fill='both',expand=True)
        sbarr = Scrollbar(tree,orient='vertical',command=tree.yview)
        sbarr.pack(side ='right',fill='both')
        hbarr = Scrollbar(tree,orient='horizontal',command=tree.xview)
        hbarr.pack(side ='bottom',fill='x')
        tree.configure(yscrollcommand=sbarr.set)
        tree.configure(xscrollcommand=hbarr.set)
        
       
        for i in cols:
            tree.column(i,minwidth=0,width=50,anchor='center')
            tree.heading(i,text=i)
        
            
       
        conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
            
        cursor = conexao.cursor()
        comando = f"""select * from trafego_total"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            tree.insert("",'end',values=i)
        
        
        
       
        cursor.close()
        conexao.close()
        
        
    
    def jan_UPtf():
        jan_up = Toplevel(jantf)
        jan_up.title('Atualizar - Trafego novo')
        jan_up.geometry('800x600')
        jan_up.configure(background="grey")
        jan_up.resizable(width=False,height=False)
 
        SelLabel = Label(jan_up,text='Informe um campo a ser alterado')
        SelLabel.place(x = 50, y = 20)
         
        SelEntry = Entry(jan_up,width=15)
        SelEntry.place(x=50,y=50)
        
        avLabel =  Label(jan_up,text='Informe o ID')
        avLabel.place(x=300,y=20)
        
        avEntry = Entry(jan_up,width=15)
        avEntry.place(x=300,y=50)
       
        nvLabel = Label(jan_up,text='Informe o novo valor')
        nvLabel.place(x=500,y=20)
        nvEntry = Entry(jan_up,width=15)
        nvEntry.place(x=500,y=50)

        
 
        l = Listbox(jan_up,selectmode='single')
       
        l.place(x=50,y=150,width=200,height=200)
        yscrollbar = Scrollbar(l)
        yscrollbar.pack(side = RIGHT, fill = Y)
        selecao =['ID','Semana','display','organico' ,'pago','direta' ,'social' ,'email','ref']
        for i in selecao:
            l.insert(END,i)
        
        def Apagar():
            conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
            
            id = avEntry.get()
            cursor = conexao.cursor()
            comando = f"""delete from trafego_total  where  IDtt = "{id}"; """
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo('ok','Apagado com sucesso!')
       
            cursor.close()
            conexao.close()



        def Comando():   
            conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
            Selecionado = SelEntry.get()
            Novo = nvEntry.get()
            id = avEntry.get()
           
            cursor = conexao.cursor()
            comando = f"""update  trafego_total set {Selecionado} = "{Novo}" where  ID_tt = "{id}"; """
            cursor.execute(comando)
            conexao.commit()

            messagebox.showinfo('ok','Atualizado com sucesso')
       
            cursor.close()
            conexao.close()

            
 
       
       
        bt = Button(jan_up,text='Alterar dados',font={'century gothic',20} , bg='grey',fg='black',command=Comando)
        bt.place(x=250,y=100)

        bt2 = Button(jan_up,text='Apagar(Informe somente o ID)',font={'century gothic',20} , bg='grey',fg='black',command=Apagar)
        bt2.place(x=400,y=100)

        
           
           
 
   
 
    # Adicionar dados no site
    def Add_tt():
        conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
        semana = SemanaEntry.get()
        Display = DisplayEntry.get()
        Organica = OrganicaEntry.get()
        Paga = PagaEntry.get()
        Direta = DiretaEntry.get()
        Social = SocialEntry.get()
        Email = EmailEntry.get()
        Ref = RefEntry.get()
        
 
        cursor = conexao.cursor()
        comando = f"""insert into  trafego_total (semana1,display,organico ,pago,direta ,social ,email,ref) values("{semana}","{Display}","{Organica}","{Paga}","{Direta}","{Social}","{Email}","{Ref}")"""
        cursor.execute(comando)
        conexao.commit()

        messagebox.showinfo('Informação','Dados inseridos com sucesso!')
       
        cursor.close()
        conexao.close()
   
       
 
 
   
   
   
    AddButton = Button(jantf,text='Inserir',font={'century gothic',20} , bg='grey',fg='black',command=Add_tt)
    AddButton.place(x=200,y=300)
 
    UpButton = Button(jantf,text='Alterar dados',font={'century gothic',20} , bg='grey',fg='black',command=jan_UPtf)
    UpButton.place(x=300,y=300)

    LerButton = Button(jantf,text='Ler dados',font={'century gothic',20} , bg='grey',fg='black',command=LerTf)
    LerButton.place(x=450,y=300)
 

def jan_tn():
   
    jantn = Toplevel(jan)
    jantn.title('Trafego Total - KPi')
    jantn.geometry('800x600')
    jantn.configure(background="grey")
    jantn.resizable(width=False,height=False)
   
    SemanaLabel = Label(jantn,text='Semana')
    SemanaLabel.place(x = 50, y = 20)
   
    SemanaEntry = Entry(jantn,width=30)
    SemanaEntry.place(x=170,y=20)
 
    DisplayLabel = Label(jantn,text='Display')
    DisplayLabel.place(x = 50, y = 50)
 
    DisplayEntry = Entry(jantn,width=30)
    DisplayEntry.place(x=170,y=50)

    OrganicaLabel = Label(jantn,text='Organico')
    OrganicaLabel.place(x = 50, y = 80)
 
    OrganicaEntry = Entry(jantn,width=30)
    OrganicaEntry.place(x=170,y=80)
 
    PagaLabel = Label(jantn,text='Paga')
    PagaLabel.place(x = 50, y = 110)
 
    PagaEntry = Entry(jantn,width=30)
    PagaEntry.place(x=170,y=110)
 
 
    DiretaLabel = Label(jantn,text='Direta')
    DiretaLabel.place(x = 50, y = 140)
 
    DiretaEntry = Entry(jantn,width=30)
    DiretaEntry.place(x=170,y=140)
 
    SocialLabel = Label(jantn,text='Social')
    SocialLabel.place(x = 50, y = 170)
 
    SocialEntry = Entry(jantn,width=30)
    SocialEntry.place(x=170,y=170)
 
    EmailLabel = Label(jantn,text='Email')
    EmailLabel.place(x = 50, y = 200)
 
    EmailEntry = Entry(jantn,width=30)
    EmailEntry.place(x=170,y=200)
 
    RefLabel = Label(jantn,text='Referência')
    RefLabel.place(x = 50, y = 230)

    RefEntry = Entry(jantn,width=30)
    RefEntry.place(x = 170,y=230)
 
    
    
    # Concetar 
    def LerTf():
        cols = ['ID','Semana','display','organico' ,'pago','direta' ,'social' ,'email','ref']
        root = Toplevel(jantn)
        root.geometry('800x800')
        root.title('Trafego total')
        tree = Treeview(root,columns=cols,show='headings')
        tree.pack(fill='both',expand=True)
        sbarr = Scrollbar(tree,orient='vertical',command=tree.yview)
        sbarr.pack(side ='right',fill='both')
        hbarr = Scrollbar(tree,orient='horizontal',command=tree.xview)
        hbarr.pack(side ='bottom',fill='x')
        tree.configure(yscrollcommand=sbarr.set)
        tree.configure(xscrollcommand=hbarr.set)
        
       
        for i in cols:
            tree.column(i,minwidth=0,width=50,anchor='center')
            tree.heading(i,text=i)
        
            
       
        conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
            
        cursor = conexao.cursor()
        comando = f"""select * from trafego_novo"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            tree.insert("",'end',values=i)
        
        
        
       
        cursor.close()
        conexao.close()
        
        
    
    def jan_UPtf():
        jan_up = Toplevel(jantn)
        jan_up.title('Atualizar - Trafego novo')
        jan_up.geometry('800x600')
        jan_up.configure(background="grey")
        jan_up.resizable(width=False,height=False)
 
        SelLabel = Label(jan_up,text='Informe um campo a ser alterado')
        SelLabel.place(x = 50, y = 20)
         
        SelEntry = Entry(jan_up,width=15)
        SelEntry.place(x=50,y=50)
        
        avLabel =  Label(jan_up,text='Informe o ID')
        avLabel.place(x=300,y=20)
        
        avEntry = Entry(jan_up,width=15)
        avEntry.place(x=300,y=50)
       
        nvLabel = Label(jan_up,text='Informe o novo valor')
        nvLabel.place(x=500,y=20)
        nvEntry = Entry(jan_up,width=15)
        nvEntry.place(x=500,y=50)

        
 
        l = Listbox(jan_up,selectmode='single')
       
        l.place(x=50,y=150,width=200,height=200)
        yscrollbar = Scrollbar(l)
        yscrollbar.pack(side = RIGHT, fill = Y)
        selecao =['ID','semana2','novo_display','novo_organico' ,'novo_pago','novo_direta' ,'novo_social' ,'novo_email','nref']
        for i in selecao:
            l.insert(END,i)
        
        def Apagar():
            conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
            
            id = avEntry.get()
            cursor = conexao.cursor()
            comando = f"""delete from trafego_novo  where  IDtt = "{id}"; """
            cursor.execute(comando)
            conexao.commit()
            messagebox.showinfo('ok','Apagado com sucesso!')
       
            cursor.close()
            conexao.close()



        def Comando():   
            conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
            Selecionado = SelEntry.get()
            Novo = nvEntry.get()
            id = avEntry.get()
           
            cursor = conexao.cursor()
            comando = f"""update  trafego_novo set {Selecionado} = "{Novo}" where  ID_tn = "{id}"; """
            cursor.execute(comando)
            conexao.commit()

            messagebox.showinfo('ok','Atualizado com sucesso')
       
            cursor.close()
            conexao.close()

            
 
       
       
        bt = Button(jan_up,text='Alterar dados',font={'century gothic',20} , bg='grey',fg='black',command=Comando)
        bt.place(x=250,y=100)

        bt2 = Button(jan_up,text='Apagar(Informe somente o ID)',font={'century gothic',20} , bg='grey',fg='black',command=Apagar)
        bt2.place(x=400,y=100)

        
           
           
 
   
 
    # Adicionar dados no site
    def Add_tt():
        conexao = sql.connect(host='localhost',user='root',password='1234',database='dados')
        # Criação
        semana = SemanaEntry.get()
        Display = DisplayEntry.get()
        Organica = OrganicaEntry.get()
        Paga = PagaEntry.get()
        Direta = DiretaEntry.get()
        Social = SocialEntry.get()
        Email = EmailEntry.get()
        Ref = RefEntry.get()
        
 
        cursor = conexao.cursor()
        comando = f"""insert into  trafego_novo (semana2,novo_display,novo_organico ,novo_pago,novo_direta ,novo_social ,novo_email,nref) values("{semana}","{Display}","{Organica}","{Paga}","{Direta}","{Social}","{Email}","{Ref}")"""
        cursor.execute(comando)
        conexao.commit()

        messagebox.showinfo('Informação','Dados inseridos com sucesso!')
       
        cursor.close()
        conexao.close()
   
       
 
 
   
   
   
    AddButton = Button(jantn,text='Inserir',font={'century gothic',20} , bg='grey',fg='black',command=Add_tt)
    AddButton.place(x=200,y=300)
 
    UpButton = Button(jantn,text='Alterar dados',font={'century gothic',20} , bg='grey',fg='black',command=jan_UPtf)
    UpButton.place(x=300,y=300)

    LerButton = Button(jantn,text='Ler dados',font={'century gothic',20} , bg='grey',fg='black',command=LerTf)
    LerButton.place(x=450,y=300)

def Rel():
    webbrowser.open('https://app.powerbi.com/links/5jvVDGc2rR?ctid=ceda6518-cbc2-4f99-ace9-6c5749c41993&pbi_source=linkShare')
 
SiteButton = Button(text='Site: ',font={'century gothic',20} , bg='grey',fg='black',command=Jan_Site)
SiteButton.place(x = 50, y = 20)

 
LinkButton = Button(text='Linkedin: ',font={'century gothic',20} , bg='grey',fg='black',command=Jan_Lik)
LinkButton.place(x= 50, y =80)
 
 
InstaButton = Button(text='Instagram: ',font={'century gothic',20} , bg='grey',fg='black',command=Jan_Insta)
InstaButton.place(x= 50, y =140)
 
GoogleButton = Button(text='Google: ',font={'century gothic',20} , bg='grey',fg='black',command=Jan_Goo)
GoogleButton.place(x= 50, y =200)

TrafegototalButton = Button(text='Trafego Total: ',font={'century gothic',20} , bg='grey',fg='black',command=jan_tt) 
TrafegototalButton.place(x=50, y=260)

TrafegoNovoButton = Button(text='Trafego Novo: ',font={'century gothic',20} , bg='grey',fg='black',command=jan_tn) 
TrafegoNovoButton.place(x=50, y =320)

LerButton = Button(text='Todos os dados: ',font={'century gothic',20} , bg='grey',fg='black',command=Lertudo)
LerButton.place(x= 50, y =380)

RelButton =  Button(text='Relatório: ',font={'century gothic',20} , bg='grey',fg='black',command=Rel)
RelButton.place(x=50,y=440)



jan.mainloop()
 
 
# Corrigir trafego novo e total. não apaga e não atualiza

 

#https://app.powerbi.com/links/5jvVDGc2rR?ctid=ceda6518-cbc2-4f99-ace9-6c5749c41993&pbi_source=linkShare