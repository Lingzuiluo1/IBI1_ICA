#import some functions
import numpy as np
import matplotlib.pyplot as plt
#define the basic variables
population = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
#initialize people in different state
S = 9999
I = 1
R = 0
#create arrays to record people in different state
S_list = [S]
I_list = [I]
R_list = [R]
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
     #save to the list
     S_list.append(S)
     I_list.append(I)
     R_list.append(R)
 #make a figure
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Population') 
plt.title('SIR Model') 
plt.legend()
plt.savefig('SIR_Model.png', format = 'png')
plt.show()