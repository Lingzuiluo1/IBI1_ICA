#import some functions
import numpy as np
import matplotlib.pyplot as plt
#define the basic variables
population = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
##Add vaccination rates
vaccine_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
##Create a canvas in advance to present multiple curves in the same figure
plt.figure(figsize=(6,4), dpi=150)
#initialize people in different state
##after vaccination
for v in vaccine_rates:
     vaccinated = int(population * v)
     S = max(0, 9999 - vaccinated)
     I = 1
     R = 0
     #create arrays to record people in different state(##only I)
     I_list = [I]
     #start the loop
     for step in range(time_steps):
     #calculate the infection probability
       infection_probability = beta * (I / population)
       # calculate new infected people
       if S > 0:
        new_infected = np.random.choice([0, 1], size=S, p=[1-infection_probability, infection_probability]).sum()
       else:  
        new_infected = 0
        #calculate new recovered people
       if I > 0:
        new_recovered = np.random.choice([0, 1], size=I, p=[1-gamma, gamma]).sum()
       else:
        new_recovered = 0
       #update S、I、R
       S = S - new_infected
       I = I + new_infected - new_recovered
       R = R + new_recovered
       #save to the list(##only I)
       I = int(I)
       I_list.append(I)
     #make a figure
     plt.plot(I_list, label=f'{int(v*100)}%')
plt.xlabel('Time')
plt.ylabel('population') 
plt.title('SIR Model with different vaccination rates') 
plt.legend(loc='upper right', fontsize=8)
plt.ylim(-200, 6000)
plt.savefig('SIR_vaccination.png', format = 'png')
plt.show()
