import simpy
import random
import queue



#Ingresa proceso al sistema si hay ram suficiente

def programa (nombre,ramP,esperar,delay,procesos):

    
    print (mram.level)  #Imprime la memoria actual
    if mram.level > 0: #Verifica si la memoria es suficiente, despues entra (NEW)
        mram.get(ramP)
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

                    
        mram.put(ramP)      #Devuelve la memoria utilizada (TERMINATED)
        print (mram.level)  #Imprime la memoria actual
        #env.process(programa(i,ram,t,txp,instP))

    
#Variables
RAM = 100
NumeroDeProgramas = 5
RANDOM_SEED = 42
random.seed(RANDOM_SEED)
txp = 1   
    
################################################################
env = simpy.Environment()  #crear ambiente de simulacion
cpu = simpy.Resource(env, capacity=1) #Declaracion de la cantidad de CPU
mram = simpy.Container(env, init=RAM, capacity=RAM) #Declaracion de la cantidad de RAM







# crear los carros

for i in range(NumeroDeProgramas):
    
    #Declara algunas variables
    interval = 10
    t = random.expovariate(1.0/interval)
    ram = random.randint (1,10)
    instP = random.randint (1,10)
    waitOready = random.randint (1,2)

    #Ejecuta los procesos
    env.process(programa(i,ram,t,txp,instP))
    
# correr la simulacion
env.run()
        
