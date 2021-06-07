from tkinter import*
from tkinter.ttk import Combobox
import re
from textblob import TextBlob
win=Tk()
lo=StringVar()
li=StringVar()
dr={"french":'fr',"spanish":'es',"chinese":"zh","tamil":"ta"}
win.geometry("850x250")
bc=Combobox(win,values=["french","english","spanish"],textvariable=li)
bc.set("select languge")
bc.pack(anchor=NW)
fc=Combobox(win,values=["french","chinese","spanish","tamil"],textvariable=lo)
fc.set("select language")
fc.pack(anchor=NE)
po=Text(win,width=23)
po.pack(side=LEFT)
gh=Text(win,width=23)
gh.pack(side=RIGHT)
def key():
    ui=li.get()

    f=open("E:\\"+ui,"r")
    er=f.read()
    ty=re.findall(r'\w+',er)
    print(ty)
    root=Tk()
    root.geometry("450x150")
    br=Frame(root,width=450,height=150)
    br.pack()
    q=Button(br,text="q",width=5,command=lambda:po.insert(15.0,"q"))
    q.grid(row=0,column=0)
    w=Button(br,text="w",width=5,command=lambda:po.insert(15.0,"w"))
    w.grid(row=0,column=1)
    e=Button(br,text="e",width=5,command=lambda:po.insert(15.0,"e"))
    e.grid(row=0,column=2)
    r=Button(br,text="r",width=5,command=lambda:po.insert(15.0,"r"))
    r.grid(row=0,column=3)
    t=Button(br,text="t",width=5,command=lambda:po.insert(15.0,"t"))
    t.grid(row=0,column=4)
    y=Button(br,text="y",width=5,command=lambda:po.insert(15.0,"y"))
    y.grid(row=0,column=5)
    u=Button(br,text="u",width=5,command=lambda:po.insert(15.0,"u"))
    u.grid(row=0,column=6)
    i=Button(br,text="i",width=6,command=lambda:po.insert(15.0,"i"))
    i.grid(row=0,column=7)
    o=Button(br,text="o",width=5,command=lambda:po.insert(15.0,"o"))
    o.grid(row=0,column=8)
    p=Button(br,text="p",width=5,command=lambda:po.insert(15.0,"p"))
    p.grid(row=0,column=9)
    a=Button(br,text='a',width=5,command=lambda:po.insert(15.0,"a"))
    a.grid(row=1,column=0)
    s=Button(br,text="s",width=5,command=lambda:po.insert(15.0,"s"))
    s.grid(row=1,column=1)
    d=Button(br,text="d",width=5,command=lambda:po.insert(15.0,"d"))
    d.grid(row=1,column=2)
    f=Button(br,text="f",width=5,command=lambda:po.insert(15.0,"f"))
    f.grid(row=1,column=3)
    g=Button(br,text="g",width=5,command=lambda:po.insert(15.0,"g"))
    g.grid(row=1,column=4)
    h=Button(br,text="h",width=5,command=lambda:po.insert(15.0,"h"))
    h.grid(row=1,column=5)
    j=Button(br,text="j",width=5,command=lambda:po.insert(15.0,"j"))
    j.grid(row=1,column=6)
    k=Button(br,text="k",width=6,command=lambda:po.insert(15.0,"k"))
    k.grid(row=1,column=7)
    l=Button(br,text="l",width=5,command=lambda:po.insert(15.0,"l"))
    l.grid(row=1,column=8)
    z=Button(br,text="z",width=5,command=lambda:po.insert(15.0,"z"))
    z.grid(row=1,column=9)
    x=Button(br,text="x",width=5,command=lambda:po.insert(15.0,"x"))
    x.grid(row=2,column=0)
    c=Button(br,text="c",width=5,command=lambda:po.insert(15.0,"c"))
    c.grid(row=2,column=1)
    v=Button(br,text="v",width=5,command=lambda:po.insert(15.0,"v"))
    v.grid(row=2,column=2)
    b=Button(br,text="b",width=5,command=lambda:po.insert(15.0,"b"))
    b.grid(row=2,column=3)
    n=Button(br,text="n",width=5,command=lambda:po.insert(15.0,"n"))
    n.grid(row=2,column=4)
    m=Button(br,text="m",width=5,command=lambda:po.insert(15.0,"m"))
    m.grid(row=2,column=5)
    de=Button(br,text="DEL",width=5).grid(row=2,column=6)
    def caps():
         bre=Frame(root)
         bre.pack()
         br.pack_forget()
         q=Button(bre,text="Q",width=5,command=lambda:po.insert(15.0,"Q"))
         q.grid(row=0,column=0)
         w=Button(bre,text="W",width=5,command=lambda:po.insert(15.0,"W"))
         w.grid(row=0,column=1)
         e=Button(bre,text="E",width=5,command=lambda:po.insert(15.0,"E"))
         e.grid(row=0,column=2)
         r=Button(bre,text="R",width=5,command=lambda:po.insert(15.0,"R"))
         r.grid(row=0,column=3)
         t=Button(bre,text="T",width=5,command=lambda:po.insert(15.0,"T"))
         t.grid(row=0,column=4)
         y=Button(bre,text="Y",width=5,command=lambda:po.insert(15.0,"Y"))
         y.grid(row=0,column=5)
         u=Button(bre,text="U",width=5,command=lambda:po.insert(15.0,"U"))
         u.grid(row=0,column=6)
         i=Button(bre,text="I",width=6,command=lambda:po.insert(15.0,"I"))
         i.grid(row=0,column=7)
         o=Button(bre,text="O",width=5,command=lambda:po.insert(15.0,"O"))
         o.grid(row=0,column=8)
         p=Button(bre,text="P",width=5,command=lambda:po.insert(15.0,"P"))
         p.grid(row=0,column=9)
         a=Button(bre,text='A',width=5,command=lambda:po.insert(15.0,"A"))
         a.grid(row=1,column=0)
         s=Button(bre,text="S",width=5,command=lambda:po.insert(15.0,"S"))
         s.grid(row=1,column=1)
         d=Button(bre,text="D",width=5,command=lambda:po.insert(15.0,"D"))
         d.grid(row=1,column=2)
         f=Button(bre,text="F",width=5,command=lambda:po.insert(15.0,"F"))
         f.grid(row=1,column=3)
         g=Button(bre,text="G",width=5,command=lambda:po.insert(15.0,"G"))
         g.grid(row=1,column=4)
         h=Button(bre,text="H",width=5,command=lambda:po.insert(15.0,"H"))
         h.grid(row=1,column=5)
         j=Button(bre,text="J",width=5,command=lambda:po.insert(15.0,"J"))
         j.grid(row=1,column=6)
         k=Button(bre,text="K",width=6,command=lambda:po.insert(15.0,"K"))
         k.grid(row=1,column=7)
         l=Button(bre,text="L",width=5,command=lambda:po.insert(15.0,"L"))
         l.grid(row=1,column=8)
         z=Button(bre,text="Z",width=5,command=lambda:po.insert(15.0,"Z"))
         z.grid(row=1,column=9)
         x=Button(bre,text="X",width=5,command=lambda:po.insert(15.0,"X"))
         x.grid(row=2,column=0)
         c=Button(bre,text="C",width=5,command=lambda:po.insert(15.0,"C"))
         c.grid(row=2,column=1)
         v=Button(bre,text="V",width=5,command=lambda:po.insert(15.0,"V"))
         v.grid(row=2,column=2)
         b=Button(bre,text="B",width=5,command=lambda:po.insert(15.0,"B"))
         b.grid(row=2,column=3)
         n=Button(bre,text="N",width=5,command=lambda:po.insert(15.0,"N"))
         n.grid(row=2,column=4)
         m=Button(bre,text="M",width=5,command=lambda:po.insert(15.0,"M"))
         m.grid(row=2,column=5)
         de=Button(bre,text="DEL",width=5)
         de.grid(row=2,column=6)
         
         def back():
             bre.pack_forget()
             br.pack()
         we=Button(bre,text="Back",width=6,command=back)
         we.grid(row=2,column=7)
         
         
        
    se=Button(br,text="caps lock",width=6,command=caps).grid(row=2,column=7)
def ente(event):
    pi=lo.get()
    ki=po.get("1.0","end")
    blob=TextBlob(ki)
    fr=blob.translate(to=dr[pi])
    gh.insert(END,fr+"\n")
        
op=Button(win,text="keyboard",command=key)
op.pack(anchor=NW)
win.bind("<Control-c>",ente)
ent=Button(win,text="enter")
#win.bind("<Control-c>",ente)
ent.pack(side=TOP)


