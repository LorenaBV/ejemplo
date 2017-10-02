inicial = [0, 0]

def vaciar1(estado):
  nuevo_estado = list(estado)
  nuevo_estado[0] = 0
  #print(estado, " => ", nuevo_estado)
  return nuevo_estado

def vaciar2(estado):
  nuevo_estado = list(estado)
  nuevo_estado[1] = 0
  #print(estado, " => ", nuevo_estado)
  return nuevo_estado

def llenar1(estado):
  nuevo_estado = list(estado)
  nuevo_estado[0] = 5
  #print(estado, " => ", nuevo_estado)
  return nuevo_estado

def llenar2(estado):
  nuevo_estado = list(estado)
  nuevo_estado[1] = 3
  #print(estado, " => ", nuevo_estado)
  return nuevo_estado

def verter1en2(estado):
  nuevo_estado = list(estado)
  capacidad2 = 3 - nuevo_estado[1]
  if(capacidad2 > nuevo_estado[0]):
    intercambio = nuevo_estado[0]
  else:
    intercambio = capacidad2
  nuevo_estado[0] -= intercambio
  nuevo_estado[1] += intercambio
  #print(estado, " => ", nuevo_estado)
  return nuevo_estado

def verter2en1(estado):
  nuevo_estado = list(estado)
  capacidad1 = 5 - nuevo_estado[0]
  if(capacidad1 > nuevo_estado[1]):
    intercambio = nuevo_estado[1]
  else:
    intercambio = capacidad1
  nuevo_estado[1] -= intercambio
  nuevo_estado[0] += intercambio
  #print(estado, " => ", nuevo_estado)
  return nuevo_estado

acciones = [vaciar1, vaciar2, llenar1, llenar2, verter1en2, verter2en1]

def meta(estado):
  return estado[0] + estado[1] == 4

def buscar(estados):
  if meta(estados[-1]):
    print(estados)
    exit()

  for accion in acciones:
    nuevo_estado = accion(estados[-1])
    if not nuevo_estado in estados:
      estados2 = list(estados)
      estados2.append(nuevo_estado)
      buscar(estados2)

buscar([inicial])
