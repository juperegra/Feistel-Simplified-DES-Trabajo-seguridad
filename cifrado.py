def calculateKi(k1,buffOld):
    #input'11001101' 8 bits
    b='10000000'
    c='11111111'

    buff=bin((int(k1,2)&int(b,2))>>7)

    ne=k1+buffOld[2:]
    
    next2=bin(int(ne,2)&int(c,2))
    
    return [next2,buff]  

def inverseKi(k1,buffOld):
    #input'11001101' 8 bits
    b='00000001'

    buff=bin((int(k1,2)&int(b,2)))

    print('buff',buff)

    ne=buff[2:]+k1
    
    next2=bin(int(ne,2)>>1)
    
    return next2 

def calculateK1(k):
    #input'001111010' 9bits
    b='10000000'
    buffOld=bin((int(k,2)&int(b,2))>>7)

    k1=bin(int(k,2)>>1)
    
    return [k1,buffOld]

def boxS1(p1):
    #input'1101' 4 bits
    s1=[['100','101','110','111','010','001','011','000'],
    ['011','101','000','010','001','100','111','110']]

    p1_1=p1[0]
    p1_2_4=p1[1:]

    numBox1=s1[int(p1_1,2)][int(p1_2_4,2)]
    return numBox1

def boxS2(p2):
    #input'0111' 4 bits
    s2=[['100','000','110','111','101','001','010','011'],
    ['010','101','000','110','001','111','011','100']]

    p2_1=p2[0]
    p2_2_4=p2[1:]

    numBox2=s2[int(p2_1,2)][int(p2_2_4,2)]
    return numBox2

def expansion(a):
    #input'011100' 6 bits
    lista=list(a)

    exp=lista[4]+lista[3]+lista[0]+lista[1]+lista[2]+lista[0]+lista[5]+lista[1]

    return exp



print("Bienvenido")
print("Introduzca el dato a cifrar, tiene que ser de tipo binario con 12 bits")
entrada=input()
dato = list(entrada)
while(len(dato)!=12):
    print("El dato introducido no tiene 12 bits, introduzca un dato valido")
    entrada=input()
    dato=list(entrada)
esBin=False
while(esBin==False):
    for i in range(12):
        if dato[i]!="0" and dato[i]!="1":
            break
        if i==11 and(dato[11]=="0" or dato[11]=="1"):
            esBin=True
    if esBin==False:
        print("Has introducido un dato que no esta en binario, introduce un dato valido")
        entrada=input()
        dato = list(entrada)
        while(len(dato)!=12):
            print("El dato introducido no tiene 12 bits, introduzca un dato valido")
            entrada=input()
            dato=list(entrada)

            
    
print("Introduzca la clave, tiene que ser de tipo binario con 9 bits")
entr=input()
key=list(entr)
while(len(key)!=9):
    print("El dato introducido no tiene 9 bits, introduzca un dato valido")
    entr=input()
    key=list(entr)
esBin=False
while(esBin==False):
    for i in range(9):
        if key[i]!="0" and key[i]!="1":
            break
        if i==8 and(key[8]=="0" or key[8]=="1"):
            esBin=True
    if esBin==False:
        print("Has introducido un dato que no esta en binario, introduce un dato valido")
        entr=input()
        key = list(entr)
        while(len(key)!=9):
            print("El dato introducido no tiene 9 bits, introduzca un dato valido")
            entr=input()
            key=list(entr)

print("Introduzca el  numero deiteraciones que quiere realizar")
n=input()

lik=calculateK1(entr)
k=lik[0]
buffOld=lik[1]

l=entrada[:6]
r=entrada[6:]

listaK=[]

for i in range(int(n)):

    k=k[2:]
    print('K de la iteracion ', i,':',k)
    er=expansion(r)
    
    listaK.append(k)
    erXORk=int(er,2)^int(k,2)
    erXORk=bin(erXORk)
    
    t=erXORk[2:]
    
    le=len(t)
    
    if le == 1:
        t1='0000'
        t2='000'+t
    if le == 2:
        t1='0000'
        t2='00'+t
    if le == 3:
        t1='0000'
        t2='0'+t
    if le == 4:
        t1='0000'
        t2=t
    if le == 5:
        t1='000'+t[0]
        t2=t[1:]
    if le == 6:
        t1='00'+t[:2]
        t2=t[2:]
    if le == 7:
        t1='0'+t[:3]
        t2=t[3:]
    if le == 8:
        t1=t[:4]
        t2=t[4:]
    
    s1=boxS1(t1)
    s2=boxS2(t2)
    f=s1+s2
    l1=l
    l=r
    r=int(l1,2)^int(f,2)
    r=bin(r)
    
    r=r[2:]
    le=len(r)
    if le == 1:
        r='00000'+r
    if le == 2:
        r='0000'+r
    if le == 3:
        r='000'+r
    if le == 4:
        r='00'+r
    if le == 5:
        r='0'+r
    
    lik=calculateKi(k,buffOld)
    k=lik[0]
    buffOld=lik[1]

print('dato cifrado:',r+l)




k=listaK[int(n)-1]

for i in range(int(n)):
    print('it:', i)
    print('k:',k)

    er=expansion(r)
    
    
    erXORk=int(er,2)^int(k,2)
    erXORk=bin(erXORk)
    
    t=erXORk[2:]
    
    le=len(t)
    
    if le == 1:
        t1='0000'
        t2='000'+t
    if le == 2:
        t1='0000'
        t2='00'+t
    if le == 3:
        t1='0000'
        t2='0'+t
    if le == 4:
        t1='0000'
        t2=t
    if le == 5:
        t1='000'+t[0]
        t2=t[1:]
    if le == 6:
        t1='00'+t[:2]
        t2=t[2:]
    if le == 7:
        t1='0'+t[:3]
        t2=t[3:]
    if le == 8:
        t1=t[:4]
        t2=t[4:]

    s1=boxS1(t1)
    s2=boxS2(t2)
    f=s1+s2
    l1=l
    l=r
    r=int(l1,2)^int(f,2)
    r=bin(r)
    
    r=r[2:]
    le=len(r)
    if le == 1:
        r='00000'+r
    if le == 2:
        r='0000'+r
    if le == 3:
        r='000'+r
    if le == 4:
        r='00'+r
    if le == 5:
        r='0'+r
    
    k=listaK[(int(n)-2)-i]

print('dato descifrado:', r+l)

