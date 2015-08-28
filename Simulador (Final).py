#SIMULADOR DE PROGRAMAS HDT5
#SAMUEL DIAZ 14083
#JOSE ANGEL OCHOA 14230

#Modulos necesarios
import simpy
import random
import math

#Desviacion estandar
def DE(l, m):
     global w
     for i in range(0,len(l)):
          v = l[i]
          v = v - m
          v = v**2
          w = w + v
          w = w/float(len(l))
          return math.sqrt(w)



#Ingresa proceso al sistema si hay ram suficiente
def programa (env,nombre,cpu,ramP,esperar,delay,instrucciones,esperando,num,CCPUU):
    
    if mram.level > 0:  #Verifica si la memoria es suficiente, despues entra (NEW)
        #Debe sacar estas variables
        global TiempoTotal
        global Lista1
        
        #Toma RAM y espera segun el tiempode llegada
        mram.get(ramP)
        yield env.timeout(esperar)
        x = env.now #Similar a la variable "a", pero se declara por aparte para facilitar los calculos
        a = env.now #Tiempo actual
        print ("El proceso %s solicita memoria (Tiempo de llegada: %s)" % (nombre,a))
        with cpu.request() as req:  #Verifica si esta desocupado el CPU (READY)
            yield req      
            #Ejecuta algunos procesos(RUNNING):
            for i in range(0,3):
                j = 0
                b = env.now
                print ("El proceso %s comenzo a usar el cpu (Tiempo de llegada: %s)" % (nombre,b))
                if  (instrucciones>0): #Verifica si hay suficientes instrucciones
                    yield env.timeout(delay)
                    c = env.now
                    while (j < CCPUU):
                        instrucciones = instrucciones - 1
                        j = j+1 #Resta procesos hasta que la capacidad de procesar del cpu llega al limite
                        print ("Ejecutando instrucciones del proceso %s(Tiempo de tardanza: %s)" % (nombre,c))
                        if instrucciones <= 0:
                            j = CCPUU   
                    if (waitOready == 2):
                        #Espera si es necesario, hasta 10 segundos
                        yield env.timeout(esperando)
                        d = env.now
                        print ("El proceso %s esta esperando (Tiempo %s)" % (nombre,d))
                    
                else:
                    #Termina el proceso si ya no hay instrucciones
                    f = env.now
                    print ("El proceso %s ha terminado (Tiempo %s)" % (nombre,f))
                    
        y = env.now #Segundo tiempo para realizar calculos
        z = y - x #Tiempo de duracion del proceso
        Lista1.append(z)
        TiempoTotal= TiempoTotal + z
        mram.put(ramP)      #Devuelve la memoria utilizada (TERMINATED)

    
#Variables
RANDOM_SEED = 42                #RANDOM SEED
random.seed(RANDOM_SEED)        
RAM = 100                       #Capacidad de la RAM
NumDeProcesos = 25              #Cantidad de procesos
CCPU = 3                        #Capacidad de instrucciones del CPU
txp = 1                         #Unidad de tiempo del CPU
NoCPU = 1                       #Cantidad de CPUs
 
#Otras variables
intervalo = 10                  
TiempoTotal = 0
Lista1 = []
w = 0

    
#Variables para cambiar el entorno de simpy
env = simpy.Environment()  #crear ambiente de simulacion
cpu = simpy.Resource(env, capacity=NoCPU) #Declaracion de la cantidad de CPU
mram = simpy.Container(env, init=RAM, capacity=RAM) #Declaracion de la cantidad de RAM







# crear los carros

for i in range(NumDeProcesos):
    
    #Declara algunos parametros para simular el programa
    t = random.expovariate(1.0/intervalo)
    ram = random.randint (1,10)
    instP = random.randint (1,10)
    waitOready = random.randint (1,2)
    tespera = random.randint (1,10)
    

    #Ejecuta los procesos
    env.process(programa(env,i,cpu,ram,t,txp,instP,tespera,NumDeProcesos,CCPU))
    
#Ejecuta la simulacion
env.run()


#Imprime los datos
p = TiempoTotal/NumDeProcesos
D = DE(Lista1, p)
print ("Tiempo promedio del proceso: %s" % (p))
print("Desviacion estandar: %s" % (D))
        
