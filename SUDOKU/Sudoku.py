altura = 9
ancho = 9
grid = [[5,0,0,0,4,0,0,0,9]
        [0,2,0,0,1,0,6,8,0]
        [0,0,9,8,7,0,1,0,0]
        [0,0,6,7,0,0,2,0,0]
        [0,9,0,3,5,4,0,6,0]
        [3,0,0,0,0,0,0,0,1]
        [9,0,0,0,6,0,0,0,2]
        [0,1,4,0,3,0,0,5,7]
        [0,0,5,0,8,7,0,0,0]]

def solucionar(fila,columna, numero):
    for x in range(fila): #comprobamos si el numero dado esta en la fila
        if grid[fila][x] == numero:
            return False
    for x in range(ancho): #comprobamos si el numero dado esta en la columna
        if grid[x][columna] == numero:
            return False
    for x in range(ancho//3):#toca comprobar si el numero esta en la matriz 3x3
        for y in range(altura//3):
            if grid[(fila//3)*3][(columna//3)*3] == numero:
                return False
    return True
