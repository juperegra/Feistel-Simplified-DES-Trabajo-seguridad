#Creado por Juan Pérez Gracia
#He tomado la decicision de trabajar con strings
#Cada vez que a un numero binario le aplico '[2:]', es para quitar la cadena 0b que pone python a las strings 
#Al haber decidido trabajar con strings, para cada operacion hay que convertir cada string a entero y a veces tambien a binario para conseguir el resultado como una combinacion de 1's y 0's

def calculateKi(k1,buffOld):#En esta funcion se calculan las ki a partir de ki-1
    #input'11001101' 8 bits
    b='10000000'
    c='11111111'

    buff=bin((int(k1,2)&int(b,2))>>7)#Con esta instruccion saco el digito que "desaparece" al desplazar los bits a la derecha tras hacer un and con un numero con todo ceros menos un uno en la posicion que quiero conservar

    ne=k1+buffOld[2:]#Con eso sumo el digito que desaparece de la anterior clave para seguir el ciclo
    
    next2=bin(int(ne,2)&int(c,2))#Como lo que queria era "eliminar" el bit de la izquierda del numero, y no me servia el desplazamiento, he hecho un and con un numero de 8 bits con todo unos ya que el que quiero modificar tiene 9 y asi conservo el numero original
    
    return [next2,buff]  

def calculateK1(k):#funciona de igual manera que "calculateKi", con la diferencia de que aqui partimos de la clave introducida por el usuario y no hace falta sumar nada
    #input'001111010' 9bits
    b='10000000'
    buffOld=bin((int(k,2)&int(b,2))>>7)

    k1=bin(int(k,2)>>1)
    
    return [k1,buffOld]

def boxS1(p1):#Este subprograma se encarga de la busqueda en la box s1 y devuelve el resultado
    #input'1101' 4 bits
    s1=[['100','101','110','111','010','001','011','000'],
    ['011','101','000','010','001','100','111','110']]

    p1_1=p1[0]
    p1_2_4=p1[1:]

    numBox1=s1[int(p1_1,2)][int(p1_2_4,2)]
    return numBox1

def boxS2(p2):#Este subprograma se encarga de la busqueda en la box s2 y devuelve el resultado
    #input'0111' 4 bits
    s2=[['100','000','110','111','101','001','010','011'],
    ['010','101','000','110','001','111','011','100']]

    p2_1=p2[0]
    p2_2_4=p2[1:]

    numBox2=s2[int(p2_1,2)][int(p2_2_4,2)]
    return numBox2

def expansion(a):#Este subprograma se encarga de la funcion de expansion del algoritmo, su inica labor es reordenar y duplicar algunos bits para conseguir 8 bits a partir de 6
    #input'011100' 6 bits
    lista=list(a)

    exp=lista[4]+lista[3]+lista[0]+lista[1]+lista[2]+lista[0]+lista[5]+lista[1]

    return exp


#De aqui a la linea 110, se recogen los datos proporcionados por el usuario y se comprueba que cumplan los requisitos del programa
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

lik=calculateK1(entr)#Calculamos k1
k=lik[0]
buffOld=lik[1]

#Dividimos el dato a codificar en las 2 partes necesarias para la codificacion
l=entrada[:6]
r=entrada[6:]

listaK=[]#Esta lista sirve para almacenar las claves usadas para la posterior decodificacion

for i in range(int(n)):

    k=k[2:]
    
    er=expansion(r)#Expandimos r
    
    listaK.append(k)
    erXORk=int(er,2)^int(k,2)#Hacemos la operacion XOR entre r expandido y la clave
    erXORk=bin(erXORk)
    
    t=erXORk[2:]
    
    le=len(t)
    #Como python recorta los ceros a la izquierda de los numeros, y es necesario que tenga 8 bits, con esto se rellena de ceros a la izquierda para llegar a 8 bits y se divide en t1 y t2 para hacer la posterior busqueda en las boxes
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

    f=s1+s2#Tras las busquedas en las cajas, formamo f como la concatenacion de s1 y s2

    #aqui actualizamos los valores de l y r para la siguiente pasada del bucle
    l1=l
    l=r
    r=int(l1,2)^int(f,2)
    r=bin(r)
    
    r=r[2:]
    #Con esto rellenamos los ceros a la izquierda de r hasta llegar a 6 bits
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

    lik=calculateKi(k,buffOld)#calculamos la siguiente clave
    k=lik[0]
    buffOld=lik[1]

print('dato cifrado:',r+l)#Mostramos el dato cifrado



#Comienza la desencriptacion, que es el mismo algoritmo que el de encriptacion, con la diferencia de que l hace las funciones de r y viceversa, que es lo que se hace en las lineas 196-198, y las claves se usan en orden inverso al usado en la encriptacion

ra=r
r=l
l=ra


k=listaK[int(n)-1]#Sacamos la ultima clave de la lista, dado que se han colocado en el ordend e uso

for i in range(int(n)):

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
    
    k=listaK[(int(n)-2)-i]#En esta linea se saca la clave de lalista en lugar de calcularla

print('dato descifrado:', r+l)#Se muestra el dato odiginal introducido por el usuario

