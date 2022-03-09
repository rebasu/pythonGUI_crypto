from tkinter import *
from tkinter import ttk, messagebox

import csv

import hashlib

#####-----PARAMETER-----#####

resolution = '1000x700'
title = 'Crypto allcation GUI Project (Uncle Engineer)'
FONT1 = ('Angsana New', 22)
FONT2 = ('Angsana New', 20)
FONT3 = ('Angsana New', 18)
FONT4 = ('Angsana New', 15)
VERSION = '1.0'
KEY = ' 0xF306AAEd663534398C37A2566467a26dB6886c33'


OFFSET = 5

Brelx = 0.82 # relx logout button
Brely = 0.12 # rely logout button


#####-----MAIN-----#####

GUI = Tk()
GUI.title(title)
GUI.geometry(resolution)
GUI.iconbitmap('assets/icon.ico')

style = ttk.Style(GUI)
style.theme_use('winnative')


#####-----PhotoImage-----#####

icon_tab1 = PhotoImage(file = 'assets/login_icon.png')
icon_tab2 = PhotoImage(file = 'assets/coin_icon.png')
icon_tab3 = PhotoImage(file = 'assets/account_icon.png')
icon_tab4 = PhotoImage(file = 'assets/Aboutme_icon.png')

icon_allocation = PhotoImage(file = "assets/coin2_icon.png")
icon_aboutme = PhotoImage(file = 'assets/Aboutme2_icon.png')
icon_metamask = PhotoImage(file = 'assets/metamask.png')
icon_checklist = PhotoImage(file = 'assets/checklist_icon.png')
icon_logout = PhotoImage(file = 'assets/logout_icon.png')

icon_addini = PhotoImage(file = 'assets/addini_icon.png')
icon_trade = PhotoImage(file = 'assets/trade_icon.png')

icon_account = PhotoImage(file = 'assets/account2_icon.png')
icon_password = PhotoImage(file = 'assets/password_icon.png')
icon_password2 = PhotoImage(file = 'assets/password2_icon.png')
icon_undo = PhotoImage(file = 'assets/undo_icon.png')
icon_clearorder = PhotoImage(file = 'assets/clearorder_icon.png')
icon_clearini = PhotoImage(file = 'assets/clearini_icon.png')

icon_addini2 = PhotoImage(file = 'assets/addini2_icon.png')
icon_cal = PhotoImage(file = 'assets/cal_icon.png')
icon_buy = PhotoImage(file = 'assets/buy_icon.png')
icon_sell = PhotoImage(file = 'assets/sell_icon.png')
icon_save = PhotoImage(file = 'assets/save_icon.png')
icon_register = PhotoImage(file = 'assets/register_icon.png')

icon_BTC = PhotoImage(file = 'assets/BTC_icon.png')
icon_ETH = PhotoImage(file = 'assets/ETH_icon.png')
icon_LUNA = PhotoImage(file = 'assets/LUNA_icon.png')
icon_DOGE = PhotoImage(file = 'assets/DOGE_icon.png')
icon_SOL = PhotoImage(file = 'assets/SOL_icon.png')
icon_ADA = PhotoImage(file = 'assets/ADA_icon.png')


#####-----TAB-----#####

Tab = ttk.Notebook(GUI)
Tab.pack(fill = BOTH, expand = 1)

Tab1 = Frame(Tab)
Tab2 = Frame(Tab)
Tab3 = Frame(Tab)
Tab4 = Frame(Tab)
Tab.add(Tab1, text = 'Login', compound = 'left', image = icon_tab1)


#####-----TEMPLATE-----#####

def UpdateTable(data, value):
    table.delete(*table.get_children())
    table.insert('', 'end', value = value)



def LabelEntry(GUI, text, font, show = None):
	v_strvar = StringVar()
	L = Label(GUI, text = text, font = font).pack()
	E = ttk.Entry(GUI, textvariable = v_strvar, font = font, justify = 'center', show = show)
	return(L, E, v_strvar)


def Version(Tabnumber, VERSION = VERSION):
	L_version = Label(Tabnumber, text = f"Current version: {VERSION}")
	L_version.place(relx = 1.0, rely = 1.0, anchor='se')

def LogoutButton(Tabnumber, relx = Brelx, rely = Brely):
	B_Logout = ttk.Button(Tabnumber, text = 'Logout', command = LogoutComfirm, image = icon_logout, compound = 'left')
	B_Logout.pack()

def LogoutComfirm():
	msgbox = messagebox.askokcancel('Logout', 'Do you confirm to logout?')
	if msgbox:
		Logout()


def Logout():
	v_username.set('')
	v_password.set('')
	Tab.hide(1)
	Tab.hide(2)
	Tab.hide(3)
	Tab.add(Tab1, text = 'Login', compound = 'left')
	Tab.select(0)
	v_incorrect.set('')
	E_username.focus()


def InitialMoney():
	INITIAL = Toplevel()
	INITIAL.title('Initial fiat money')
	INITIAL.geometry('400x330')
	INITIAL.iconbitmap('assets/addini.ico')
	INITIAL.focus_force()

	style = ttk.Style(INITIAL)
	style.theme_use('winnative')

	def InsertInitial(event = None):
		try:
			ini = round(float(v_INI.get()), 2)
			if ini < 0:
				messagebox.showinfo('Input positive money', 'The initial money should be positive value!')
				return

			data = ReadCSV()
			username = v_username.get()

			for item in range(len(data)):
				if data[item][0] == username:
					try:
						print(data[item][2])
						messagebox.showinfo('Already Inserted',f'You have inserted fiat money, now you have {data[item][2]} THB.')
					except:
						data[item].append(ini)
						messagebox.showinfo('Insert completed',f'Initial money insert completed, now you have {ini} THB.')
			v_INITIAL.set(f'Your initial money : {ini} THB')
			v_balance.set(str(ini))
			B_order.state(['!disabled'])
			B_undo.state(['!disabled'])
			B_reset.state(['!disabled'])
			B_INITIAL.state(['disabled'])
			updatetocsv(data, filename = 'log.csv')
			

		except:
			messagebox.showinfo('Input wrong data', 'The initial money should be number!')
		INITIAL.destroy()

			

	L = Label(INITIAL, image = icon_addini2)
	L.pack(pady = 20)
	L_INI, E_INI, v_INI = LabelEntry(INITIAL, 'Input your initial fiat money (THB)', font = FONT2)
	E_INI.pack(pady = OFFSET)
	B_INI = ttk.Button(INITIAL, text = 'Save', command = InsertInitial, image = icon_save, compound = 'left')
	B_INI.pack(pady = OFFSET)

	E_INI.focus()
	E_INI.bind('<Return>', InsertInitial)


def ListCoin(data):
	cryp_list = ['BTC', 'ETH', 'DOGE', 'ADA', 'LUNA', 'SOL']
	cryp_amount = [0, 0, 0, 0, 0, 0]
	text = 'You have:'
	for cryp in range(len(cryp_list)):
		for i in range(len(data)):
			if data[i][1] == 'Buy' and cryp_list[cryp] == data[i][2]:
				print('buy', cryp, data[i][3])
				cryp_amount[cryp] = cryp_amount[cryp] +  float(data[i][3])
			if data[i][1] == 'Sell' and cryp_list[cryp] == data[i][2]:
				print('Sell', cryp, data[i][3])
				cryp_amount[cryp] = cryp_amount[cryp] - float(data[i][3])
	print(cryp_amount)
	for t in range(len(cryp_list)):
		if t < 5:
			text = text + ' ' + str(round(cryp_amount[t], 8)) + ' ' + str(cryp_list[t]) + ','
		else:
			text = text + ' ' + str(round(cryp_amount[t], 8)) + ' ' + str(cryp_list[t])
	print(text)
	v_coin.set(text)


def Order():
	ORDER = Toplevel()
	ORDER.title('Add order')
	ORDER.geometry('500x520')
	ORDER.focus_force()
	style = ttk.Style(ORDER)
	style.theme_use('winnative')
	ORDER.iconbitmap('assets/checklist_icon.ico')

	def Calc():
		cryp = v_cryp.get()
		try:
			amount = round(float(v_amount.get()), 8)
			price = round(float(v_price.get()), 2)
			total = round((amount * price), 2)
			if amount > 0 and price > 0 and total > 0:
				v_cal.set(f'Total price: {total:,} THB ({price:,} THB for 1 {cryp})')
				B_recal.state(['!disabled'])
				B_cal.state(['disabled'])
				B_buy.state(['!disabled'])
				B_sell.state(['!disabled'])
				E_amount.state(['disabled'])
				E_price.state(['disabled'])
			else:
				v_cal.set(f'Please input positive number!')
				B_buy.state(['disabled'])
				B_sell.state(['disabled'])
		except:
			v_cal.set(f'Please input the correct value!')
			B_buy.state(['disabled'])
			B_sell.state(['disabled'])

	def ReCalc():
		B_cal.state(['!disabled'])
		B_buy.state(['disabled'])
		B_sell.state(['disabled'])
		B_recal.state(['disabled'])
		E_amount.state(['!disabled'])
		E_price.state(['!disabled'])
		v_amount.set('')
		v_price.set('')
		v_cal.set('Enter your order and click <calculate>')



	def BuyOrder():
		msgbox = messagebox.askokcancel('Buy order', 'Are you sure to buy this order?')
		print('BUY', msgbox)
		if msgbox == True:
			data = ReadCSV()
			username = v_username.get()
			cryp = v_cryp.get()
			amount = round(float(v_amount.get()), 8)
			price = round(float(v_price.get()), 2)
			total = round((amount * price), 2)
			order = [1, 'Buy', cryp, amount, price, total]
			for item in range(len(data)):
				if data[item][0] == username:
					try:
						order_csv = ReadCSV(filename = f'order_{username}.csv')
						initial = float(order_csv[-1][6])
						grand_total = initial - total
						if grand_total < 0:
							messagebox.showinfo('Cannot create an order', 'Not enough money!')
							break
						order.append(grand_total)
						order_csv.append(order)
						order_csv[-1][0] = len(order_csv)
						updatetocsv(order_csv, filename = f'order_{username}.csv')
						log_csv = ReadCSV(filename = f'order_{username}.csv')
						table.delete(*table.get_children())
						number_bs = len(log_csv)
						balance = log_csv[-1][6]
						v_numberbs.set(number_bs)
						v_balance.set(balance)
						for element in log_csv:
							table.insert('', 'end', value = element)
						v_INITIAL.set(f'Your initial money : {float(data[item][2]):,.2f} THB. Current money: {float(balance):,.2f} THB')

						ListCoin(log_csv)

					except Exception as e:
						print(e)
						grand_total = round(float(data[item][2]), 2) - total
						if grand_total < 0:
							messagebox.showinfo('Cannot create an order', 'Not enough money!')
							break
						order.append(grand_total)
						table.insert('', 'end', value = order)
						writetocsv(order, filename = f'order_{username}.csv')
						v_INITIAL.set(f'Your initial money : {float(data[item][2]):,.2f} THB. Current money: {float(grand_total):,.2f} THB')
						v_numberbs.set('1')
						v_balance.set(grand_total)
						log_csv = ReadCSV(filename = f'order_{username}.csv')
						ListCoin(data = log_csv)
			ORDER.destroy()



	def SellOrder():
		msgbox = messagebox.askokcancel('Sell order', 'Are you sure to sell this order?')
		print('sell', msgbox)
		if msgbox == True:
			data = ReadCSV()
			username = v_username.get()
			cryp = v_cryp.get()
			amount = round(float(v_amount.get()), 8)
			price = round(float(v_price.get()), 2)
			total = round((amount * price), 2)
			order = [1, 'Sell', cryp, amount, price, total]
			for item in range(len(data)):
				if data[item][0] == username:
					try:
						order_csv = ReadCSV(filename = f'order_{username}.csv')
						initial = float(order_csv[-1][6])
						grand_total = initial + total
						order.append(grand_total)
						order_csv.append(order)
						order_csv[-1][0] = len(order_csv)
						updatetocsv(order_csv, filename = f'order_{username}.csv')
						log_csv = ReadCSV(filename = f'order_{username}.csv')
						table.delete(*table.get_children())
						number_bs = len(log_csv)
						balance = log_csv[-1][6]
						v_numberbs.set(number_bs)
						v_balance.set(balance)
						for element in log_csv:
							table.insert('', 'end', value = element)
						v_INITIAL.set(f'Your initial money : {float(data[item][2]):,.2f} THB. Current money: {float(balance):,.2f} THB')
						

						SELL_STATE = True
						cryp_list = ['BTC', 'ETH', 'DOGE', 'ADA', 'LUNA', 'SOL']
						cryp_amount = [0, 0, 0, 0, 0, 0]
						text = 'You have:'
						for cryp in range(len(cryp_list)):
							for i in range(len(log_csv)):
								if log_csv[i][1] == 'Buy' and cryp_list[cryp] == log_csv[i][2]:
									print('buy', cryp, log_csv[i][3])
									cryp_amount[cryp] = cryp_amount[cryp] +  float(log_csv[i][3])
								if log_csv[i][1] == 'Sell' and cryp_list[cryp] == log_csv[i][2]:
									print('Sell', cryp, log_csv[i][3])
									cryp_amount[cryp] = cryp_amount[cryp] - float(log_csv[i][3])
								print(cryp_amount[cryp])
						print(cryp_amount)
						for n in cryp_amount:
							if n < 0:
								log_csv = log_csv[:len(log_csv) - 1]
								table.delete(*table.get_children())
								for item in log_csv:
									table.insert('', 'end', value = item)
								messagebox.showinfo('Cannot create an order', f'Not enough {v_cryp.get()}')
								updatetocsv(filename = f'order_{username}.csv', data = log_csv)
								SELL_STATE = False
						if SELL_STATE == True:
							for t in range(len(cryp_list)):
								if t < 5:
									text = text + ' ' + str(round(cryp_amount[t], 8)) + ' ' + str(cryp_list[t]) + ','
								else:
									text = text + ' ' + str(round(cryp_amount[t], 8)) + ' ' + str(cryp_list[t])
							print(text)
							v_coin.set(text)
						else:
							break


					except Exception as e:
						print(e)
						messagebox.showinfo('Cannot create an order', f'Not enough {v_cryp.get()}')

			ORDER.destroy()



	FrameA = Frame(ORDER)
	FrameA.place(x = 150, y = 10)
	FrameB = Frame(ORDER)
	FrameB.place(x = 192, y = 275)

	L = Label(FrameA, text = 'Select your cryptocurrency', font = FONT2)
	L.pack()

	cryp_list = ['BTC', 'ETH', 'DOGE', 'ADA', 'LUNA', 'SOL']
	v_cryp = StringVar()
	v_cryp.set(cryp_list[0])

	combobox = ttk.Combobox(FrameA, textvariable = v_cryp , values = cryp_list, state = "readonly")
	combobox.pack(pady = OFFSET - 1)

	L_amount, E_amount, v_amount = LabelEntry(FrameA, text = 'Amount', font = FONT3)
	E_amount.pack(pady = OFFSET - 1)


	L_price, E_price, v_price = LabelEntry(FrameA, text = 'Price (THB)', font = FONT3)
	E_price.pack(pady = OFFSET - 1)

	B_cal = ttk.Button(FrameB, text = 'Calculate', command = Calc, image = icon_cal, compound = 'left')
	B_cal.pack(pady = OFFSET - 1)

	B_recal = ttk.Button(ORDER, text = 'Recalculate', command = ReCalc, image = icon_undo, compound = 'left')
	B_recal.place(x = 62, y = 350)

	B_recal.state(['disabled'])

	v_cal = StringVar()
	v_cal.set('Enter your order and click <calculate>')

	v_money = StringVar()
	cal = v_balance.get()
	v_money.set(f'Current money: {cal} THB.')

	

	B_buy = ttk.Button(ORDER, text = 'BUY', command = BuyOrder, image = icon_buy, compound = 'left')
	B_buy.place(x = 192, y = 350)
	B_buy.state(['disabled'])


	B_sell = ttk.Button(ORDER, text = 'SELL', command = SellOrder, image = icon_sell, compound = 'left')
	B_sell.place(x = 322, y = 350)

	B_sell.state(['disabled'])

	L_cal = Label(ORDER, textvariable = v_cal, font = FONT3)
	L_cal.place(relx = 0.5, rely = 0.87, anchor = 's')

	L_money = Label(ORDER, textvariable = v_money, font = FONT3, fg = 'red')
	L_money.place(relx = 0.5, rely = 0.935, anchor = 's')

	L_coin = Label(ORDER, textvariable = v_coin, font = FONT3, fg = 'blue')
	L_coin.place(relx = 0.5, rely = 1, anchor = 's')

	E_amount.focus()

	ORDER.mainloop()



def Undo():
	msgbox = messagebox.askokcancel('Undo order', 'Do you confirm to Undo the latest order?')
	if msgbox:
		username = v_username.get()
		order = ReadCSV(f'order_{username}.csv')
		if len(order) <= 1:
			updatetocsv(filename = f'order_{username}.csv', data = '')
			table.delete(*table.get_children())
			v_coin.set('')
			data = ReadCSV()
			for i in range(len(data)):
				if data[i][0] == username:
					v_INITIAL.set(f'Your initial money : {float(data[i][2]):,.2f} THB.')
					v_balance.set(float(data[i][2]))
					v_numberbs.set('0')
		else:
			order.remove(order[-1])
			balance = order[-1][6]
			number_bs = len(order)
			updatetocsv(filename = f'order_{username}.csv', data = order)
			order.reverse()
			table.delete(*table.get_children())
			for item in order:
				table.insert('', 0, value = item)
			ListCoin(order)
			data = ReadCSV()
			for i in range(len(data)):
				if data[i][0] == username:
					v_INITIAL.set(f'Your initial money : {float(data[i][2]):,.2f} THB. Current money: {float(balance):,.2f} THB')
					v_balance.set(balance)
					v_numberbs.set(number_bs)
	

def Reset():
	msgbox = messagebox.askokcancel('Reset order', 'Do you confirm to Reset all order?')
	if msgbox:
		username = v_username.get()
		updatetocsv(filename = f'order_{username}.csv', data = '')
		table.delete(*table.get_children())
		v_coin.set('')
		data = ReadCSV()
		for i in range(len(data)):
			if data[i][0] == username:
				v_INITIAL.set(f'Your initial money : {float(data[i][2]):,.2f} THB.')
				v_balance.set(float(data[i][2]))
				v_numberbs.set('0')


def ReIni():
	msgbox = messagebox.askokcancel('Reset order and clear initial money', 'Do you confirm to Reset all order and clear initial money?')
	if msgbox:
		msgbox2 = messagebox.askokcancel('Warning', 'All order will be deleted and initial money will be set to ZERO, Are you sure?')
		if msgbox2:
			username = v_username.get()
			updatetocsv(filename = f'order_{username}.csv', data = '')
			table.delete(*table.get_children())
			v_coin.set('')
			data = ReadCSV()
			for i in range(len(data)):
				if data[i][0] == username:
					print(data[i][2], data[i][-1])
					data[i].remove(data[i][-1])
					v_INITIAL.set('Please insert your initial fiat money!')
					v_balance.set('0')
					v_numberbs.set('0')
					B_order.state(['disabled'])
					B_undo.state(['disabled'])
					B_reset.state(['disabled'])
					B_INITIAL.state(['!disabled'])
			print(data)
			updatetocsv(filename = 'log.csv', data = data)



#####-----CHECK PASSWORD-----#####

def Encode(plaintext):
	text = plaintext.encode()
	d = hashlib.sha256(text)
	encode_text = d.digest()
	encode_text = d.hexdigest()
	return encode_text


def CheckPassword(event = None):
	try:
		(username, password) = (v_username.get(), v_password.get())
		data = ReadCSV()
		for item in range(len(data)):
			check_pass = Encode(password)
			if username == data[item][0] and check_pass == data[item][1]:
				Tab.hide(0)
				Tab.add(Tab2, text = 'Allocation', compound = 'left', image = icon_tab2)
				Tab.add(Tab3, text = 'Account', compound = 'left', image = icon_tab3)
				Tab.add(Tab4, text = 'About Me', compound = 'left', image = icon_tab4)
				Tab.select(1)

				username = v_username.get()
				v_text.set(f'Welcome back, {username}')
				table.delete(*table.get_children())
				try:
					log_csv = ReadCSV(filename = f'order_{username}.csv')
					number_bs = len(log_csv)
					balance = log_csv[-1][6]
					v_numberbs.set(number_bs)
					v_balance.set(balance)
					for p in log_csv:
						table.insert('', 'end', value = p)

					ListCoin(log_csv)

				except Exception as e:
					print(e)
					v_coin.set('')

				try:
					try:
						ini_money = float(data[item][2])
						balance = float(balance)
						v_INITIAL.set(f'Your initial money : {ini_money:,.2f} THB. Current money: {balance:,.2f} THB')
						
					except:
						v_INITIAL.set(f'Your initial money : {ini_money:,.2f} THB')
						v_balance.set(ini_money)
					B_order.state(['!disabled'])
					B_undo.state(['!disabled'])
					B_reset.state(['!disabled'])
					B_INITIAL.state(['disabled'])
				except Exception as e:
					print(e)
					v_INITIAL.set('Please insert your initial fiat money!')
					v_balance.set('0')
					v_numberbs.set('0')
					B_order.state(['disabled'])
					B_undo.state(['disabled'])
					B_reset.state(['disabled'])
					B_INITIAL.state(['!disabled'])
				break
	except Exception as e: print(e)

	v_incorrect.set('Incorrect username or password')


def ChangePassword():

	CP = Toplevel()
	CP.title('Change Password')
	CP.geometry('500x450')
	CP.focus_force()
	style = ttk.Style(CP)
	style.theme_use('winnative')
	CP.iconbitmap('assets/password2_icon.ico')


	def ComparePassword(event = None):
		msgbox = messagebox.askokcancel('Comfirm change passsword', 'Do you confirm to change password?')
		if msgbox:
			data = ReadCSV()
			for item in range(len(data)):
				if data[item][0] == username:
					password = data[item][1]
			oldpass = v_oldpass.get()
			oldpass = Encode(oldpass)
			newpass = v_newpass.get()
			newpass = Encode(newpass)
			if oldpass == password:
				messagebox.showinfo('Success', 'Change successfully')
				for item in range(len(data)):
					if data[item][0] == username:
						data[item][1] = newpass
				updatetocsv(data)
				
			else:
				messagebox.showwarning('Wrong password', 'Wrong password, please try again.')
			CP.destroy()


	(username, password) = (v_username.get(), v_password.get())
	v_oldpass = StringVar()
	v_newpass = StringVar()
	v_oldpass.set('')
	v_newpass.set('')

	L = Label(CP, image = icon_password2)
	L.pack(pady = 20)

	L, E_oldpass, v_oldpass = LabelEntry(CP, 'Input your old password', FONT3, '*')
	E_oldpass.pack(pady = OFFSET)

	L, E_newpass, v_newpass = LabelEntry(CP, 'Input your new password', FONT3, '*')
	E_newpass.pack(pady = OFFSET)

	B = ttk.Button(CP, text = 'Change password', command = ComparePassword, image = icon_password, compound = 'left')
	B.pack()

	E_oldpass.focus()
	E_newpass.bind('<Return>', ComparePassword)


#####-----LOG CSV-----#####


def writetocsv(data, filename = 'log.csv'):
    with open(filename, 'a', newline = '', encoding = 'utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)


def updatetocsv(data, filename = 'log.csv'):
    with open(filename, 'w', newline = '', encoding = 'utf-8') as file:
        fw = csv.writer(file)
        fw.writerows(data)


def ReadCSV(filename = 'log.csv'):
	data = []
	with open(filename, newline = '', encoding = 'utf-8') as file:
		fr = csv.reader(file)
		for row in fr:
			data.append(row)
	return data


#####-----REGISTER FORM-----#####

def RegisterForm(event = None):

	REG = Toplevel()
	REG.title('Register')
	REG.geometry('450x500')
	REG.focus_force()
	REG.iconbitmap('assets/register_icon.ico')



#####-------CSV CRUD-----#####
	def Register(event = None):
		(username, password) = (v_reguser.get(), v_regpass.get())
		password = Encode(password)
		data = [username, password]
		STATUS = True
		try:
			check_data = ReadCSV()
			for item in range(len(check_data)):
				if check_data[item][0] == username:
					STATUS = False
			if STATUS:
				messagebox.showinfo('Register Complete','Register Success')
				writetocsv(data)
			else:
				messagebox.showinfo('Cannot register','This username has been used!')

		except:
			messagebox.showinfo('Register Complete','Register Success')
			writetocsv(data)
		REG.destroy()


	L = Label(REG, image = icon_register, compound = 'left')
	L.pack(pady = 20)


	L = Label(REG, text = 'Create an account', font = FONT1).pack(pady = 3)

	L, E_reguser, v_reguser = LabelEntry(REG, 'Username', FONT3)
	E_reguser.pack(pady = OFFSET)


	L, E_regpass, v_regpass = LabelEntry(REG, 'Password', FONT3, '*')
	E_regpass.pack(pady = OFFSET)

	B_reg = ttk.Button(REG, text = 'Register', command = Register, image = icon_tab3, compound = 'left')
	B_reg.pack(pady = OFFSET)

	Version(REG)

	E_reguser.focus()

	E_regpass.bind("<Return>", Register)

	REG.mainloop()


#####-----LOGIN-----#####


Frame1_1 = Frame(Tab1)
Frame1_1.place(x = 330, y = 250)

Frame1_2 = Frame(Tab1)
Frame1_2.place(x = 255, y = 5)


icon_cryp = [icon_BTC, icon_ETH, icon_LUNA, icon_DOGE, icon_SOL, icon_ADA]
for i in range(6):
	L = Label(Tab1, image = icon_cryp[i]).place(x = 50 + 150 * i, y = 105)

L = Label(Frame1_2, text = 'Welcome to crypto allcation program', font = FONT1).pack()
L = Label(Frame1_2, text = 'Now we accept BTC / ETH / LUNA / DOGE / SOL / ADA (More in further)', font = FONT3).pack()


L = Label(Frame1_1, text = 'Please login', font = FONT1).pack(pady = OFFSET)

L, E_username, v_username = LabelEntry(Frame1_1, 'Username', FONT3)
E_username.pack(pady = OFFSET)

L, E_password, v_password = LabelEntry(Frame1_1, 'Password', FONT3, '*')
E_password.pack(pady = OFFSET)

B_login = ttk.Button(Frame1_1, text = 'Login', command = CheckPassword, image = icon_tab1, compound = 'left')
B_login.pack(pady = OFFSET)

L_login = Label(Frame1_1, text = "If you don't have any account, register here.", font = FONT2, fg = "blue")
L_login.pack(pady = OFFSET)

v_incorrect = StringVar()
L_wrong = Label(Frame1_1, textvariable = v_incorrect, font = FONT2, fg = 'red')
L_wrong.pack()

Version(Tab1)

E_username.focus()

E_password.bind("<Return>", CheckPassword)
L_login.bind("<Button-1>", RegisterForm)


#####-----CRYPTO ALLOCATION-----#####


Frame2_1 = Frame(Tab2)
Frame2_1.place(x = 100, y = 135)

Frame2_2 = Frame(Tab2)
Frame2_2.place(x = 800, y = 0)

Frame2_3 = Frame(Tab2)
Frame2_3.place(x = 365, y = 100)

L = Label(Frame2_1, image = icon_allocation)
L.pack()

L = Label(Frame2_1, text = 'Crypto Allocation', font = FONT2)
L.pack()

B_INITIAL = ttk.Button(Frame2_1, text = 'Insert Initial', command = InitialMoney, image = icon_addini, compound = 'left')
B_INITIAL.pack(ipadx = 35, ipady = OFFSET)

B_order = ttk.Button(Frame2_1, text = 'Create order', command = Order, image = icon_trade, compound = 'left')
B_order.pack(ipadx = 35, ipady = OFFSET)


v_INITIAL = StringVar()

L_INITIAL = Label(Frame2_3, textvariable = v_INITIAL, font = FONT3)
L_INITIAL.pack()



header = ['Order No.', 'Buy/Sell', 'Currency', 'Amount', 'Rate', 'Total', 'Grand total']
hwidth = [65, 75, 75, 75, 80, 75, 100]


table = ttk.Treeview(Frame2_3, columns = header, show = 'headings', height = 15)
table.pack()


for hd,hw in zip(header, hwidth):
    table.heading(hd, text = hd)
    table.column(hd, width = hw)

v_coin = StringVar()
v_coin.set('Currency amount summary: ')

L_coin = Label(Frame2_3, textvariable = v_coin, font = FONT3)
L_coin.pack()

B_undo = ttk.Button(Tab2, text = 'Undo', command = Undo, image = icon_undo, compound = 'left')
B_undo.place(x = 400, y = 510)

B_reset = ttk.Button(Tab2, text = 'Clear order', command = Reset, image = icon_clearorder, compound = 'left')
B_reset.place(x = 585, y = 510)

B_reini = ttk.Button(Tab2, text = 'Clear Initial', command = ReIni, image = icon_clearini, compound = 'left')
B_reini.place(x = 770, y = 510)

Version(Tab2)

v_text = StringVar()

L_user = Label(Frame2_2, textvariable = v_text, font = FONT3)
L_user.pack()

LogoutButton(Frame2_2)


#####-----ACCOUNT-----#####


Frame3_1 = Frame(Tab3)
Frame3_1.place(x = 400, y = 115)

Frame3_2 = Frame(Tab3)
Frame3_2.place(x = 800, y = 0)


information = ['0', '0', '0']

v_balance = StringVar()
v_numberbs = StringVar()

v_balance.set(information[0])
v_numberbs.set(information[1])

L = Label(Frame3_1, image = icon_account)
L.pack()

L = Label(Frame3_1, text = 'Account information' , font = FONT2)
L.pack()


L = Label(Frame3_1, text = 'Your balance' , font = FONT3)
L.pack()


L_balance = Label(Frame3_1, textvariable = v_balance, font = FONT3)
L_balance.pack()

L = Label(Frame3_1, text = 'Number of buy-sell' , font = FONT2)
L.pack()

L_numberbs = Label(Frame3_1, textvariable = v_numberbs, font = FONT3)
L_numberbs.pack()


B_changepass = ttk.Button(Frame3_1, text = 'Change password', command = ChangePassword, image = icon_password, compound = 'left')
B_changepass.pack()



L_user = Label(Frame3_2, textvariable = v_text, font = FONT3)
L_user.pack()

LogoutButton(Frame3_2)

Version(Tab3)




#####-----ABOUT ME-----#####


Frame4_1 = Frame(Tab4)
Frame4_1.place(x = 175, y = 50)

Frame4_2 = Frame(Tab4)
Frame4_2.place(x = 515, y = 185)

Frame4_3 = Frame(Tab4)
Frame4_3.place(x = 800, y = 0)

Frame4_4 = Frame(Tab4)
Frame4_4.place(x = 96, y = 330)

L = Label(Frame4_1, image = icon_aboutme)
L.pack()

L = Label(Frame4_1, text = 'About me', font = FONT2)
L.pack()

L = Label(Frame4_1, text = 'Name: Wanthep Saesee', font = FONT3)
L.pack()

L = Label(Frame4_1, text = 'Role: Newbie Developer', font = FONT3)
L.pack()

L = Label(Frame4_4, image = icon_checklist)
L.pack()

L = Label(Frame4_4, text = 'Further Plans', font = FONT3)
L.pack()

L = Label(Frame4_4, text = '1. API the crypto value and show in this GUI', font = FONT4)
L.pack()

L = Label(Frame4_4, text = '2. Do the trading simulation on the price that collect in API', font = FONT4)
L.pack()

L = Label(Frame4_2, image = icon_metamask)
L.pack()

L = Label(Frame4_2, text = 'Please support me for a cup of coffee :)', font = FONT3)
L.pack()

L = Label(Frame4_2, text = 'Metamask Address', font = FONT3)
L.pack()

T = Text(Frame4_2, width = 44, height = 1)
T.insert(1.0, KEY)
T.pack()
T.configure(state = 'disabled')



L_user = Label(Frame4_3, textvariable = v_text, font = FONT3)
L_user.pack()

LogoutButton(Frame4_3)

Version(Tab4)


GUI.mainloop()
