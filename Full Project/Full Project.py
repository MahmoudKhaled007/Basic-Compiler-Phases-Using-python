##task1
mystr=input('enter equation')
op_ref=['=','-','+','-','*','/','**']
ide=[]
ide2=[]
st=[]
operators=[]
num=[]
num2=[]
x=''
count=0
flag=False
#for checking if letter capital or small 
for i in range(len(mystr)):
    if 65<=ord(mystr[i])<=90  or  97<=ord(mystr[i])<=123  :
        count=count+1
        st.append(mystr[i])
        ide.append(mystr[i])
        ide2.append('id'+str(count))
        
        print(f'id{str(count)}',end= '')
        x=x+'id'+str(count)+' '
 #numbers
    elif mystr[i].isdigit() or mystr[i]=='.':
        st.append(mystr[i])
        num.append(mystr[i])
        if mystr[i]=='.':
            flag=True
        
           
        print(f'{mystr[i]}',end= '')
        x=x+mystr[i]
#operators    
    elif mystr[i] in op_ref:
        
        operators.append(mystr[i])
        print(f' {mystr[i]}',end = '')
        x=x+mystr[i]+' '
    

##task 2

import re
mystr2=input('Please enter an example of Numbers: ')
if re.findall(r'[-+]?[0-9]+$', mystr2):
    print(True)
else:
    print(False)
mystr2=input('Please enter an example of Identifiers: ')
if re.findall(r'^[a-zA-Z]+[_]|^[a-zA-Z]+', mystr2):
    print(True)
else:
    print(False)

mystr2=input('Please enter an example of Reserved Words: ')
if re.findall(r'else$|until$|end$', mystr2):
    print(True)
else:
    print(False) 
mystr2=input('Please enter an example of Special Symbols: ')
if re.findall(r'[<|>]$|=<', mystr2):
    print(True)
else:
    print(False)
    
mystr2=input('Please enter an example of Comments: ')
if re.findall(r'%%[ A-Za-z0-9]+', mystr2):
    print(True)
else:
    print(False)    



##task3

x.strip()
y=x[6:].split('+')
z=y[1].split('*')
g=[]
g.append(y[0])
g.append(z[0])
g.append(z[1])
for i in range(len(g)):
    g[i].strip()

new_num=num[0]+num[1]+num[2]
new_num_Float=float(new_num)



def semantic():
    print('  ','id1'  ,'\n    \\  ' )
    print('       =','   \n         \\    \n           +      \n         /   \\')
    print('     ',g[0],'','  *',' \n            /    \\    \n         ',g[1],g[2])
semantic()



if flag==True:
    try:
        for i in g:
            float(i)
    except:
         str(i)
    print('      ','   id1'  ,'\n            \\  ' )
    print('             =','   \n               \\    \n                +      \n               /    \\')
    print('intToFloat(',g[0],')','  *',' \n                   /    \\    \n                 ',float(g[1]),
          '   intToFloat(',g[2],')')

else:
    semantic()



##task 4
def ICG():
    if flag==True:
        print('T1= ','intToFloat(',ide2[1] ,')')
        print('T2= ','intToFloat(',ide2[2] ,')')
        print('T3= ','T1 ','* ','T2')
        print('T4= ',new_num_Float,'+','T2')
        print(ide2[0],'= ','T4')
    else:  
        print('T1= ',ide2[1],'*',ide2[2])
        print('T2= ',new_num_Float,'+','T1')
        print(ide2[0],'= ','T2')
ICG()        


##Task5
def optimzer():
    if flag==True:
        print('T1= ','#',ide2[1],'*','#',ide2[2])
        print(ide2[0],'= ','T1','+',new_num_Float)
    else:
        print('T1= ',ide2[1],'*',ide2[2])
        print(ide2[0],'= ','T1','+',new_num_Float)
optimzer()        


##Task6
def CodeGenertor():
    if flag==True:
        print('LDF','R1','R1',ide2[1])
        print('MULF','R1','R1',ide2[2])
        print('LDF','R2','R1')
        print('ADDF','R2','R2',new_num_Float)
        print('STRF',ide2[0],'R2')
    else:        
        print('LD','R1','R1',ide2[1])
        print('MUL','R1','R1',ide2[2])
        print('LD','R2','R1')
        print('ADD','R2','R2',new_num_Float)
        print('STR',ide2[0],'R2')
CodeGenertor()              
