from tkinter import *
import math
root=Tk()
root.title("Scientific Calculator")

box=Entry(root,borderwidth=5,width=45)
box.grid(row=0,column=0,columnspan=5,padx=10,pady=5)

def num(number):
    num=box.get()
    box.delete(0,END)
    box.insert(0,num+str(number))
def add():
    ad=box.get()
    box.delete(0,END)
    box.insert(0,ad+'+')

def mul():
    mul=box.get()
    box.delete(0,END)
    box.insert(0,mul+'*')

def div():
    mul=box.get()
    box.delete(0,END)
    box.insert(0,mul+'/')

def sub():
    mul=box.get()
    box.delete(0,END)
    box.insert(0,mul+'-')

def power():
    mul=box.get()
    box.delete(0,END)
    box.insert(0,mul+'^')

def roots():
    mul=box.get()
    box.delete(0,END)
    box.insert(0,mul+'root(')

def sin():
    mul=box.get()
    box.delete(0,END)
    box.insert(0,mul+'sin(')

def cos():
    mul=box.get()
    box.delete(0,END)
    box.insert(0,mul+'cos(')

def tan():
    mul=box.get()
    box.delete(0,END)
    box.insert(0,mul+'tan(')

def logs():
    mul=box.get()
    box.delete(0,END)
    box.insert(0,mul+'log(')
    

def ent():
    val=box.get()
    box.delete(0,END)
    count=0
    operator=['+','-','*','/','^','root(','sin','cos','tan','log(']
    for i in operator:
        job=val.count(i)
        count+=1
        if job==1 and count==1:
            j=val.split('+')
            box.insert(0,float(j[0])+float(j[1]))
        elif job==1 and count==2:
            j=val.split('-')
            box.insert(0,float(j[0])-float(j[1]))
        elif job==1 and count==3:
            j=val.split('*')
            box.insert(0,float(j[0])*float(j[1]))
        elif job==1 and count==4:
            j=val.split('/')
            if j[1]=='0':
                box.insert(0,'Error')
            else:
                box.insert(0,float(j[0])/float(j[1]))
        elif job==1 and count==5:
            j=val.split('^')
            box.insert(0,float(j[0])**float(j[1]))
        elif job==1 and count==6:
            j=val.split('root(')
            box.insert(0,float(j[1])**(1/2))
        elif job==1 and count==7:
            j=val.split('sin(')
            box.insert(0,math.sin(float(j[1])))
        elif job==1 and count==8:
            j=val.split('cos(')
            box.insert(0,math.cos(float(j[1])))
        elif job==1 and count==9:
            j=val.split('tan(')
            box.insert(0,math.tan(float(j[1])))
        elif job==1 and count==10:
            j=val.split('log(')
            box.insert(0,math.log(float(j[1]),10))
            

def AC():
    box.delete(0,END)
    
    
butt1=Button(root,text='1',padx=20,pady=20,command=lambda:num(1))
butt2=Button(root,text='2',padx=20,pady=20,command=lambda:num(2))
butt3=Button(root,text='3',padx=20,pady=20,command=lambda:num(3))
butt4=Button(root,text='4',padx=20,pady=20,command=lambda:num(4))
butt5=Button(root,text='5',padx=20,pady=20,command=lambda:num(5))
butt6=Button(root,text='6',padx=20,pady=20,command=lambda:num(6))
butt7=Button(root,text='7',padx=20,pady=20,command=lambda:num(7))
butt8=Button(root,text='8',padx=20,pady=20,command=lambda:num(8))
butt9=Button(root,text='9',padx=20,pady=20,command=lambda:num(9))
butt0=Button(root,text='0',padx=52,pady=20,command=lambda:num(0))
buttd=Button(root,text='.',padx=22,pady=20,command=lambda:num('.'))
buttent=Button(root,text='Enter',padx=13,pady=50,command=ent)
buttac=Button(root,text='AC',padx=15,pady=20,command=AC)

butt_add=Button(root,text='+',padx=20,pady=20,command=add)
butt_sub=Button(root,text='-',padx=21,pady=20,command=sub)
butt_mul=Button(root,text='*',padx=20,pady=20,command=mul)
butt_div=Button(root,text='/',padx=20.5,pady=20,command=div)

butt_root=Button(root,text='root',padx=14,pady=20,command=roots)
butt_power=Button(root,text='^',padx=21,pady=20,command=power)
butt_sin=Button(root,text='sin',padx=17.4,pady=20,command=sin)
butt_cos=Button(root,text='cos',padx=15.6,pady=20,command=cos)
butt_tan=Button(root,text='tan',padx=15.6,pady=20,command=tan)
butt_log=Button(root,text='log',padx=17,pady=20,command=logs)

butt1.grid(row=4,column=0)
butt2.grid(row=4,column=1)
butt3.grid(row=4,column=2)

butt4.grid(row=3,column=0)
butt5.grid(row=3,column=1)
butt6.grid(row=3,column=2)

butt7.grid(row=2,column=0)
butt8.grid(row=2,column=1)
butt9.grid(row=2,column=2)

butt0.grid(row=5,column=0,columnspan=2)
buttd.grid(row=5,column=2)
buttent.grid(row=4,column=4,rowspan=2)

buttac.grid(row=1,column=0)

butt_add.grid(row=2,column=4)
butt_sub.grid(row=1,column=4)
butt_mul.grid(row=1,column=1)
butt_div.grid(row=1,column=2)

butt_root.grid(row=1,column=3)
butt_power.grid(row=2,column=3)
butt_sin.grid(row=3,column=3)
butt_cos.grid(row=4,column=3)
butt_tan.grid(row=5,column=3)
butt_log.grid(row=3,column=4)

root.mainloop()

