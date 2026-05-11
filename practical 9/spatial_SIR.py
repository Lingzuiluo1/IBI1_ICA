import numpy as np
import matplotlib.pyplot as plt
# 参数设置
population = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
# 疫苗比例
vaccine_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.figure(figsize=(6,4), dpi=150)
# 遍历每个疫苗接种率
for v in vaccine_list:
     vaccinated = int(population * v)
     S = population - vaccinated - 1
     I = 1
     R = 0
     I_history = [I]
     
     # 时间循环
     for step in range(time_steps):
         infect_prob = beta * (I / population)
         
         new_infected = 0
         for i in range(S):
             if np.random.rand() < infect_prob:
                 new_infected += 1
         
         new_recovered = 0
         for i in range(I):
             if np.random.rand() < gamma:
                 new_recovered += 1
         
         S = S - new_infected
         I = I + new_infected - new_recovered
         R = R + new_recovered
         I_history.append(I)
     
     # 画图
     plt.plot(I_history, label=f'{int(v*100)}%')
plt.xlabel('Time')
plt.ylabel('Infected')
plt.title('SIR with Different Vaccination Rates')
plt.legend(bbox_to_anchor=(1,1))
plt.show()