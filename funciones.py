from numpy import ndarray
import numpy as np

def iniciar_campo()->ndarray:
    '''
    Doc:
    Esta función inicia el array que se utilizara para ser el 
    campo de juego.
    '''
    campo=np.array([["a","b","c"],
                    ["d","e","f"],
                    ["g","h","i"]])
    print(campo)
    return campo

def opcionesMov(campo:ndarray)->ndarray:
    '''
    Doc: Función para listar los indices en donde se pueden 
    colocar simbolos
    '''
    row=np.where((campo != "X") & (campo !="O"))[0]
    col = np.where((campo != "X") & (campo !="O"))[1]
    return row,col

def contar(campo:ndarray, simbolo:str)->int:
    '''
    Doc: Función para contar X y O, determina por fila cuantos 
    simbolos seguidos hay de cada uno y devuelve el máximo
    '''
    x=0
    for i in campo:
        row=np.where((i==simbolo))[0]
        x=max(x,len(row))
    return x

def diag(campo:ndarray, simbolo:str)->int:
    '''
    Doc: Función para contar X y O, determina para las diagona-
    les cuantos simbolos seguidos hay en cada uno y devuelve
    el máximo
    '''
    ds=np.array([campo[0][0],
                 campo[1][1],
                 campo[2][2]])
    di=np.array([campo[0][2],
                 campo[1][1],
                 campo[2][0]])
    ds_s=np.where((ds==simbolo))[0]
    di_s=np.where((di==simbolo))[0]
    return max(len(ds_s),len(di_s))

def final(campo:ndarray)->bool:
    '''
    Doc: Función que determina si el juego acabó,ya sea que hay 
    un ganador o que no hay más movimientos para hacer
    '''
    pf_x=contar(campo,"X")
    pc_x=contar(campo.T,"X")
    pd_x=diag(campo,"X")
    pf_o=contar(campo,"O")
    pc_o=contar(campo.T,"O")
    pd_o=diag(campo,"O")
    if (pf_x==3) | (pc_x==3) | (pd_x==3) | (pf_o==3) | (pc_o==3) | (pd_o==3):
        return True
    f,c=opcionesMov(campo)
    if len(f)==0:
        return True
    else:
        return False

def ganador(campo:ndarray)->str:
    '''
    Doc: Función que devuelve si el ganador fue el J1, la CPU o
    si hubó un empate
    '''
    pf_x=contar(campo,"X")
    pc_x=contar(campo.T,"X")
    pd_x=diag(campo,"X")
    pf_o=contar(campo,"O")
    pc_o=contar(campo.T,"O")
    pd_o=diag(campo,"O")
    if (pf_x==3) | (pc_x==3) | (pd_x==3):
        return "J1"
    elif (pf_o==3) | (pc_o==3) | (pd_o==3):
        return "CPU"
    else:
        return "Empate"
    
def utilidad(campo:ndarray)->int:
    '''
    Doc: Función que indica el ganador del encuentro o indica si 
    hay un empate
    '''
    winner=ganador(campo)
    if winner=="J1":
        return 1
    elif winner=="CPU":
        return -1
    elif winner=="Empate":
        return 0
    
def mover(campo:ndarray,jugada:list,jugador:str)->ndarray:
    '''
    Doc: Función para colocar un simbolo en el tablero
    '''
    if jugador=="J1":
        nuevo_campo=campo.copy()
        nuevo_campo[jugada[0],jugada[1]]="X"
    elif jugador=="CPU":
        nuevo_campo=campo.copy()
        nuevo_campo[jugada[0],jugada[1]]="O"
    return nuevo_campo
    


def mejor_mov(campo:ndarray)->list:
    '''
    Doc: Función para calcular dos pasos adelante cual es el 
    mejor movimiento que puede realizar el computador
    '''
    f,c=opcionesMov(campo)
    v=10000
    jugador="CPU"
    mejor=""
    for i,j in zip(f,c):
        cn=mover(campo,[i,j],jugador)
        if final(cn):
            d=utilidad(cn)
        else:
            row,col=opcionesMov(cn)
            v2=-10000
            for k,w in zip(row,col):
                cn2=mover(cn,[k,w],"J1")
                d=utilidad(cn2)
                if max(v2,d)==v2:
                    d=v2
                    next
                else:
                    v2=d
        print("-"*10+"CALCULANDO"+"-"*10)
        if min(v,d)==v:
            next
        else:
            v=d
            mejor=[i,j]
    return mejor,v

def ubicarEnCampo(campo:ndarray, valor:str)->ndarray:
    '''
    Doc: Función encargada de ubicar en el campo el lugar donde 
    el J1 va a poner una X y colocar la ficha
    '''
    row=np.where(campo == valor)[0][0]
    col = np.where(campo == valor)[1][0]
    nuevo_campo=mover(campo,[row,col],"J1")
    return nuevo_campo

def min_value(campo:ndarray)->any:
    if final(campo):
        return utilidad(campo)
    v=10000
    jugador="CPU"
    mejor=0
    f,c=opcionesMov(campo)
    for coord in enumerate(zip(f,c)):
        d,mejor=max_value(mover(campo,list(coord),jugador))
        if min(v,d)==v:
            next
        else:
            v=d
            mejor=list(coord)
    return v,mejor

def max_value(campo:ndarray)->any:
    if final(campo):
        return utilidad(campo)
    v=-10000
    jugador="J1"
    mejor=0
    f,c=opcionesMov(campo)
    for indice,coord in enumerate(zip(f,c)):
        d,mejor=min_value(mover(campo,list(coord),jugador))
        if max(v,d)==v:
            next
        else:
            v=d
            mejor=list(coord)
    return v,mejor
