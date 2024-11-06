#Juego NIM : Fila de Objetos
#1era Implementacion

import random
import time 
import os

def pres_1():
    print("NIM")
    print("Gana quien toma el ultimo palillo")
    print("1. Aleatorio")
    print("2. IA")
    nivel = ""
    while nivel != "1" and nivel != "2":
        nivel = input()
    return nivel
def pres_2(objetos, quita):
    print("NIM")
    print("Habra {} objetos en total".format(objetos))
    print("Sacar minimo 1 y  maximo {} objetos".format(quita))
    print("Empiezas...")
    input("Presiona Enter para comenzar")
def sorteo_opciones():
    #objetos = random.randint(16,23)
    #quita = random.randint(3,5)
    objetos =20
    quita = 3 
    return objetos, quita
def area_de_juego(objetos, quita):
    print("NIM")
    for fila in range(4):
        print(end= " ")
        for p in range(1, objetos+1):
            print("|", end=" ")
            if p % quita == 0:
                print(end=" ")
        print()
def movimiento_jugador(objetos, quita):
    if quita == 3:
        quita = ("1", "2", "3")
    '''
    elif quita == 4:
        quita = ("1", "2", "3", "4")
    if quita == 5:
        quita = ("1", "2", "3","4","5")
    '''
    q = input("sacas: ")
    while q not in quita or int(q) > objetos:
        if q not in quita:
            q = input("Saca minimo 1 y  maximo {} objetos".format(len(quita))) 
        elif int(q) > objetos:
            q = input("Quedan {} objetos".format(objetos))
    else: 
        objetos_quita = int(q)
    return objetos_quita        
        
def movimiento_ordenador_random(objetos, quita):
    if objetos <= quita:
        objetos_quita = objetos
    else:
        objetos_quita = random.randint(1, quita)
        while objetos_quita > objetos:
            objetos_quita = random.randint(1,quita)
    return objetos_quita

def movimiento_ordenador_ia(objetos, quita):
    objectos_quita=None
    while objectos_quita is None or objectos_quita > objetos:
        if objetos <= quita:
            objectos_quita = objetos
        #EstrategiaGanadora: Dejar un objeto mas del que se puede quitar
        #elif objetos % (quita+1) == 5:
        #    objectos_quita = 5
        #elif objetos % (quita+1) == 4:
        #    objectos_quita = 4
        elif objetos % (quita+1) == 3:
            objectos_quita = 3
        elif objetos % (quita+1) == 2:
            objectos_quita = 2
        elif objetos % (quita+1) == 1:
            objectos_quita = 1
        elif objetos % (quita+1) == 0:
            objectos_quita = random.randint(1,3)
        print("Hay: ", objetos,"palitos ","   Saco: ",objectos_quita)
        print("Quedan:", objetos-objectos_quita," palitos ")
    return objectos_quita

def mostrar_ganador(turno):
    if turno == 2:
        print("Gana Jugador 2")
    elif turno == 1:
        print("Gana Jugador 1")
    
#Main
turno =1 
objetos, quita = sorteo_opciones()
#os.system("cls")
#nivel=pres_1()
#os.system("cls")
pres_2(objetos, quita)  
jugando = True
while jugando:
    #os.system("cls")
    area_de_juego(objetos,quita)
    if turno==1:
        jugada = movimiento_jugador(objetos,quita)
        turno=2
    elif turno==2:
        time.sleep(1)
        '''if nivel == "1":
            jugada = movimiento_ordenador_random(objetos,quita)
        elif nivel == "2":
            jugada = movimiento_ordenador_ia(objetos,quita)
        '''
        jugada = movimiento_jugador(objetos,quita)
        #jugada = movimiento_ordenador_ia(objetos,quita)
        turno = 1
    objetos = objetos - jugada
    if objetos == 0:
        #os.system("cls")
        mostrar_ganador(turno)
        jugando=False 
