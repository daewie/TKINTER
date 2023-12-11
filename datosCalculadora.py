from tkinter import *
import math

def calcTotal():
    operacion=texto.get()
    total=eval(operacion)
    texto.delete(0,len(texto.get()))
    texto.insert(len(texto.get()),total)
def handleFactorial():
    operacion=texto.get()
    total=int(eval(operacion))
    fact=math.factorial(total)
    texto.delete(0,len(texto.get()))
    texto.insert(len(texto.get()),fact)


window=Tk()
window.title("Calculadora")
window.config(background="yellow")

texto=Entry(window,font=("arial 20"))
texto.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
sum=Button(window,text="+",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"+"),background="#151515",fg="#ffffff")
sum.grid(row=1,column=0,padx=20,pady=20)
rest=Button(window,text="-",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"-"),background="#151515",fg="#ffffff")
rest.grid(row=1,column=1,padx=1,pady=20)
potencia=Button(window,text="^",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"**"),background="#151515",fg="#ffffff")
potencia.grid(row=2,column=2,padx=20,pady=20)
radicacion=Button(window,text="rad",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"**0.5"),background="#151515",fg="#ffffff")
radicacion.grid(row=1,column=2,padx=1,pady=1)
multi=Button(window,text="*",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"*"),background="#151515",fg="#ffffff")
multi.grid(row=2,column=0,padx=1,pady=1)
factorial=Button(window,text="!",width=5,height=2,command=lambda:handleFactorial(),background="#151515",fg="#ffffff")
factorial.grid(row=2,column=3,padx=1,pady=1)
deleted=Button(window,text="A/C",width=5,height=2,command=lambda:texto.delete(0,len(texto.get())),background="#cc0000")
deleted.grid(row=1,column=3,padx=1,pady=1)
div=Button(window,text="/",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"/"),background="#151515",fg="red")
div.grid(row=2,column=1,padx=1,pady=1)
box0=Button(window,text="0",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"0"),background="white")
box0.grid(row=3,column=0,padx=1,pady=1)
box1=Button(window,text="1",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"1"),background="white")
box1.grid(row=3,column=1,padx=1,pady=1)
box2=Button(window,text="2",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"2"),background="white")
box2.grid(row=3,column=2,padx=1,pady=1)
box3=Button(window,text="3",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"3"),background="white")
box3.grid(row=3,column=3,padx=1,pady=1)
box4=Button(window,text="4",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"4"),background="white")
box4.grid(row=4,column=0,padx=1,pady=1)
box5=Button(window,text="5",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"5"),background="white")
box5.grid(row=4,column=1,padx=1,pady=1)
box6=Button(window,text="6",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"6"),background="white")
box6.grid(row=4,column=2,padx=1,pady=1)
box7=Button(window,text="7",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"7"),background="white")
box7.grid(row=4,column=3,padx=1,pady=1)
box8=Button(window,text="8",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"8"),background="white")
box8.grid(row=5,column=0,padx=1,pady=1)
box9=Button(window,text="9",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"9"),background="white")
box9.grid(row=5,column=1,padx=1,pady=1)
boxp1=Button(window,text="(",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"("),background="white")
boxp1.grid(row=5,column=2,padx=1,pady=1)
boxp2=Button(window,text=")",width=5,height=2,command=lambda:texto.insert(len(texto.get()),")"),background="white")
boxp2.grid(row=5,column=3,padx=1,pady=1)
total=Button(window,text="=",width=30,height=2,command=lambda:calcTotal(),background="white")
total.grid(row=6,column=1,columnspan=3,padx=5,pady=5)
dot=Button(window,text=".",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"."),background="white")
dot.grid(row=6,column=0,padx=1,pady=1)


window.mainloop()