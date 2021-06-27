from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np
import requests
import bs4
import re


#******************************* Functions *******************************************

def f1():
	ent_rno.delete(0,END)
	ent_name.delete(0,END)	
	ent_marks.delete(0,END)
	add.deiconify()
	root.withdraw()
	

def f2():
	root.deiconify()
	add.withdraw()

def f3():
	scrol.configure(state='normal')
	scrol.delete(1.0,END)
	view.deiconify()
	root.withdraw()
	
	con=None
	try:
		con=connect("sms.db")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:
			info="  Roll no :  " +  str(d[0]) +  "  ||  "   + "  Name :  " +  str(d[1])  +  "  ||  "  +  "  Marks :  "  +  str(d[2])  +  "\n"
			scrol.insert(INSERT,info)
		con.commit()
		scrol.configure(state='disabled')
	except Exception as e:
		print("Isssue ",e)
		con.rollback()
	else:
		if con is not None:
			con.close()
			print("Closed")

def f4():
	root.deiconify()
	view.withdraw()

def f5():
	ent_rno1.delete(0,END)
	ent_name1.delete(0,END)	
	ent_marks1.delete(0,END)
	update.deiconify()
	root.withdraw()

def f6():
	root.deiconify()
	update.withdraw()

def f7():
	ent_rno2.delete(0,END)
	delete.deiconify()
	root.withdraw()

def f8():
	root.deiconify()
	delete.withdraw()

def saveadd():
	rollno=ent_rno.get()
	sname=ent_name.get()
	smarks=ent_marks.get()
	rolllist=[]
	con=None
	if rollno=="":
		showerror("Error","Fill the roll number!")
	elif rollno.isalpha()==True:
		showerror("Error","Entered roll number is not in digits!")
	elif rollno.isdigit()==False:
		showerror("Error"," Roll no should be in Positive integers only")
	elif int(rollno)<0:
		showerror("Error","Roll number can't be below 0!")
	elif sname=="" :
		showerror("Error","Fill the name!")
	elif sname.isalpha()==False:
		showerror("Error","Name should be in Alphabets only!")
	elif len(sname)<2:
		showerror("Error","Length of name should be greator than 2 charaters!")
	elif smarks=="":
		showerror("Error","Fill the marks!")
	elif smarks.isalpha()==True:
		showerror("Error","Entered marks is not in digits!")
	elif smarks.isdigit()==False:
		showerror("Error","Marks should be in Positive 0-100 integers only")
	elif int(smarks)<0:
		showerror("Error","Enter positive value of marks!")
	elif int(smarks)>100:
		showerror("Error","Enter marks upto 100!")
	else:
		try:
			con=connect("sms.db")
			cursor=con.cursor()
			sql3="select roll from student"
			cursor.execute(sql3)
			z=cursor.fetchall()
			for i in z:
				rolllist.append(i[0])
			print(rolllist)
			if int(rollno) in rolllist:
				showerror("Information","Already present")
			else:
				sql="insert into student values('%d','%s','%d')"
				print(type(rollno))
				print(rollno)
				cursor.execute(sql % (int(rollno),sname,int(smarks)))
				con.commit()
				print("Record added")
				showinfo("Information","Record Added Successfully!")
				ent_rno.delete(0,END)
				ent_name.delete(0,END)
				ent_marks.delete(0,END)
				ent_rno.focus()
		except Exception as e:
			print("issue created ",e)
			con.rollback()
		else:
			if con is not None:
				con.close()
				print("Closed")
	ent_rno.delete(0,END)
	ent_name.delete(0,END)
	ent_marks.delete(0,END)
	ent_rno.focus()
def updatesave():
	rollno=(ent_rno1.get())
	name=(ent_name1.get())	
	marks=(ent_marks1.get())
	updateroll=[]
	con=None
	if rollno=="":
		showerror("Error","Fill the roll number!")
		ent_rno1.delete(0,END)
		ent_name1.delete(0,END)	
		ent_marks1.delete(0,END)
		ent_rno1.focus()
	elif rollno.isalpha()==True:
		showerror("Error","Entered roll number is not in digits!")
		ent_rno1.delete(0,END)
		ent_name1.delete(0,END)	
		ent_marks1.delete(0,END)
		ent_rno1.focus()
	elif rollno.isdigit()==False:
		showerror("Error"," Roll no should be in Positive integers only")
	elif int(rollno)<0:
		showerror("Error","Roll number can't be below 0!")
		ent_rno1.delete(0,END)
		ent_name1.delete(0,END)	
		ent_marks1.delete(0,END)
		ent_rno1.focus()
	elif name=="" :
		showerror("Error","Fill the name!")
		ent_rno1.delete(0,END)
		ent_name1.delete(0,END)	
		ent_marks1.delete(0,END)
		ent_rno1.focus()
	elif name.isalpha()==False:
		showerror("Error","Name should be in Alphabets only!")
		ent_rno1.delete(0,END)
		ent_name1.delete(0,END)	
		ent_marks1.delete(0,END)
		ent_rno1.focus()
	elif len(name)<2:
		showerror("Error","Length of name should be greator than 2 charaters!")
		ent_rno1.delete(0,END)
		ent_name1.delete(0,END)	
		ent_marks1.delete(0,END)
	elif marks=="":
		showerror("Error","Fill the marks!")
		ent_rno1.delete(0,END)
		ent_name1.delete(0,END)	
		ent_marks1.delete(0,END)
		ent_rno1.focus()
	elif marks.isalpha()==True:
		showerror("Error","Entered marks is not in digits!")
		ent_rno1.delete(0,END)
		ent_name1.delete(0,END)	
		ent_marks1.delete(0,END)
		ent_rno1.focus()
	elif marks.isdigit()==False:
		showerror("Error","Marks should be in Positive 0-100 integers only")
	elif int(marks)<0:
		showerror("Error","Enter positive value of marks!")
		ent_rno1.delete(0,END)
		ent_name1.delete(0,END)	
		ent_marks1.delete(0,END)
		ent_rno1.focus()
	elif int(marks)>100:
		showerror("Error","Enter marks upto 100!")
		ent_rno1.delete(0,END)
		ent_name1.delete(0,END)	
		ent_marks1.delete(0,END)
		ent_rno1.focus()
	else:
		try:
			con=connect("sms.db")
			cursor=con.cursor()
			sql3="select roll from student"
			cursor.execute(sql3)
			rollnm=int(rollno)
			w=cursor.fetchall()
			for i in w:
				updateroll.append(i[0])
			if int(rollnm) not in updateroll:
				showerror("Information","Roll no is not present! Can't update")
			else:
				con=connect("sms.db")
				cursor=con.cursor()
				sql="update student set name='%s',marks='%d' where roll='%d'"
				cursor.execute(sql%(name,int(marks),int(rollnm)))
				con.commit()
				print("Record updated")
				showinfo("Information","Record updated Successfully!")
				ent_rno1.delete(0,END)
				ent_name1.delete(0,END)	
				ent_marks1.delete(0,END)
				ent_rno1.focus()
		except Exception as e:
			print("issue created ",e)
			con.rollback()
		else:
			if con is not None:
				con.close()
				print("Closed")
	ent_rno1.delete(0,END)
	ent_name1.delete(0,END)	
	ent_marks1.delete(0,END)
	
def deletesave():
	rollno=ent_rno2.get()
	con=None
	deleteroll=[]
	if rollno=="":
		showerror("Error","Fill the roll number!")
		ent_rno2.delete(0,END)
		ent_rno2.focus()
	elif rollno.isalpha()==True:
		showerror("Error","Entered roll number is not in digits!")
		ent_rno2.delete(0,END)
		ent_rno2.focus()
	elif rollno.isdigit()==False:
		showerror("Error"," Roll no should be in Positive integers only")
		ent_rno2.delete(0,END)
		ent_rno2.focus()
	elif int(rollno)<0:
		showerror("Error","Roll number can't be below 0!")
		ent_rno2.delete(0,END)
		ent_rno2.focus()
	else:
		try:
			con=connect("sms.db")
			cursor=con.cursor()
			sql3="select roll from student"
			cursor.execute(sql3)
			q=cursor.fetchall()
			rollnm=int(rollno)
			for i in q:
				deleteroll.append(i[0])
			if int(rollnm) not in deleteroll:
				showerror("Information","Roll no is not present! Can't delete")
			else:
				con=connect("sms.db")
				cursor=con.cursor()
				sql="delete from student where roll='%d'"
				cursor.execute(sql%(int(rollnm)))
				con.commit()
				print("Record Deleted")
				showinfo("Information","Record deleted Successfully!")
				ent_rno2.delete(0,END)
				ent_rno2.focus()
		except Exception as e:
			print("issue created ",e)
			con.rollback()
		else:
			if con is not None:
				con.close()
				print("Closed")
				ent_rno2.delete(0,END)
def charts():
	#name=ent_name1.get()	
	#marks=int(ent_marks1.get())
	con=None
	x=[]
	y=[]
	try:
		con=connect("sms.db")
		cursor=con.cursor()
		sql1="select marks from student"
		p=cursor.execute(sql1)
		print(p)
		x1=cursor.fetchall()
		for i in x1:
			x.append(i[0])
		sql2="select name from student"
		cursor.execute(sql2)
		y1=cursor.fetchall()
		for p in y1:
			y.append(p[0])
		plt.bar(y,x,label="student",color=['blue','red','green'])
		plt.xlabel("Student name")
		plt.ylabel("Student's marks")
		plt.title("Student's Performance")
		plt.legend()
		plt.show()
	except Exception as e:
		print("issue created ",e)
		con.rollback()
	else:
		if con is not None:
			con.close()
			print("Closed")


def Quote():
	
	try:
		wa="https://www.brainyquote.com/quote_of_the_day"
		res=requests.get(wa)
		#print(res)
		data=bs4.BeautifulSoup(res.text,"html.parser")
		#print("data")
		info=data.find("img",{"class":"p-qotd"})
		#print(info)
		Q.set(info['alt'])
		#print(" Good thoughts : ",qots)
	except Exception as e:
		print("Issue ",e)
def temp():
	try:
		a1="https://api.openweathermap.org/data/2.5/weather?units=metric"
		a2="&q=" + "kalyan"
		a3="&appid=" + "c6e315d09197cec231495138183954bd"
		wa=a1+a2+a3
		res=requests.get(wa)
		#print(res)        #200 okk
		data=res.json()
		T.set(data['main']['temp'])
		#print("temp= ",temp)
	except Exception as e:
		print("issue",e)
def location():
	try:
		wa="https://ipinfo.io/"
		res=requests.get(wa)
		#print(res)        #200 okk

		data=res.json()
		#print(data)
		L.set(data['city'])
	except Exception as e:
		print("Issue",e)
	
	
		

#**************************** Main window ***************************************************
root=Tk()
root.title("S.M.S")
root.geometry("750x600+300+150")
root.configure(bg='navy')
T=StringVar()
Q=StringVar()
L=StringVar()
f=("Bahnschrift SemiBold SemiConden",10,"normal")
btn_add=Button(root,text="Add",width=15,height=2,font=f,bg="white",command=f1)
btn_view=Button(root,text="View",width=15,height=2,font=f,bg="white",command=f3)
btn_update=Button(root,text="Update",width=15,height=2,font=f,bg="white",command=f5)
btn_delete=Button(root,text="Delete",width=15,height=2,font=f,bg="white",command=f7)
btn_charts=Button(root,text="Charts",width=15,height=2,font=f,bg="white",command=charts)

special=("Bahnschrift SemiBold SemiConden",22,"italic")
special1=("Bahnschrift SemiBold SemiConden",14,"normal")
lbl_sms=Label(root,text="Student Management System",font=special,foreground="navy")
lbl_line1=Label(root,text="___________________________________________________________________________________________________________________________________________________")
lbl_location=Label(root,text="Location : ",font=special1)
lbl_loc=Label(root,textvariable=L,font=special1,foreground="navy")
lbl_temp=Label(root,text="Temp : ",font=special1)
lbl_temperature=Label(root,textvariable=T,font=special1,foreground="navy")
lbl_line2=Label(root,text="___________________________________________________________________________________________________________________________________________________")
lbl_qotd=Label(root,text="QOTD : ",font=special1)
lbl_qoute=Label(root,textvariable=Q,font=special1,foreground="navy")
lbl_line3=Label(root,text="___________________________________________________________________________________________________________________________________________________")
Quote()

temp()

location()





lbl_sms.place(x=220,y=10)
btn_add.place(x=290,y=100)
btn_view.place(x=290,y=150)
btn_update.place(x=290,y=200)
btn_delete.place(x=290,y=250)
btn_charts.place(x=290,y=300)
lbl_line1.place(x=1,y=360)
lbl_location.place(x=10,y=390)
lbl_loc.place(x=120,y=390)
lbl_temp.place(x=290,y=390)
lbl_temperature.place(x=380,y=390)
lbl_line2.place(x=1,y=430)
lbl_qotd.place(x=10,y=470)
lbl_qoute.place(x=5,y=520)
lbl_line3.place(x=1,y=570)

#********************* ADD STUDENT ****************************

add=Toplevel(root)
add.title("Add Student")
add.geometry("750x600+300+150")
add.configure(bg="navy")
lbl_addstud=Label(add,text="Add Student",font=special,foreground="navy")
f1=("Bahnschrift SemiBold SemiConden",18,"normal")
lbl_rno=Label(add,text="Enter Roll no. : ",font=f1)
ent_rno=Entry(add,border=5,width=29,font=f1)
lbl_name=Label(add,text="Enter Name : ",font=f1)
ent_name=Entry(add,border=5,font=f1,width=29)
lbl_marks=Label(add,text="Enter Marks : ",font=f1)
ent_marks=Entry(add,border=5,font=f1,width=29)
btn_save=Button(add,text="Save",font=f1,bg="white",command=saveadd)
btn_back=Button(add,text="Back",font=f1,bg="white",command=f2)

lbl_addstud.place(x=300,y=10)
lbl_rno.place(x=300,y=100)
ent_rno.place(x=190,y=150)
lbl_name.place(x=300,y=200)
ent_name.place(x=190,y=250)
lbl_marks.place(x=300,y=300)
ent_marks.place(x=190,y=350)
btn_save.place(x=350,y=430)
btn_back.place(x=350,y=490)
add.withdraw()

#***************** View student **************************

view=Toplevel(root)
view.title("View Student")
view.geometry("750x600+300+150")
view.configure(bg="navy")

scrol=ScrolledText(view,width=100,height=25,font=f)
btn_back=Button(view,font=f1,text="Back",bg="white",command=f4)
scrol.place(x=50,y=40)
btn_back.place(x=330,y=520)
view.withdraw()

#********************** Update student *****************************
update=Toplevel(root)
update.title("Update Student")
update.geometry("750x600+300+150")
update.configure(bg="navy")

lbl_updatestud=Label(update,text="Update Student",font=special,foreground="navy")
lbl_rno=Label(update,text="Enter Roll no. : ",font=f1)
ent_rno1=Entry(update,border=5,width=29,font=f1)
lbl_name=Label(update,text="Enter Name : ",font=f1)
ent_name1=Entry(update,border=5,font=f1,width=29)
btn_save=Button(update,text="Save",font=f1,bg="white",command=updatesave)
btn_back=Button(update,text="Back",font=f1,bg="white",command=f6)
lbl_marks=Label(update,text="Enter Marks : ",font=f1)
ent_marks1=Entry(update,border=5,font=f1,width=29)

lbl_updatestud.place(x=300,y=10)
lbl_rno.place(x=300,y=100)
ent_rno1.place(x=190,y=150)
lbl_name.place(x=300,y=200)
ent_name1.place(x=190,y=250)
lbl_marks.place(x=300,y=300)
ent_marks1.place(x=190,y=350)
btn_save.place(x=350,y=430)
btn_back.place(x=350,y=490)





update.withdraw()

#***************************** delete student **********************************

delete=Toplevel(root)
delete.title("Delete Student")
delete.geometry("750x600+300+150")
delete.configure(bg='navy')

lbl_rno2=Label(delete,text="Enter Roll no. : ",font=f1)
ent_rno2=Entry(delete,border=5,width=29,font=f1)
btn_save2=Button(delete,text="Delete",font=f1,bg="white",command=deletesave)
btn_back2=Button(delete,text="Back",font=f1,bg="white",command=f8)

lbl_rno2.place(x=300,y=150)
ent_rno2.place(x=200,y=200)
btn_save2.place(x=360,y=390)
btn_back2.place(x=360,y=450)
delete.withdraw()





root.mainloop()


























