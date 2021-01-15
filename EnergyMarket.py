import random
import threading
from multiprocessing import Manager, Value, Process, Lock, Event, Array, Pipe, Queue
import os
import time

delay = 3 #délai d'attente de 3 secondes (pour l'instant on a mis ça un peu aléatoirement)
price0=0.15375 #prix initial

gamma = 0,99 #is a long-term attenuation coefFicient
alpha0 = 0.001
beta0 = 0.01


def home(nb_of_homes, temperature, clock_ready):
    # 0 = always sell to market, 1 = always give away, 2 = sell if no takers
    id = int(os.getpid())
    while clock_ready.wait(delay): #Block until the internal flag is true.
        
        

def market(number_of_days, temperature, clock_ready,):
    current_price = price0
    """while clock_ready.wait(delay): 
        market_conn, external_conn = Pipe() #market et external sont connectés, comme external_events est un child process
        e = Process(target = external_events, args=(external_conn, clock_ready, number_of_days))
	    e.start()
        e.join()"""


def weather(temperature, clock_ready, weather_ready, weather_connection):
    
    while clock_ready.wait(1.5 * delay):
        temperature[0] = random.randint(-10,20) #temperature en degré
        weather_connection.send(temperature[0])
    
        weather_ready.set()
        time.sleep(delay/2)
	
def terminal(clock_ready):
    while clock_ready.wait(delay):


def external_events(clock_ready, number_of_days): #politics et economics
    #liste des evenements random:
    #~~ici mettre une liste des evenements randoms, par exemple civil war etc~~
    #un evenement random peut arriver (aussi de façon aléatoire) pendant un des jours
    for i in range(number_of_days):
            event = False
            rand = random.random()




def clock(clock_ready, number_of_days):
	c = 0
	
	while c < nb_of_days:
		clock_ready.set() #All threads waiting for the flag to become true are awakened. 
		c += 1
		time_i = time.time()
		
		while time.time() - time_i < delay:
			time.sleep(2)


if __name__ == "__main__":
    start = time.time()
    nb_of_days = input("Entrez le nombre de jours pour la simulation") #finalement on peut le mettre à l'infini et faire ctrl c pourstopper
    nb_of_homes = input("Entrez le nombre de maison au minimum 3")

    clock_ready = Event()



    c = Process(target = clock, args = (clock_ready, nb_of_days,))
    c.start()

    c.join()

