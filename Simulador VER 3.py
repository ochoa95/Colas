import simpy
import random
import queue

RAM = 100
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

#Ingresa proceso al sistema si hay ram suficiente

def programa (nombre,ramP,esperar,delay,procesos):
    global RAM
    with mram.request() as req:  #Verifica si es posible tomar RAM e ingresar a procesos(NEW)
        yield req
        yield env.timeout(esperar)
        print ("El proceso %s solicita memoria (Tiempo de llegada: %s)" % (nombre,env.now))

        with cpu.request() as req:  #Verifica si esta desocupado el CPU (READY)
            yield req      
            #Ejecuta algunos procesos(RUNNING):
            for i in range(3):
                if  (procesos>0):
                    yield env.timeout(delay)
                    procesos = procesos - 1
                    print ("Ejecutando instruccion %s del proceso %s(Tiempo de tardanza: %s)" % (i,nombre,env.now))
             
    
    
    
################################################################
env = simpy.Environment()  #crear ambiente de simulacion
cpu = simpy.Resource(env, capacity=1) #Declaracion de la cantidad de CPU
mram = simpy.Resource(env, capacity=100) #Declaracion de la cantidad de CPU







# crear los carros

for i in range(10):
    
    #Declara algunas variables
    interval = 10
    t = random.expovariate(1.0/interval)
    ram = random.randint (1,10)
    tiempoXproceso = 1
    instP = random.randint (1,10)
    waitOready = random.randint (1,2)

    #Ejecuta los procesos
    env.process(programa(i,ram,t,tiempoXproceso,instP))
    
# correr la simulacion
env.run()
        
