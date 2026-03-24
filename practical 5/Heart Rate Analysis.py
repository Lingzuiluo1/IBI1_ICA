import matplotlib.pyplot as plt
import numpy as np
#create a list of heart rates and calculate the average heart rate
heart_rate = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
total = sum(heart_rate)
patients_numbers = len(heart_rate)
average_heart_rate = total / patients_numbers
print(f"There are {patients_numbers} patients and the average heart rate: {average_heart_rate:.2f} bpm")
#difine three categories of heart rates and compare the number of each category
low = 0
normal = 0
high = 0
for rate in heart_rate:
    if rate < 60:
        low += 1
    elif 60 <= rate <= 100:
        normal += 1
    else:
        high += 1
heart_rate1 = {'Low rate': low, 'Normal rate': normal, 'High rate': high}
max_category = max(heart_rate1, key=heart_rate1.get)
print(f"low: {low}, normal: {normal}, high: {high}, and the largest categoty is {max_category}.")
#produce a pie chart of the three categories
labels = heart_rate1.keys()
sizes = heart_rate1.values()
autopct = '%1.1f%%'
plt.figure()
plt.pie(sizes, labels=labels, autopct=autopct, shadow=True, startangle=90)
plt.title('Heart Rate Categories')
plt.show()




