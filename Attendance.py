from tkinter import*
from tkinter import scrolledtext as tk
import re
import datetime
from tkinter import font as tkk
fe=datetime.datetime.now()
c=fe.strftime("%d-%m-%y")
de=re.findall(r'\w+',c)
date=de[0]+de[1]
win=Tk()
win.geometry("400x400")
a=["aravind","raj","abi","prem","latha"]
ei=StringVar()
rs=StringVar()
l=Entry(win,textvariable=ei,width=18)
l.grid(row=0,columnspan=2)
w=IntVar()
r=IntVar()
l.insert(15,a[0])
del a[0]
    
def sef():
        if w.get()==1:
            f=open("F:\\"+date,'a+')
            ui=ei.get()+"-present"
            f.write(ui+"\n")
            f.close()
        else:
            if r.get()==1:
              f=open("F:\\"+date,'a+')
              ue=ei.get()+"-absent"
              f.write(ue+"\n")
              f.close()
     
       
def ne():
      
        y=l.get()
        l.delete(0,len(y))
        for i in range(1):
          if len(a)==1:
              w.set(0)
              r.set(0)
              l.insert(0,a[0])
          else:     
            l.insert(0,a[0])
            del a[0]
            w.set(0)
            r.set(0)
                 
def op():
    root=Tk()
    rs=StringVar()
    place=StringVar()
    uw=IntVar()
    ui=IntVar()
    da=Label(root,text="Date:")
    da.grid(row=0,column=0)
    sea=Entry(root,width=18,textvariable=rs)
    sea.grid(row=0,column=1)
    we=Label(root,text="Name:")
    we.grid(row=1,column=0)
    qsa=Entry(root,width=18,textvariable=place)
    qsa.grid(row=1,column=1)   
    def change():
      ew=sea.get()
      ti=re.findall(r'\w+',ew)
      pl=ti[0]+ti[1]
      fe=open("F:\\"+pl,'r')
      x=fe.read()
      tq=re.findall(r'\w+',x)
      uo=tq.index(qsa.get())
      tq[uo+1]=ce.get()
      fe.close()
      ru=open("F:\\"+pl,'w')
      count1=0
      count2=0
      for i in range(len(tq)):
              if i%2==0:
                      if tq[i+1]=="present":
                         count1+=0
                         pi=tq[i]+"-"+tq[i+1]
                         ru.write(pi+"\n")
                      else:
                         count2+=0
                         pi=tq[i]+"-"+tq[i+1]
                         ru.write(pi+"\n")
      print(count1)
      print(count2)
      ru.close()

    pr=Label(root,text="replace").grid(row=3,column=0)
    ce=Entry(root,width=18)
    ce.grid(row=3,column=1)
    bc=Button(root,text="change",command=change)
    bc.grid(row=4,columnspan=3)
    root.mainloop()  
b=Checkbutton(win,text="present",variable=w,command=sef)
b.grid(row=1,column=0)
c=Checkbutton(win,text="absent",variable=r,command=sef)
c.grid(row=1,column=1)
f=Button(win,text="next",command=ne).grid(row=2,columnspan=2)
e=Button(win,text="replace",command=op).grid(row=2,column=34)
si=Entry(win,width=18)
si.grid(row=6,columnspan=2)
scroll=Scrollbar(win)
scr=tk.ScrolledText(win,height=5,width=30,yscrollcommand=scroll.set)
scroll.config(command=scr.yview)
scr.grid(row=13,columnspan=13)
def present():
        scr.delete(1.0,END)
        op=si.get()
        li=re.findall(r'\w+',op)
        uy=li[0]+li[1]
        tr=open("F:\\"+uy,'r')
        qs=tr.read()
        we=re.findall(r'\w+',qs)
        tr.close()
        scr.config(fg='blue')
        for i in range(len(we)):
                if i%2!=0:
                        if we[i]=="present":
                                te=we[i-1]+"\n"
                                scr.insert(INSERT,te)
                           
gt=Button(win,text="present",command=present).grid(row=13,column=33)
def absent():
        scr.delete(1.0,END)
        op=si.get()
        li=re.findall(r'\w+',op)
        uy=li[0]+li[1]
        tr=open("F:\\"+uy,'r')
        qs=tr.read()
        we=re.findall(r'\w+',qs)
        tr.close()
        scr.config(fg='red')
        for i in range(len(we)):
                if i%2!=0:
                        if we[i]=="absent":
                                te=we[i-1]+"\n"
                                scr.insert(INSERT,te) 
ry=Button(win,text="absent",command=absent).grid(row=13,column=35)


















































































































