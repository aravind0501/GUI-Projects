from tkinter import*
import re
import itertools
root=Tk()
root.title("TIC TOE")
t1=[(1,2,3),(3,6,9),(7,8,9),(1,4,7),(1,5,9),(3,5,7),(2,5,8),(4,5,6)]
o=[]
p=[]
one=Button(root,width=4,height=4)
one.grid(row=1,column=0)
two=Button(root,width=4,height=4)
two.grid(row=1,column=1)
three=Button(root,width=4,height=4)
three.grid(row=1,column=2)
four=Button(root,width=4,height=4)
four.grid(row=2,column=0)
five=Button(root,width=4,height=4)
five.grid(row=2,column=1)
six=Button(root,width=4,height=4)
six.grid(row=2,column=2)
seven=Button(root,width=4,height=4)
seven.grid(row=3,column=0)
eight=Button(root,width=4,height=4)
eight.grid(row=3,column=1)
nine=Button(root,width=4,height=4)
nine.grid(row=3,column=2)
tr=Text(root,width=30,height=14)
tr.grid(row=0,column=4)
def create(event):
    y=tr.get("1.0","end")
    t=re.findall(r'\w+',y)
    w=0
    s=0
    q=0
    if t[1]=='X':
        u=int(t[0])
        o.append(u)
    else:
        pe=int(t[0])
        p.append(pe)
    tr.delete("1.0","end")
    if int(t[0])==1:
        one.configure(text=t[1])
    if int(t[0])==2:
        two.configure(text=t[1])
    if int(t[0])==3:
        three.configure(text=t[1])
    if int(t[0])==4:
        four.configure(text=t[1])
    if int(t[0])==5:
        five.configure(text=t[1])
    if int(t[0])==6:
        six.configure(text=t[1])
    if int(t[0])==7:
        seven.configure(text=t[1])
    if int(t[0])==8:
        eight.configure(text=t[1])
    if int(t[0])==9:
        nine.configure(text=t[1])
    t.clear()
    if len(o)>2:
        ie=itertools.permutations(o,3)
        po=[y for y in ie]
        for u in range(len(po)):
            ui=po[u]
            er=ui in  t1
            if er:
                for pi in range(len(ui)):
                    if ui[pi]==1:
                      one.configure(fg="green")
                      w+=1
                    if  ui[pi]==2:  
                       two.configure(fg="green")
                       w+=1
                    if  ui[pi]==3:
                        three.configure(fg="green")
                        w+=1
                    if   ui[pi]==4:
                        four.configure(fg="green")
                        w+=1
                    if   ui[pi]==5:
                        five.configure(fg="green")
                        w+=1
                    if  ui[pi]==6:
                        six.configure(fg="green")
                        w+=1
                    if  ui[pi]==7:
                        seven.configure(fg="green")
                        w+=1
                    if  ui[pi]==8:
                        eight.configure(fg="green")
                        w+=1
                    if  ui[pi]==9:
                        nine.configure(fg="green")
                        w+=1
    if w==3:
        tr.insert(END,"X win the game")
        tr.configure(state="disabled")
    if len(p)>2:
        ie=itertools.permutations(p,3)
        po=[y for y in ie]
        for u in range(len(po)):
            ui=po[u]
            er=ui in  t1
            if er:
                for pi in range(len(ui)):
                    if ui[pi]==1:
                      one.configure(fg="green")
                      q+=1
                    if  ui[pi]==2:  
                       two.configure(fg="green")
                       q+=1
                    if  ui[pi]==3:
                        three.configure(fg="green")
                        q+=1
                    if   ui[pi]==4:
                        four.configure(fg="green")
                        q+=1
                    if   ui[pi]==5:
                        five.configure(fg="green")
                        q+=1
                    if  ui[pi]==6:
                        six.configure(fg="green")
                        q+=1
                    if  ui[pi]==7:
                        seven.configure(fg="green")
                        q+=1
                    if  ui[pi]==8:
                        eight.configure(fg="green")
                        q+=1
                    if  ui[pi]==9:
                        nine.configure(fg="green")                     
                        q+=1
    if q==3:
        tr.insert(END,"O  win the game")
        tr.configure(state="disabled")
root.bind("<Return>",create)            
we=Button(root,text="enter")
we.grid(row=2,column=4)

