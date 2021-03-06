import simpy
import random

#
# el carro se conduce un tiempo y tiene que llegar a cargarse de energia
# luego puede continuar conduciendo
# Debe hacer cola (FIFO) en el cargador

# name: identificacion del carro
# bcs:  cargador de bateria
# driving_time: tiempo que conduce antes de necesitar carga
# charge_duration: tiempo que toma cargar la bateria

#--------------------------------------------------------------------------------
    #REALIZA LAS COLAS
    #with bcs.request() as req:  #pedimos conectarnos al cargador de bateria
        #yield req

        #    Charge the battery
        #print('%s starting to charge at %s' % (name, env.now))
        #yield env.timeout(charge_duration)
        #print('%s leaving the bcs at %s' % (name, env.now))
        #    se hizo release automatico del cargador bcs
#--------------------------------------------------------------------------
RAM = 100

#Ingresa proceso al sistema si hay ram suficiente
def new (ramP):
    global RAM

    #utilizar container para verificar si es posible tomar RAm e ingresar a procesos
    for i in range(ramP):
        with bcs.request() as req:  #pedimos conectarnos al cargador de bateria
            yield req
        #    tomar ram de SO
        
def wait (esperar):

    yield env.timeout(esperar)

    
def running (delay,procesos):

    for i in range(3):
        if  (procesos>0):
            yield env.timeout(delay)
            procesos = procesos - 1
        #if (procesos == 0):        #PUSE UN NUMERAL AQUI PARA PODER PARAR EL ERROR DE INDENTED BLOCK 
            #devolver ram



    
        
    
    
    
################################################################
env = simpy.Environment()  #crear ambiente de simulacion
bcs = simpy.Resource(env, capacity=100) #Declaracion de la cantidad de RAM para los procesos

RANDOM_SEED = 42
random.seed(RANDOM_SEED)
interval = 10 #SAQUE ESTE ELEMENTO DEL CICLO



# crear los carros

for i in range(5):
    
    
    t = random.expovariate(1.0/interval)
    ram = random.randint (1,10)
    tiempoXproceso = 1
    instP = random.randint (1,10)
    env.process(new(ram))
    env.process(running(tiempoXproceso,instP))
    waitOready = random.randint (1,2)
    if (waitOready == 1):
        env.process(wait(t))    #CAMBIE EN ESTA LINEA LA PALABRA READY POR WAIT

# correr la simulacion
env.run()
