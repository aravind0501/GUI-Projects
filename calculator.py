from tkinter import*
import re

root=Tk()
enter=StringVar()
dis=Entry(root,textvariable=enter,width=20)
dis.grid(row=0,columnspan=5)
def seven():
    dis.insert(15,'7')
seven=Button(root,text='7',command=seven)
seven.grid(row=1,column=0)
def eight():
    dis.insert(15,'8')
   # dis.focus()
eight=Button(root,text='8',command=eight).grid(row=1,column=1)            
nine=Button(root,text='9',command=lambda:dis.insert(15,'9')).grid(row=1,column=2)             
plus=Button(root,text='+',command=lambda:dis.insert(15,'+')).grid(row=1,column=3)
four=Button(root,text='4',command=lambda:dis.insert(15,'4')).grid(row=2,column=0)
five=Button(root,text='5',command=lambda:dis.insert(15,'5')).grid(row=2,column=1)
six=Button(root,text='6',command=lambda:dis.insert(15,'6')).grid(row=2,column=2)
minus=Button(root,text='-',command=lambda:dis.insert(15,'-')).grid(row=2,column=3)
one=Button(root,text='1',command=lambda:dis.insert(15,'1')).grid(row=3,column=0)
two=Button(root,text='2',command=lambda:dis.insert(15,'2')).grid(row=3,column=1)
three=Button(root,text='3',command=lambda:dis.insert(15,'3')).grid(row=3,column=2)
star=Button(root,text='*',command=lambda:dis.insert(15,'*')).grid(row=3,column=3)
zero=Button(root,text='0',command=lambda:dis.insert(15,'0')).grid(row=4,column=0) 
delete=Button(root,text='del',command=lambda:dis.delete(0,len(enter.get()))).grid(row=4,column=1)
def equal():
    q=enter.get()
    a=[]
    s=re.findall("\d+",q)
    s1=re.findall("\W+",q)
    count=0
    count2=0
    count3=0
    count4=0
    u=[]
    b=0
    d=[]
    c=0
    t=[]
    for i in range(len(s+s1)):
      if i%2==0:
        count2+=1
        if count2>1:
             a.append(s[count2-1])
             continue;        
        a.append(s[0])     
      else:
        r=s1[count] in ['*','/']          
        if r:
            a.append(s1[count])
            d.append(s1[count])
        else:
            a.append(s1[count])
            t.append(s1[count])
        count+=1
    for f in range(len(d)):
      count3+=1
      if d[f]=='*':
        b=a.index("*")
        c1=int(a[b-1])
        c2=int(a[b+1])
        c=c1*c2
        #print(c)
      if d[f]=='/':
        b=a.index("/")
        c1=int(a[b-1])
        c2=int(a[b+1])
        c=c1/c2
      
      for o in range(len(a)):
        
        if b-1==o or b==o or b+1==o:  
            continue;
        u.append(a[o])
      u.insert(b-1,c)    
      a.clear()    
      for i in range(len(u)):
        a.append(u[i])
      u.clear()
    
    for h in range(len(t)):
        count4+=1
        if t[h]=='+':
          b=a.index("+")
          c1=int(a[b-1])
          c2=int(a[b+1])
          c=c1+c2
        if t[h]=='-':
          b=a.index("-")
          c=int(a[b-1])-int(a[b+1])
       
        
                            
        for p in range(len(a)):
        
          if b-1==p or b==p or b+1==p:  
            continue;
          u.append(a[p])
        u.insert(b-1,c)    
        a.clear()    
        for i in range(len(u)):
           a.append(u[i])
        u.clear()
    e="".join(map(str,a))
    dis.delete(0,len(q))
    dis.insert(0,e)
equal=Button(root,text="=",command=equal).grid(row=4,column=2)
divide=Button(root,text='/',command=lambda:dis.insert(15,'/')).grid(row=4,column=3)

                                                      
















