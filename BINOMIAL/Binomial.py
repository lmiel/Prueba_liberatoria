""" Tenemos que elaborar (ax+b)^n
    esto es: (ax+b)*(ax+b)*(ax+b)*....*(ax+b)  n numero de veces
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def combi(j,n):
    return(int(factorial(n)/(factorial(n-j)*factorial(j))))

def coef(ex):
    i=1
    lista = []
    for j in range(2,len(ex)): #The len() function returns the number of items (length) in an object.
        if ex[j] == "+" or ex[j] == "-":
            if j == 2:
                lista.append(1)
                lista.append(ex[j-1])
            else:
                lista.append(int(ex[1:j-1]))
                lista.append(ex[j-1])
            i=j    
        if ex[j] == ")":
            lista.append(int(ex[i:j]))
            i=j+2
    lista.append(int(ex[i:len(ex)]))
    return(lista)
