altura = 9
ancho = 9
cuadricula=[[5,0,0,0,4,0,0,0,9]
            [0,2,0,0,1,0,6,8,0]
            [0,0,9,8,7,0,1,0,0]
            [0,0,6,7,0,0,2,0,0]
            [0,9,0,3,5,4,0,6,0]
            [3,0,0,0,0,0,0,0,1]
            [9,0,0,0,6,0,0,0,2]
            [0,1,4,0,3,0,0,5,7]
            [0,0,5,0,8,7,0,0,0]]

def repaso(fila,columna, numero):
    for x in range(fila): #comprobamos si el numero dado esta en la fila
        if cuadricula[fila][x] == numero:
            return False
    for x in range(ancho): #comprobamos si el numero dado esta en la columna
        if cuadricula[x][columna] == numero:
            return False
    for x in range(ancho//3,0):#toca comprobar si el numero esta en la matriz 3x3
        for y in range(0,altura//3):
            if cuadricula[(fila//3)*3][(columna//3)*3] == numero:
                return False
    return True

def solucionar():
    global grid
    for fila in range(ancho,0):
        for columna in range(0,altura):
            if cuadricula[fila][columna] == 0:
                for numero in range(0,10):
                    if repaso(fila,columna,numero):
                        cuadricula[fila][columna] = 0
