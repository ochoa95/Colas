import simpy
import random
import math



#Ingresa proceso al sistema si hay ram suficiente

def programa (env,nombre,cpu,ramP,esperar,delay,procesos,esperando):

    
    #print (mram.level)  #Imprime la memoria actual
    
    if mram.level > 0:  #Verifica si la memoria es suficiente, despues entra (NEW)
        global TiempoTotal
        global Lista1
        mram.get(ramP)
        yield env.timeout(esperar)
        x = env.now #Similar a la siguiente variable, pero se declara por aparte para facilitar los calculos
        a = env.now #Tiempo actual
        print ("El proceso %s solicita memoria (Tiempo de llegada: %s)" % (nombre,a))
        with cpu.request() as req:  #Verifica si esta desocupado el CPU (READY)
            yield req      
            #Ejecuta algunos procesos(RUNNING):
            for i in range(0,3):
                j = 0
                b = env.now
                print ("El proceso %s comenzo a usar el cpu (Tiempo de llegada: %s)" % (nombre,b))
                if  (procesos>0):
                    yield env.timeout(delay)
                    c = env.now
                    while (j < 3):
                        procesos = procesos - 1
                        j = j+1
                        print ("Ejecutando instrucciones del proceso %s(Tiempo de tardanza: %s)" % (nombre,c))
                        if procesos <= 0:
                            j = 3     
                    if (waitOready == 2):
                        env.timeout(esperando)
                        d = env.now
                        print ("El proceso %s esta esperando (Tiempo %s)" % (nombre,d))
                else:
                    f = env.now
                    print ("El proceso %s ha terminado (Tiempo %s)" % (nombre,f))
        y = env.now #Segundo tiempo para realizar calculos 
        mram.put(ramP)      #Devuelve la memoria utilizada (TERMINATED)
        #print (mram.level)  #Imprime la memoria actual
        #env.process(programa(i,ram,t,txp,instP))

    
#Variables
RAM = 10
NumDeProcesos = 10
RANDOM_SEED = 42
random.seed(RANDOM_SEED)
txp = 1
intervalo = 10
TiempoTotal = 0
Total = 0
Lista1 = []

    
################################################################
env = simpy.Environment()  #crear ambiente de simulacion
cpu = simpy.Resource(env, capacity=1) #Declaracion de la cantidad de CPU
mram = simpy.Container(env, init=RAM, capacity=RAM) #Declaracion de la cantidad de RAM







# crear los carros

for i in range(NumDeProcesos):
    
    #Declara algunas variables
    t = random.expovariate(1.0/intervalo)
    ram = random.randint (1,10)
    instP = random.randint (1,10)
    waitOready = random.randint (1,2)
    tespera = random.randint (1,10)
    

    #Ejecuta los procesos
    env.process(programa(env,i,cpu,ram,t,txp,instP,tespera))
    
# correr la simulacion
env.run()
        
