import os

def dir(p,s):
    b=[]
    for i in s:
        d=f'{p}/{i}'
        if os.path.isdir(d):
            if i[0]!='.':
                b.append(i)
    return b

def ser(p,s,h='',l=[],z=0):
    if z==0:
        print(h)
    s=dir(p,s)
    for i in s:
        if s.index(i)>0:
            del l[len(l)-1]
        
        d=f'{p}/{i}'
        if os.path.isdir(d):
            if i!='Android':
                f=os.listdir(d)
                for x in l:
                    print(x,end='')
                l=l[:z]
                if s.index(i)==len(s)-1:
                    print('┗'+i);
                    l.append(' ')
                else:
                    print('┣'+i);
                    l.append('┃')
                ser(d,f,h,l,z+1)
#        elif os.path.isfile(d):
#            if True:
#                #f=os.listdir(d)
#                if s.index(link)==len(s)-1:
#                    for z in l:
#                        print(z,end='')
#                    print('┖'+link)
#                else:
#                    for z in l:
#                        print(z,end='')
#                    print('┠'+link);
            
g=os.getcwd()

ss=os.listdir(g)

s=g[g.rfind('/')+1:]
try:
    ss.remove('Android')
except:
    pass
ser(g,ss,s)