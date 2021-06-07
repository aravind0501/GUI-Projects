from tkinter import*
root= Tk()
ey=[]
tip=[]
g=[]
we=1
ui=0
root.geometry("800x2000")
ge=Menu(root)
root.config(menu=ge)
he=Menu(ge)
ge.add_cascade(label="find",menu=he)
def show():
    gri=Tk()
    fr=Label(gri,text="word").grid(row=0,column=0)
    sq=Entry(gri)
    sq.grid(row=0,column=1)
    def find():
      total=0  
      ep=fri.get(1.0,END).splitlines()
      for h in range(len(ep)):
          rt=ep[h]
          t=rt.split()
          for i in range(len(t)):
              c=[]
              s=len(t[i])+1
              if t[i]==sq.get():
                  c.append(total)
                  total+=s
                  c.append(total)
                  c.append(h+1)
                  g.append(c)
                  continue
              total+=s
          total=0
      for e in range(len(g)): 
           ti=str(g[e][2])+'.'+str(g[e][0])
           op=str(g[e][2])+'.'+str(g[e][1])
           fri.tag_add('one',ti,op)
           fri.tag_config('one',foreground="red")
    opi=Button(gri,text="find",command=find)
    opi.grid(row=1,column=2)
    
he.add_command(label="show",command=show)
hi=Menu(ge)
ge.add_cascade(label="replace  all",menu=hi)
def showi():
    groot=Tk()
    fw=Label(groot,text="word").grid(row=0,column=0)
    se=Entry(groot)
    se.grid(row=0,column=1)
    ft=Label(groot,text="replace")
    ft.grid(row=1,column=0)
    fu=Entry(groot)
    fu.grid(row=1,column=1)
    def change():
        cou=0
        f=0
        v=fri.get(1.0,END).splitlines()
        for i in range(len(v)):
            te=[]
            tu=[]
            t=v[i]
            er=t.split()
            r=er.count(se.get())
            if r:
              for e in range(len(er)):
               if er[e]==se.get():
                 del er[e]
                 er.insert(e,fu.get())
              for i in range(len(er)):
                te.append(er[i])
              ey.append(te)
            else:  
              for i in range(len(er)):
                  te.append(er[i])
              ey.append(te)
        fri.delete(1.0,END)
        for u in range(len(ey)): 
            qw=ey[u]
            out=" ".join(qw)
            fri.insert(END,out+"\n")             
    op=Button(groot,text="change",command=change)
    op.grid(row=2,column=2)
hi.add_command(label="show",command=showi)
hk=Menu(ge)
ge.add_cascade(label="replace ",menu=hk)
def showe():
    grt=Tk()
    fq=Label(grt,text="word").grid(row=0,column=0)
    so=Entry(grt)
    so.grid(row=0,column=1)
    fp=Label(grt,text="replace")
    fp.grid(row=1,column=0)
    fc=Entry(grt)
    fc.grid(row=1,column=1)  
    def change():
        v=fri.get(1.0,END).splitlines()
        cnt=0
        print(v)
        for i in range(len(v)):
            te=[]
            tu=[]
            t=v[i]
            er=t.split()
            r=er.count(so.get())
            if r:
              for e in range(len(er)):
               if cnt==1:
                   break;
                   
               if er[e]==so.get():
                 cnt+=1
                 del er[e]
                 er.insert(e,fc.get())
              for i in range(len(er)):
                te.append(er[i])
              ey.append(te)
            else:  
              for i in range(len(er)):
                  te.append(er[i])
              ey.append(te)
        fri.delete(1.0,END)
        for u in range(len(ey)):
            qw=ey[u]
            out=" ".join(qw)
            fri.insert(END,out+"\n")
    
    opi=Button(grt,text="change",command=change)
    opi.grid(row=2,column=2)
    
hk.add_command(label="show",command=showe)            
hy=Menu(ge)
ge.add_cascade(label="close",menu=hy)
def close():
    exit()
hy.add_command(label="exit",command=close)
fri=Text(root,height=800,width=10000,fg="black")
fri.pack()
with open("E:\\EEE.txt",'r') as fe:
    c=fe.read()
fri.insert(1.0,c)
root.mainloop()
                           
