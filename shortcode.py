import requests, sys, json, os
from tkinter import *
import tkinter.messagebox as tkmsg
from time import sleep
from ctypes import *
from random import randint

login = "lucassilveira"
token = "0613b8a0f5f1ec203581291d9c33aa23"

def sair():
	sys.exit(0)
	exit(0)

def menu(login, senha):
	menu_login.destroy()
	#################################
	global menu
	menu = Tk()
	menu.title('Central - Adriel')
	menu['bg'] = "white"
	#################################
	def gerar_numeros():
		if(len(dd.get()) > 2):
			tkmsg.askretrycancel("Falha ao Logar!", "Tente Logar novamente! login e senha incorretos.")
		else:
			for i in range(1, 100):
				numero = "{}984{}{}{}{}{}{}".format(dd.get(), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
				nums.insert("1.0", "{},".format(numero))
	#################################
	def enviar():
		lista_nums = nums.get("1.0", "end-1c")
		texto = txt.get("1.0", "end-1c")
		if(len(texto) > 160):
			Label(menu, text="Status: Mensagem Muito grande (tamanho maximo: 160 caracteres)!", bg='white', fg='green', font="Arial 11").place(x=250, y=270)
		else:
			lista_nums = lista_nums.split(',')
			for numeros in lista_nums:
				if numeros != "":
					'''
					criar log por numero que deu erro, e adicionar em uma lista txt
					'''
					url = "http://painel.kingsms.com.br/kingsms/api.php?acao=sendsms&login={}&token={}&numero={}&msg={}".format(login, senha, numeros, texto)
					json_result = json.loads(requests.get(url).text)
					Label(menu, text="Saldo: {}".format(json_result['cause']), bg='white', fg='black').place(x=5, y=20)
					Label(menu, text="Status: SMS Enviado (Numero: {})(Status: {})!".format(numeros, json_result['cause']), bg='white', fg='green', font="Arial 11").place(x=250, y=270)
				else:
					Label(menu, text="Status: Fim de Numeros!", bg='white', fg='green', font="Arial 11").place(x=250, y=270)
	#################################
	url = "http://painel.kingsms.com.br/kingsms/api.php?acao=saldo&login={}&token={}".format(login, senha)
	json_result = json.loads(requests.get(url).text)
	#################################
	Label(menu, text="Usuario: {}".format(login), bg='white', fg='black').place(x=5, y=5)
	Label(menu, text="Saldo: {}".format(json_result['cause']), bg='white', fg='black').place(x=5, y=20)
	Label(menu, text="Mensagem: ", bg='white', fg='black').place(x=170, y=70)
	Label(menu, text="Lista de Numeros:", bg='white', fg='black').place(x=520, y=70)
	#################################
	global dd
	dd = Entry(menu, bg='white', fg='black', width=6)
	dd.insert(0, "DDD")
	dd.place(x=630, y=70)
	Label(menu, text="Status: Logado!", bg='white', fg='green', font="Arial 11").place(x=250, y=270)
	#################################
	global txt
	txt = Text(menu, width=50, height=10)
	txt.place(x=10, y=100)
	#################################
	global nums
	nums = Text(menu, width=20, height=10)
	nums.place(x=500, y=100)
	#################################
	bt1 = Button(menu, text="Confirmar", bg="white", fg="green", command=enviar, width=15).place(x=10, y=270)
	bt2 = Button(menu, text="Gerar", bg="white", fg="green", command=gerar_numeros, width=10).place(x=145, y=270)
	#################################
	menu.geometry("750x300")
	menu.mainloop()

def menu_login():
	def logar():
		url = "http://painel.kingsms.com.br/kingsms/api.php?acao=saldo&login={}&token={}".format(ed1.get(), ed2.get())
		json_result = json.loads(requests.get(url).text)
		if json_result['status'] == 'success':
			menu(ed1.get(), ed2.get())
		else:
			tkmsg.askretrycancel("Falha ao Logar!", "Tente Logar novamente! login e senha incorretos.")
	#################################
	global menu_login
	menu_login = Tk()
	menu_login.title('Central - Adriel')
	menu_login['bg'] = "white"
	#################################
	label1 = Label(menu_login, text="Login: ", bg='white', fg='black').place(x=5, y=30)
	#################################
	label2 = Label(menu_login, text="Token: ", bg='white', fg='black').place(x=5, y=60)
	#################################
	global ed1, ed2
	ed1 = Entry(menu_login)
	ed1.place(x=60, y=30)
	ed2 = Entry(menu_login, show='*')
	ed2.place(x=60, y=60)
	#################################
	bt1 = Button(menu_login, text="Confirmar", bg="white", fg="green", command=logar, width=20).place(x=60, y=100)
	bt2 = Button(menu_login, text="Sair", bg="white", fg="red", command=sair, width=20).place(x=60, y=130)
	#################################
	menu_login.geometry("270x170")
	menu_login.mainloop()

menu_login()