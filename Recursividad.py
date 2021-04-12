#Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a. Ejemplo:

#posiciones_de("Un tete a tete con Tete", "te")
#[3, 5, 10, 12, 21]

arr = "un tete a tete con Tete"
busqueda = "te"

def posicion(a,b):
  posArr = []
  pos = a.find(b)
  while True:
    if pos == -1: break
    else:
      posArr.append(pos)
      pos = a.find(b, pos + 1)
  return posArr
  
print (posicion(arr,busqueda))